import random
import PIL.Image as Img
import os
import copy

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

def saveImg(img, path, name):
    file = os.path.expanduser(path + name)
    print(file)
    img.save(file)

def display(img):
    img.show()

def countPossibleMovements(img, lastPos, pos, imgSize, pathColor, wallColor):

    xPos = pos[0]
    yPos = pos[1]
    up = (xPos, yPos - 1)
    right = (xPos + 1, yPos)
    down = (xPos, yPos + 1)
    left = (xPos - 1, yPos)
    
    possibleMovements = []
    if up[1] > 0:
        if img.getpixel(up) != wallColor:
            if img.getpixel((xPos, yPos - 2)) != pathColor:
                possibleMovements.append((xPos, yPos - 2))
    if right[0] < imgSize[0]:
        if img.getpixel(right) != wallColor:
            if img.getpixel((xPos + 2, yPos)) != pathColor:
                possibleMovements.append((xPos + 2, yPos))
    if down[1] < imgSize[1]:
        if img.getpixel(down) != wallColor:
            if img.getpixel((xPos, yPos + 2)) != pathColor:
                possibleMovements.append((xPos, yPos + 2))
    if left[0] > 0:
        if img.getpixel(left) != wallColor:
            if img.getpixel((xPos - 2, yPos)) != pathColor:
                possibleMovements.append((xPos - 2, yPos))

    if lastPos in possibleMovements:
        possibleMovements.pop(possibleMovements.index(lastPos))
    return(possibleMovements)

def addWalls(img, lastPos, pos, imgSize, pathColor, wallColor):

    xPos = pos[0]
    yPos = pos[1]
    up = (xPos, yPos - 2)
    right = (xPos + 2, yPos)
    down = (xPos, yPos + 2)
    left = (xPos - 2, yPos)

    if up[1] >= 0:
        if img.getpixel(up) == pathColor:
            if up != lastPos:
                img.putpixel((xPos, yPos - 1), wallColor)
    if right[0] < imgSize[0]:
        if img.getpixel(right) == pathColor:
            if right != lastPos:
                img.putpixel((xPos + 1, yPos), wallColor)
    if down[1] < imgSize[1]:
        if img.getpixel(down) == pathColor:
            if down != lastPos:
                img.putpixel((xPos, yPos + 1), wallColor)
    if left[0] >= 0:
        if img.getpixel(left) == pathColor:
            if left != lastPos:
                img.putpixel((xPos - 1, yPos), wallColor)

    return(img)

def findNewPath(img, lastPos, pos, imgSize, wallColor, turn):
    xPos = pos[0]
    yPos = pos[1]
    up = [(xPos, yPos - 1),(xPos, yPos - 2)]
    right = [(xPos + 1, yPos),(xPos + 2, yPos)]
    down = [(xPos, yPos + 1),(xPos, yPos + 2)]
    left = [(xPos - 1, yPos),(xPos - 2, yPos)]
    if turn == 0:
        directions = [up,right,down,left]
    else:
        directions = [up,left,down,right]
    if lastPos == directions[0][1]:
        direction = 0
    elif lastPos == directions[1][1]:
        direction = 1
    elif lastPos == directions[2][1]:
        direction = 2
    elif lastPos == directions[3][1]:
        direction = 3
    else:
        direction = 0
    movement = 0
    for i in range(4):
        if movement == 0:
            direction = (direction + 1) % 4
            if directions[direction][1] == lastPos:
                movement = lastPos
            if directions[direction][0][0] >= 0 and directions[direction][0][0] < imgSize[0] and directions[direction][0][1] >= 0 and directions[direction][0][1] < imgSize[1]:
                if img.getpixel(directions[direction][0]) != wallColor:
                    movement = directions[direction][1]
    
    return(movement)

