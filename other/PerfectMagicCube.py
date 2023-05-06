import os
import copy

myCube = [[[17,8,61,44],[15,42,19,54],[52,21,48,9],[46,59,2,23]],[[10,47,22,51],[40,49,12,29],[27,14,55,34],[53,20,41,16]],[[64,25,36,5],[18,7,62,43],[45,60,1,24],[3,38,31,58]],[[39,50,11,30],[57,32,37,4],[6,35,26,63],[28,13,56,33]]]
cube0 = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
sum = 130
settingsFile = os.path.expanduser('~/Desktop/Python/cube.txt')

def printCube(cube):
    print('\n')
    for i in cube:
        for j in i:
            row = ''
            for k in j:
                row += str(k) + ' '
            print(row)
        print('\n')

def checkMagic(cube):
    #Repetitions
    list0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for square in cube:
        for row in square:
            for box in row:
                list0[box-1] += 1
    for i in list0:
        if i != 1:
            return(False)
    #Rows
    for square in cube:
        for row in square:
            check = 0
            for box in row:
                check += box
            if check != sum:
                return(False)
    #Columns
    for square in cube:
        for col in range(4):
            check = 0
            for box in range(4):
                check += square[box][col]
            if check != sum:
                return(False)
    #Height
    for i in range(4):
        for j in range(4):
            check = 0
            for k in range(4):
                check += cube[k][j][i]
            if check != sum:
                return(False)
    return(True)

def main():
    cubeIdx = []
    data = 0
    for i in range(64):
        cubeIdx.append(data)
        data += 1
    while cubeIdx[63] != 64:
        oldList = copy.copy(cubeIdx)
        for n,obj in enumerate(cubeIdx):
            if obj > 64:
                cubeIdx[n] = 0
                cubeIdx[n+1] += 1
        if oldList[3] != cubeIdx[3]:
            print(cubeIdx)
        cube = cube0
        place = 0
        for x,i in enumerate(cube):
            for y,j in enumerate(i):
                for z,k in enumerate(j):
                    cube[x][y][z] = cubeIdx[place]
                    place += 1
        response = checkMagic(cube)
        if response:
            print(response)
            file = open(settingsFile)
            fileLines = file.readlines()
            file.close()
            file = open(settingsFile, 'w')
            rewrite = ''
            for i in fileLines:
                rewrite += i
            stringList = ''
            for i in cube:
                for j in i:
                    for k in j:
                        stringList += str(k) + ','
            rewrite += stringList + '\n'
            file.write(rewrite)
            file.close()
        cubeIdx[0] += 1

test = checkMagic(myCube)
if test:
    print(test)
    file = open(settingsFile)
    fileLines = file.readlines()
    file.close()
    file = open(settingsFile, 'w')
    rewrite = ''
    for i in fileLines:
        rewrite += i
    stringList = ''
    for i in myCube:
        for j in i:
            for k in j:
                stringList += str(k) + ','
    rewrite += stringList + '\n'
    file.write(rewrite)
    file.close()
main()
printCube(cube0)
