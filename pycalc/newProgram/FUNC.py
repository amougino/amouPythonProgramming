def translate(text, start, finish):
    baseVal = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    num10 = 0
    for idx,i in enumerate([j for j in text]):
       num10 += int(i)*(start**(len(text) - idx - 1))
    a = 1
    b = 0
    while a < num10:
        a *= finish
        b += 1
    translated = ''
    while a >= 1:
        translated += baseVal[int(num10//a)]
        num10 = num10%a
        a /= finish
    if translated[0] == '0':
        translated = translated[1:]
    return(translated)

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

def fi(a,b,c):
  l = [a,b]
  for i in range(c):
    l.append(l[-1] + l[-2])
  print(l)