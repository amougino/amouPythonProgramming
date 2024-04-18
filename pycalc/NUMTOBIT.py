num = int(input("Num - "))
bit = []
a = 1
while a <= num:
  a = a * 2
a = a / 2
while a >= 1:
  if num >= a:
    num -= a
    bit.append(1)
  else:
    bit.append(0)
  a = a / 2
print(bit)