searchTill = int(input('search till - '))
squareList = []
for i in range(searchTill):
    squareList.append(i**2)
numList = []
for i in squareList:
    for j in squareList:
        for k in squareList:
            for l in squareList:
                num = i + j + k + l
                myList = [num,i,j,k,l]
                notIn = False
                for m in numList:
                    if m[0] == num:
                        notIn = True
                    if notIn == True:
                        break
                if notIn == False:
                    numList.append(myList)
lol = []
for i in range(numList[-1][0]):
    if i < (searchTill**2):
        notIn = False
        for j in numList:
            if j[0] == i:
                notIn = True
        if notIn == False:
            print(str(i) + ' oh no')
        else:
            lol.append(i)
print(squareList)
print(lol)
print(numList)