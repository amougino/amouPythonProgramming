import time
import random

def reverseNumberMemory(numSize, delay = 1):
    numbers = []
    for i in range(numSize):
        numbers.append(random.randrange(0,10))
    for idx, i in enumerate(numbers):
        print(str(i) + '  [' + ('*' * (idx + 1)) + (' ' * (numSize - idx - 1)) + ']', end = '\r')
        time.sleep(delay)
    answer = input('Number list backwards : ')
    reverse = []
    for i in range(len(numbers)):
        reverse.append(numbers[-1])
        numbers.pop(-1)
    listAnswer = [char for char in answer]
    for i in range(len(listAnswer)):
        listAnswer[i] = int(listAnswer[i])
    if listAnswer == reverse:
        print('Correct!')
        print(reverse)
        return(True)
    else:
        print('Wrong!')
        print(reverse)
        return(False)
time.sleep(1)
a = True
num = 1
while a == True:
    a = reverseNumberMemory(num)
    num += 1
    time.sleep(1)