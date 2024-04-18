def facPrem(num):
  fac = 2
  facPrems = []
  while num != 1:
    notDiv = False
    while notDiv == False:
      if num % fac == 0:
        facPrems.append(fac)
        print(fac)
        num = num / fac
      else:
        notDiv = True
    fac += 1
  return(facPrems)
number = int(input("Num - "))
print(facPrem(number))