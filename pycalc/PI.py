a = 0
idx = 1
for i in range(10000):
  a += ( 1 / ((i * 2) + 1) ) * idx
  idx *= -1
  if i % 10000 == 0:
    print(i / 10000)

print(4*a)