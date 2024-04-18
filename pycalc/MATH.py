def seuil():
  u=120000
  n=0
  while u<400000:
    n+=1
    u=1.02*u
  return(n)