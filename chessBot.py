from stockfish import Stockfish
import time
import chess

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\n"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\n{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

            
class Chess:
    def __init__(self):
        self.stockfish = Stockfish()
        self.selected = False
        self.moves = []
        self.settings = {
            'bestMove' : 1,
            'advantage' : 1
        }
                
    def getSide(self):
        acceptedAnswers = [
            ["WHITE", "W"],
            ["BLACK", "B"]
        ]
        while not self.selected:
            side = input("Input the side you're playing on: ")
            side = side.upper()
            if side in acceptedAnswers[0]:
                self.yourTurn = True
                self.selected = True
                return "WHITE"
            elif side in acceptedAnswers[1]:
                self.yourTurn = False
                self.selected = True
                return "BLACK"
            elif side == "EXIT":
                self.exit()
        
    
    def isMoveLegal(self, move):
        return self.stockfish.is_move_correct(move)
        
    def getBestMove(self):
        return self.stockfish.get_best_move()
    
    def switchTurn(self):
        if self.yourTurn:
            self.yourTurn = False
        else:
            self.yourTurn = True
    
    def printBoard(self):
        print(self.stockfish.get_board_visual())
        
    def makeMove(self, move):
        self.moves.append(move)
        self.stockfish.set_position(self.moves)
        self.switchTurn()
        
    def help(self):
        print("HELP")
        
    def settingsPage(self):
        print("Settings page")
        back = False
        while not back:
            choice = input("Choose setting to change it: ")
            if choice.upper() == "BACK":
                back = True
        
        
    def exit(self):
        exit()
        
    def printAdvantage(self):
        evaluation = self.stockfish.get_evaluation()
        cp = evaluation["value"]
        pawnAdvantage = cp/100
        currentMoveAdvantage = round((1/(1+10**(-1*pawnAdvantage/4))), 2) 
        printProgressBar(currentMoveAdvantage*100, 100, prefix = 'Advantage:', suffix = "", length = 50)
        
    def start(self):
        while True:
            choice  = input("Welcome to the chessBot \n \nTo play: PLAY \nTo access Settings: SETTINGS \nTo get help: HELP \nTo Exit: EXIT \n \nInput your choice: ")
            choice = choice.upper()
            if choice == "EXIT":
                self.exit()
            elif choice == "SETTINGS":
                self.settingsPage()
            elif choice == "HELP":
                self.help()
            elif choice == "PLAY":
                self.play()
        
    def play(self):
        self.side = self.getSide()
        while True:
            self.printAdvantage()
            if self.side == "BLACK" and not self.yourTurn:
                action = input("White's Move / Action: ")
            elif self.side == "BLACK" and self.yourTurn:
                if self.settings["bestMove"] == 1:
                    bestMove = self.getBestMove()
                    print("Black's best move: ", bestMove)
                action = input("Black's Move / Action: ")

            elif self.side == "WHITE" and not self.yourTurn:
                action = input("Black's Move / Action: ")
            else:
                if self.settings["bestMove"] == 1:
                    bestMove = self.getBestMove()
                    print("White's best move: ", bestMove)
                action = input("White's Move / Action: ")
           
            if self.isMoveLegal(action):
                self.makeMove(action)
            else: #if the move is illegal it's most likely a command
                action = action.upper()
                if action == "EXIT":
                    self.exit()
                elif action == "BOARD":
                    self.printBoard()
                elif action == "HELP":
                    self.help()
                elif action == "SETTINGS":
                    self.settingsPage()
                else:
                    print("Illegal/unrecognised move or command")


if __name__ == '__main__':
    chessGame = Chess()    
    chessGame.start()
    
    
    
    """
        implement difficulty
        
        other settings of stockfish

        make a help menu 
        
        add commands like:
        
        toggle best move 
        toggle live score 
        
    """