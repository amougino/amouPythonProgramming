board = "WR WC WB WK WQ WB WC WR-WP WP WP WP WP WP WP WP-OO OO OO OO OO OO OO OO-OO OO OO OO OO OO OO OO-OO OO OO OO OO OO OO OO-OO OO OO OO OO OO OO OO-BP BP BP BP BP BP BP BP-BR BC BB BK BQ BB BC BR".split("-")
for i in range(len(board)):
  board[i] = board[i].split(" ")

def flipList(list):
  return(list[::-1])

def flipB(list):
  for i in range(len(list)):
    list[i] = flipList(list[i])
  return(list[::-1])
    
def showBoard(board):
  print("   -------------------------")
  for i in board:
    line = "   |"
    for j in i:
      line += j + "|"
    print(line)
  print("   -------------------------")

def movePiece(board,piece,loc):
  board[int(loc[0])][int(loc[1])] = board[int(piece[0])][int(piece[1])]
  board[int(piece[0])][int(piece[1])] = "OO"
  return(board)
while True:
  board = flipB(board)
  showBoard(board)
  a = input("piece ").split(".")
  b = input("loc ").split(".")
  board = movePiece(board,a,b)