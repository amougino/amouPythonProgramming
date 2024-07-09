import numpy as np
import sympy as smp
from scipy.integrate import odeint
#import matplotlib.pyplot as plt

import PIL.Image as Img
import os

t,g = smp.symbols('t g')
m1,m2 = smp.symbols('m1 m2')
L1,L2 = smp.symbols('L1 L2')

the1,the2 = smp.symbols(r'\theta_1, \theta_2', cls=smp.Function)
the1 = the1(t)
the2 = the2(t)
the1_d = smp.diff(the1, t)
the2_d = smp.diff(the2, t)
the1_dd = smp.diff(the1_d, t)
the2_dd = smp.diff(the2_d, t)

x1 = L1*smp.sin(the1)
y1 = -L1*smp.cos(the1)
x2 = L1*smp.sin(the1)+L2*smp.sin(the2)
y2 = -L1*smp.cos(the1)-L2*smp.cos(the2)
#kinetic
T1 = 1/2*m1*(smp.diff(x1,t)**2 + smp.diff(y1,t)**2)
T2 = 1/2*m2*(smp.diff(x2,t)**2 + smp.diff(y2,t)**2)
T = T1 + T2
#potential
V1 = m1*g*y1
V2 = m2*g*y2
V = V1 + V2

L = T - V

LE1 = smp.diff(L,the1) - smp.diff(smp.diff(L, the1_d), t).simplify()
LE2 = smp.diff(L,the2) - smp.diff(smp.diff(L, the2_d), t).simplify()

sols = smp.solve([LE1, LE2], (the1_dd, the2_dd), simplify = False, rational = False)

dz1dt_f = smp.lambdify((t,g,m1,m2,L1,L2,the1,the2,the1_d,the2_d), sols[the1_dd])
dz2dt_f = smp.lambdify((t,g,m1,m2,L1,L2,the1,the2,the1_d,the2_d), sols[the2_dd])
dthe1dt_f = smp.lambdify(the1_d, the1_d)
dthe2dt_f = smp.lambdify(the2_d, the2_d)

def dSdt(S, t, g, m1, m2, L1, L2):
    the1, z1, the2, z2 = S
    return [
        dthe1dt_f(z1),
        dz1dt_f(t, g, m1, m2, L1, L2, the1, the2, z1, z2),
        dthe2dt_f(z2),
        dz2dt_f(t, g, m1, m2, L1, L2, the1, the2, z1, z2),
    ]

def getImage(filePath = ''):
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Img.open(file)
        return img
    except FileNotFoundError:
        raise Exception('File does not exist')
    
def createImg(size):
    img = Img.new('RGB', size)
    return(img)

def saveImage(img, path):
    file = os.path.expanduser(path)
    img.save(file)

t = np.linspace(0, 40, 1001)
g = 9.81
m1=2
m2=1
L1 = 2
L2 = 1

precision1 = 720
precision2 = 720

img1 = createImg((precision1,precision2))

for ang1 in range(precision1):
    for ang2 in range(precision2):
        img1.putpixel((ang1,ang2), )