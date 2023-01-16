import random
numberList = []
myList = []
numberStr = ''
for i in range(0,8):
    numberList.append(str(random.randrange(0,100)))
for i in range(0,100):
    myList.append(str(i))
for i in range(0,100):
    a = random.choice(myList)
    myList.pop(myList.index(a))
    numberList.append(a)
for i in numberList:
    if len(i) == 1:
        numberList[numberList.index(i)] = '0' + i
for i in numberList:
    numberStr = numberStr + i
print('Output (between brackets) - [' + numberStr + ']')