import numpy as np
from peristrofi import *
'''
def ln(n,prec):
    a = 0
    for i in range(prec):
        c = 2*i + 1
        a += (1 / c)*(((n-1)/(n+1))**c)
    return(2*a)

a = 2
print(ln(a,100))
print("0.693147180559945309417")
print(np.log(a))
'''


def adder(a, b):
    # print('+',a,b)
    if len(a) > len(b):
        b = [0 for i in range(len(a) - len(b))] + b
    else:
        a = [0 for i in range(len(b) - len(a))] + a
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    for i in range(1, len(c)):
        idx = len(c) - i
        c[idx - 1] += c[idx] // 10
        c[idx] %= 10
    while c[0] // 10 != 0:
        c.insert(0, c[0] // 10)
        c[1] %= 10
    while c[0] == 0 and len(c) > 1:
        c.pop(0)
    # print('add result',c)
    return (c)


def subber(a, b):
    # print('-',a,b)
    if len(a) > len(b):
        b = [0 for i in range(len(a) - len(b))] + b
    else:
        a = [0 for i in range(len(b) - len(a))] + a
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])
    for i in range(1, len(c)):
        idx = len(c) - i
        c[idx - 1] += c[idx] // 10
        c[idx] %= 10
    while c[0] // 10 != 0:
        c.insert(0, c[0] // 10)
        c[1] %= 10
    while c[0] == 0 and len(c) > 1:
        c.pop(0)
    # print('sub result',c)
    return (c)


def karatsuba(a, b):
    a_copy = a.copy()
    b_copy = b.copy()

    if len(a_copy) == 1:
        for i in range(len(b_copy)):
            b_copy[i] = a_copy[0]*b_copy[i]
        for i in range(1, len(b_copy)):
            idx = len(b_copy) - i
            b_copy[idx - 1] += b_copy[idx] // 10
            b_copy[idx] %= 10
        while b_copy[0] // 10 != 0:
            b_copy.insert(0, b_copy[0] // 10)
            b_copy[1] %= 10
        # print('k result',b_copy)
        return (b_copy)

    elif len(b_copy) == 1:
        for i in range(len(a_copy)):
            a_copy[i] = b_copy[0]*a_copy[i]
        for i in range(1, len(a_copy)):
            idx = len(a_copy) - i
            a_copy[idx - 1] += a_copy[idx] // 10
            a_copy[idx] %= 10
        while b[0] // 10 != 0:
            a_copy.insert(0, a_copy[0] // 10)
            a_copy[1] %= 10
        # print('k result',a_copy)
        return (a_copy)

    if len(a) != len(b):
        if len(a) > len(b):
            b = [0 for i in range(len(a)-len(b))] + b
        else:
            a = [0 for i in range(len(b)-len(a))] + a

    length = len(a)
    half = int(length/2)
    high_a = a[:half]
    low_a = a[half:]
    high_b = b[:half]
    low_b = b[half:]

    z0 = karatsuba(low_a, low_b)  # ac
    z1 = karatsuba(adder(high_a, low_a), adder(high_b, low_b))  # (a+b)(c+d)
    z2 = karatsuba(high_a, high_b)  # bd
    # print('all',a,b,z0,z1,z2,half)
    final = adder(z2 + [0 for i in range((length - half) * 2)],
                  adder(subber(subber(z1, z2), z0) + [0 for i in range(length - half)], z0))
    # print('---- k result',final)
    return (final)


toto1 = [3, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 4, 5, 6]
toto2 = [1, 2, 1, 4, 5, 6, 7, 2]
print(karatsuba(toto1, toto2))
print([int(i) for i in "392860006663715946432"])
