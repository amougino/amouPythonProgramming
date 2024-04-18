def reseau(x,y):
  n1 = -x + y + 0.5
  n2 = x - y + 0.5
  if n1 < 0:
    xprime = 0
  else:
    xprime = 1
  if n2 < 0:
    yprime = 0
  else:
    yprime = 1
  if xprime + yprime - 2 < 0:
    return(0)
  else:
    return(1)