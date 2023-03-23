class piece:
    def __init__(self, type, pos, color):
        self.type = type
        self.pos = pos
        self.color = color
        self.hasMoved = False
        self.enPassant = False
        
    def possibleMoves(self):
        moves = []
        if self.type == "pawn":
            if self.hasMoved == False:
                if self.color == "white":
                    pass
                
        elif self.type == "rook":
            pass
        elif self.type == "knight":
            pass
        elif self.type == "bishop":
            pass
        elif self.type == "queen":
            pass
        elif self.type == "king":
            pass
        #return(moves)
        
    def move(self, pos):
        pass
        
        
board = [
            [piece('rook', [0,0], 'black'), piece('knight', [0,1], 'black'), piece('bishop', [0,2], 'black'), piece('queen', [0,3], 'black'), piece('king', [0,4], 'black'), piece('bishop', [0,5], 'black'), piece('knight', [0,6], 'black'), piece('rook', [0,7], 'black')],
            [piece('pawn', [1,0], 'black'), piece('pawn', [1,1], 'black'), piece('pawn', [1,2], 'black'), piece('pawn', [1,3], 'black'), piece('pawn', [1,4], 'black'), piece('pawn', [1,5], 'black'), piece('pawn', [1,6], 'black'), piece('pawn', [1,7], 'black')],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [piece('pawn', [6,0], 'white'), piece('pawn', [6,1], 'white'), piece('pawn', [6,2], 'white'), piece('pawn', [6,3], 'white'), piece('pawn', [6,4], 'white'), piece('pawn', [6,5], 'white'), piece('pawn', [6,6], 'white'), piece('pawn', [6,7], 'white')],
            [piece('rook', [7,0], 'white'), piece('knight', [7,1], 'white'), piece('bishop', [7,2], 'white'), piece('queen', [7,3], 'white'), piece('king', [7,4], 'white'), piece('bishop', [7,5], 'white'), piece('knight', [7,6], 'white'), piece('rook', [7,7], 'white')]
        ]
print(board)