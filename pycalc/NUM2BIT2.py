num = int(input("Num - "))
bit = []
while num != 1:
  bit.append(num % 2)
  num = num // 2
bit.append(num)
temp = []
while bit != []:
  temp.append(bit[-1])
  bit.pop(-1)
bit = temp
print(bit)