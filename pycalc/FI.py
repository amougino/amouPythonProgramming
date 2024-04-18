def fi(a,b,c):
  l = [a,b]
  for i in range(c):
    l.append(l[-1] + l[-2])
  print(l)