def labyrinth(size = (100,100), wallColor = (0,0,0), possibleWallColor = (150,0,0), entryColor = (0,150,0), exitColor = (150,0,0), pathColor = (200,200,200)):

    imageX = size[0] * 2 - 1
    imageY = size[1] * 2 - 1
    imageSize = (imageX,imageY)
    labyrinthImage = createImg(imageSize)

    entryPos = (0,0)
    exitPos = (imageX - 1, imageY - 1)

    for x in range(imageX):
        for y in range(imageY):
            labyrinthImage.putpixel((x,y), (254,254,254))

    for x in range(imageX):
        if x % 2 == 1:
            for y in range(imageY):
                if y % 2 == 1:
                    labyrinthImage.putpixel((x,y), wallColor)

    for x in range(imageX):
        for y in range(imageY):
            moduloX = x % 2
            moduloY = y % 2
            if moduloX + moduloY == 1:
                labyrinthImage.putpixel((x,y), possibleWallColor)

    spritePos = copy.copy(entryPos)
    labyrinthImage.putpixel(spritePos, pathColor)
    lastPos = copy.copy(entryPos)
    possibleMovements = countPossibleMovements(labyrinthImage, entryPos, spritePos, imageSize, pathColor, wallColor)
    pathsLeftToCover = size[0] * size[1] - 1
    #lastPlaceWherePathFound = [copy.copy(entryPos),copy.copy(entryPos)]
    diagonal = 0

    while pathsLeftToCover != 0:

        while len(possibleMovements) != 0 and spritePos != exitPos:
            lastPos = copy.copy(spritePos)
            spritePos = random.choice(possibleMovements)
            labyrinthImage.putpixel(spritePos, pathColor)
            pathsLeftToCover -= 1
            if pathsLeftToCover % 100 == 0:
                print(pathsLeftToCover)
            labyrinthImage = addWalls(labyrinthImage, lastPos, spritePos, imageSize, pathColor, wallColor)
            possibleMovements = countPossibleMovements(labyrinthImage, lastPos, spritePos, imageSize, pathColor, wallColor)
        '''
        spritePos = lastPlaceWherePathFound[0]
        lastPos = lastPlaceWherePathFound[1]
        foundNewPathStart = False

        while foundNewPathStart == False:
            possibleMovements = countPossibleMovements(labyrinthImage, lastPos, spritePos, imageSize, pathColor, wallColor)
            if len(possibleMovements) == 0:
                newPath = findNewPath(labyrinthImage, lastPos, spritePos, imageSize, wallColor, random.randrange(2))
                lastPos = copy.copy(spritePos)
                spritePos = copy.copy(newPath)
            else:
                lastPlaceWherePathFound = [copy.copy(spritePos),copy.copy(lastPos)]
                foundNewPathStart = True
            if pathsLeftToCover == 0:
                break
'''
        foundNewPathStart = False
        while foundNewPathStart == False:
            if pathsLeftToCover != 0:
                for i in range(diagonal + 1):
                    x = i*2
                    y = (diagonal - i)*2
                    if x < imageSize[0] and y < imageSize[1]:
                        if labyrinthImage.getpixel((x,y)) == pathColor:
                            if len(countPossibleMovements(labyrinthImage, (x,y), (x,y), imageSize, pathColor, wallColor)) != 0:
                                spritePos = (x,y)
                                lastPos = (x,y)
                                foundNewPathStart = True
                if foundNewPathStart == False:
                    diagonal += 1
            else:
                foundNewPathStart = True
        possibleMovements = countPossibleMovements(labyrinthImage, lastPos, spritePos, imageSize, pathColor, wallColor)
                

        
    for x in range(imageX):
        for y in range(imageY):
            moduloX = x % 2
            moduloY = y % 2
            if moduloX + moduloY == 1:
                if labyrinthImage.getpixel((x,y)) != wallColor:
                    labyrinthImage.putpixel((x,y), pathColor)

    labyrinthImage.putpixel(entryPos, entryColor)
    labyrinthImage.putpixel(exitPos, exitColor)

    display(labyrinthImage)
    saveImg(labyrinthImage, os.getcwd(), '/currentProjects/200_280_b_labyrinth.png')

labyrinth(size = (200,280), pathColor=(255,255,255), entryColor=(255,255,255), exitColor=(255,255,255))