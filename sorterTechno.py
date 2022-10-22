import random as r

# The greater the first number, the larger the object is
# Plus le premier nombre est grand, plus l'objet est grand
# The second number (either 1 or 0) is if the object is upright or not. 1 = upright ; 0 = not upright
# The second nombre (sois 1 ou 0) dit si l'objet est à l'endroit ou pas. 1 = à l'endroit ; 0 = à l'envers

listParts = [['1'],['2'],['3'],['4'],['5'],['6']]
listToSort = []
listFlipTemp = []

def genRandom(listGen,parts):
    for i in range(len(parts)):
        obj = r.choice(parts)
        listGen.append(obj)
        parts.pop(parts.index(obj))
        listGen[-1].append(str(r.randrange(2)))
    return(listGen)

def flipListPart(listToFlip,idx,flipList):
    flipList = []
    done = 0
    while done == 0:
        lenList = len(listToFlip)
        if not idx == lenList:
            if listToFlip[idx][1] == '0':
                listToFlip[idx][1] = '1'
            else:
                listToFlip[idx][1] = '0'
            flipList.append(listToFlip[idx])
            listToFlip.pop(idx)
        else:
            done = 1
    done = 0
    while done == 0:
        if not len(flipList) == 0:
            listToFlip.append(flipList[-1])
            flipList.pop(-1)
        else:
            done = 1
    return(listToFlip)

def sortList(sortList):
    lenList = len(sortList)
    for i in range(lenList):
        toSort = str(lenList - i)
        try:
            idxToSort = sortList.index([toSort,'0'])
        except(ValueError):
            idxToSort = sortList.index([toSort,'1'])
        sortList = flipListPart(sortList,idxToSort,listFlipTemp)
        print('Step 1 for obj size',toSort,'=',sortList)
        if sortList[-1][1] == '1':
            sortList = flipListPart(sortList,lenList - 1,listFlipTemp)
        print('Step 2 for obj size',toSort,'=',sortList)
        sortList = flipListPart(sortList,lenList - int(toSort),listFlipTemp)
        print('Step 3 for obj size',toSort,'=',sortList)
    return(sortList)

listToSort = genRandom(listToSort,listParts)

listToSort = sortList(listToSort)
print('Result =',listToSort)