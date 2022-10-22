

myList = ['0','1','6','8','9']
flipList = ['0','1','9','8','6']
for i in myList:
    for j in myList:
        num = (int(i)*10)+int(j)
        newNum = ''
        for k in str(num):
            idx = flipList.index(k)
            newNum += myList[idx]
        print(num,newNum[::-1],str(int(newNum[::-1]) - int(num)))

