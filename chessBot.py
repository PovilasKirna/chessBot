from stockfish import Stockfish
            
class Chess:
    def __init__(self):
        self.stockfish = Stockfish()
        self.selected = False
        self.moves = []
        self.yourTurn = True
                
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
        
    def help(self):
        print("HELP")
        
    def exit(self):
        exit()

if __name__ == '__main__':
    chessGame = Chess()
    chessGame.getSide()
    while True: 
        if chessGame.yourTurn:
            action = input("White's Move / Action: ")
        else:
            action = input("Black's Move / Action: ")
        if chessGame.isMoveLegal(action):
            move = action
            if chessGame.yourTurn:
                chessGame.makeMove(move)
                chessGame.switchTurn()
            else:
                chessGame.makeMove(move)
                chessGame.switchTurn()
        else:
            action = action.upper()
            if action == "EXIT":
                chessGame.exit()
            elif action == "BOARD":
                chessGame.printBoard()
            elif action == "HELP":
                chessGame.help()
            else:
                print("Illegal or unrecognised move or command")

    
    
    """
        implement difficulty
        
        other settings of stockfish

        make a help menu 
        
        add commands like:
        
        toggle best move 
        toggle live score 
        
    """