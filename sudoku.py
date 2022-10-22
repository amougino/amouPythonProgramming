import time
import copy
import os

mySudokuFile = os.path.expanduser('~/toFillIn/sudoku.txt')

def getBoard(sudokuFile):
    file = open(sudokuFile)
    fileLines = file.readlines()
    file.close()
    for rowIdx,row in enumerate(fileLines):
        fileLines[rowIdx] = row.split('\n')
    for rowIdx,row in enumerate(fileLines):
        fileLines[rowIdx] = row[0].split(' ')
    for rowIdx,row in enumerate(fileLines):
        for squareIdx,square in enumerate(row):
            fileLines[rowIdx][squareIdx] = int(square)
    return(fileLines)

def printBoard(boa):
	for row in boa:
    		print(*row)

def findEmpty(boa):
    empties = []
    for rowIdx,row in enumerate(boa):
        for colIdx,col in enumerate(row):
            if boa[rowIdx][colIdx] == 0:
                empties.append([rowIdx,colIdx])
    return(empties)

def valid(boa, row, col, num):
    for i in boa[row]:
        if i == num:
            return False
    for i in boa:
        if i[col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(startRow,startRow+3):
    	for j in range(startCol,startCol+3):
            if boa[i][j] == num and (i,j) != (row,col):
                return False
    return True

def solveBoard(boa):
    finished = False
    while finished == False:
        lastBoa = copy.deepcopy(boa)
        pos = findEmpty(boa)
        if len(pos) == 0:
            return(boa)
        else:
            for blanks in pos:
                numList = []
                row = blanks[0]
                col = blanks[1]
                for num in range(1,10):
                    if valid(boa,row,col,num):
                        numList.append(num)
                if len(numList) == 1:
                    boa[row][col] = numList[0]
        time.sleep(1)
        if lastBoa == boa:
            return(boa)

#printBoard(solveBoard(getBoard(mySudokuFile)))