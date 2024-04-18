import time
times = []
a = input('start')
start = time.time()
while time.time() - start < 30.0:
    a = input(' - ')
    times.append(time.time())
delta = []
for i in range(len(times) - 1):
    delta.append(times[i + 1] - times[i])
tot = 0
for i in delta:
    tot += i
print((tot/len(delta)*(1/60)))