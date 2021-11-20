from stockfish import Stockfish
import time
import chess

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
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
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

            
class Chess:
    def __init__(self):
        self.stockfish = Stockfish()
        self.selected = False
        self.moves = []
        self.side = self.getSide()
        self.yourTurn
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
        
    def exit(self):
        exit()
        
    def printAdvantage(self):
        wAdv = 1
        bAdv = 1
        evaluation = self.stockfish.get_evaluation()
        cp = evaluation["value"]
        currentMoveAdvantage = round((1/(1+10**(-1*cp/4))), 2) #gives advantages after a player did a move for the oponent who will do the move
        print(cp, currentMoveAdvantage)
        # if self.side == "WHITE" and self.yourTurn:
        #     wAdv = 

            
        # print("White advantage: ", wAdv, " Black advantage: ", bAdv)
        """
        possible outcomes:
        Your turn youre black -> black
        Your turn youre white -> white
        Not your turn youre black -> white
        Not your turn youre white -> black
        """


        # l = 100
        # # Initial call to print 0% progress
        # printProgressBar(currentMoveAdvantage*100, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        # for i in range(0, l):
        #     # Do stuff...
        #     time.sleep(0.01)
        #     # Update Progress Bar
        #     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

        
    def play(self):
        while True:
            if self.side == "BLACK" and not self.yourTurn:
                action = input("White's Move / Action: ")
            elif self.side == "BLACK" and self.yourTurn:
                if self.settings["bestMove"] == 1:
                    bestMove = self.getBestMove()
                    print(bestMove)
                action = input("Black's Move / Action: ")

            elif self.side == "WHITE" and not self.yourTurn:
                action = input("Black's Move / Action: ")
            else:
                if self.settings["bestMove"] == 1:
                    bestMove = self.getBestMove()
                    print(bestMove)
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
                else:
                    print("Illegal/unrecognised move or command")
                # elif action == "SETTINGS" or "SET":
                #     print("Settings page")
                #     back = False
                #     while not back:
                #         choice = input("Choose setting to change it: ")
                #         if choice.upper() == "BACK":
                #             back = True


if __name__ == '__main__':
    chessGame = Chess()    
    chessGame.play()
    
    
    
    """
        implement difficulty
        
        other settings of stockfish

        make a help menu 
        
        add commands like:
        
        toggle best move 
        toggle live score 
        
    """