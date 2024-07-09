import time

starttime = time.time()
for x in range(0,10):
    a = 0
    for i in range(1000000*x,1000000*(x+1)):
        a += i/200000
    print(a)
print('That took {} seconds'.format(time.time() - starttime))