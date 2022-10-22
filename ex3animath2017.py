#factoriel 10 exercice 3 animath 2017

listofdivs = []
checks = 6*5*4*3*2*1
for i in range(1,checks+1):
    
    b = float(checks) % float(i)
    
    if b == 0:
        listofdivs.append(i)

        
    c = i / 100000
    if c.is_integer():
        d = i / checks * 100
        e = int(d) + 1
        msg = '['
        for o in range(0,e):
            msg = msg + '-'
        for o in range(0,100-e):
            msg = msg + ' '
        msg = msg + ']'
        print(msg)


        
print(listofdivs)
print(len(listofdivs))
