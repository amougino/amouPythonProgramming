hexa = "0 1 2 3 4 5 6 7 8 9 a b c d e f".split(" ")
bi = "0 1".split(" ")
b10 = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15".split(" ")
while True:
  num = input("Num xNum or bNum - ")
  if num[0] == "x":
    num = num.split("x")[1]
    res = 0
    for i in range(len(num)):
      res += int(b10[int(hexa.index(num[i]))])*(16**(len(num)-i-1))
    print("b10 " + str(res))
  
  elif num[0] == "b":
    num = num.split("b")[1]
    res = 0
    for i in range(len(num)):
      res += int(b10[int(bi.index(num[i]))])*(2**(len(num)-i-1))
    print("b10 " + str(res))
  
  else:
    num1 = int(num)
    res = ""
    a = 1
    while num1 >= a:
      a = a * 2
    a = a / 2
    while a >= 1:
      res += bi[b10.index(str(int(num1//a)))]
      num1 = num1 % a
      a = a / 2
    print("bi " + str(res))
  
    num2 = int(num)
    res = ""
    a = 1
    while num2 >= a:
      a = a * 16
    a = a / 16
    while a >= 1:
      res += hexa[b10.index(str(int(num2//a)))]
      num2 = num2 % a
      a = a / 16
    print("hexa " + str(res))