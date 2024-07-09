import math
import time

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

import PIL.Image as Img
import os

'''
UNITS
    time    tic
    length  unit
    mass    kg

    F = ma

    F -> N
    m -> kg
    a -> unit / tic^2

    a = F/m
    F = G * m1 * m2 / d^2
'''

maxDistance = 2000
size = 300
G = 20

class Vector:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return(f'Vector({self.x}, {self.y}, {self.z})')
    
    def __str__(self):
        return(f'{self.x}i + {self.y}j + {self.z}k')
    
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError('There are only three elements in the vector')

    def __add__(self, other):
        return(Vector(self.x + other.x, self.y + other.y, self.z + other.z))
        
    def __sub__(self, other):
        return(Vector(self.x - other.x, self.y - other.y, self.z - other.z))
        
    def __mul__(self, other):
        if isinstance(other, Vector):
            return((self.x*other.x + self.y*other.y + self.z*other.z))
        elif isinstance(other, (int, float)):
            return(Vector(self.x*other, self.y*other, self.z*other))
        else:
            raise(TypeError('operand must be Vector, int, or float'))
            
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return(Vector(self.x/other, self.y/other, self.z/other))
        else:
            raise(TypeError('operand must be int or float'))
            
    def mag(self):
        return(math.sqrt(self.x**2 + self.y**2 + self.z**2))
    
    def normalize(self):
        magnitude = self.mag()
        return(Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        ))

class System:
    
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def calc_interactions(self):
        for body1 in self.bodies:
            for body2 in self.bodies:
                if body1 != body2:
                    body2.calc_acc(body1)

    def update_all(self):
        for body in self.bodies:
            body.move()

    def __str__(self):
        returnString = 'Bodies :'
        for body in self.bodies:
            returnString += '\n' + str(body)
        return(returnString)
    
    def tot_distance(self):
        distance = 0
        for body1 in range(len(self.bodies)):
            for body2 in range(len(self.bodies)):
                if body2 > body1:
                    distance += (Vector(*self.bodies[body1].pos) - Vector(*self.bodies[body2].pos)).mag()
        return(distance)
                    

class Body:
    
    def __init__(self, sys, pos, vel, mass):
        self.sys = sys
        self.pos = pos
        self.vel = Vector(*vel)
        self.mass = mass
        self.sys.add_body(self)

    def move(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1], self.pos[2] + self.vel[2])

    def calc_acc(self, other):
        posDiff = Vector(*other.pos) - Vector(*self.pos)
        distance = posDiff.mag()
        attraction = G * self.mass * other.mass / (distance**2)
        attractionVector = posDiff.normalize() * attraction
        acc = attractionVector / self.mass
        self.vel += acc

    def __str__(self):
        return(f'Pos : {self.pos}, Vel : {self.vel}, Mass : {self.mass}')

precision = 2048
startPos = 20

'''
theta1 = i * 2*math.pi/precision
theta2 = j * 2*math.pi/precision
tripleBody = System()
alpha = Body(tripleBody, (startPos,0,0), (math.sin(theta1),math.cos(theta1),0), 1)
beta = Body(tripleBody, (0,0,0), (math.sin(theta2),math.cos(theta2),0), 1)
gamma = Body(tripleBody, (-startPos,0,0), (-math.sin(theta1)-math.sin(theta2),-math.cos(theta1)-math.cos(theta2),0), 1)

data = [[],[],[]]
for i in range(3):
    data[i].append([alpha.pos[i], beta.pos[i], gamma.pos[i]])
iterations = 0
while tripleBody.tot_distance() < maxDistance:
    iterations += 1
    tripleBody.calc_interactions()
    tripleBody.update_all()
    for i in range(3):
        data[i].append([alpha.pos[i], beta.pos[i], gamma.pos[i]])
    #print(tripleBody.tot_distance())
#print(data)
print(iterations)



fig, ax = plt.subplots()

scat = ax.scatter(data[0][0], data[1][0], c="b")
ax.set(xlim=[-size, size], ylim=[-size, size])

def update(frame):
    x = data[0][frame]
    y = data[1][frame]
    data1 = np.stack([x, y]).T
    scat.set_offsets(data1)
    return(scat)


ani = animation.FuncAnimation(fig=fig, func=update, frames=iterations, interval=10)
plt.show()

'''
def createImg(size):
    img = Img.new('RGB', size)
    return(img)

def saveImg(img, path, name):
    file = os.path.expanduser(path + name)
    img.save(file)
'''
img1 = createImg((precision,precision))

for i in range(precision):
    for j in range(precision):

        theta1 = i * 2*math.pi/precision
        theta2 = j * 2*math.pi/precision
        sin1 = math.sin(theta1)
        cos1 = math.cos(theta1)
        sin2 = math.sin(theta2)
        cos2 = math.cos(theta2)

        tripleBody = System()
        alpha = Body(tripleBody, (startPos,0,0), (sin1,cos1,0), 1)
        beta = Body(tripleBody, (0,0,0), (sin2,cos2,0), 1)
        gamma = Body(tripleBody, (-startPos,0,0), (-sin1-sin2,-cos1-cos2,0), 1)

        iterations = 0
        while tripleBody.tot_distance() < maxDistance:
            iterations += 1
            tripleBody.calc_interactions()
            tripleBody.update_all()
        
        c = int(iterations / 10)
        if c < 256:
            r = c
            g = 0
            b = 0
        elif c < 256*2:
            r = 255
            g = c - 256
            b = 0
        elif c < 256*3:
            r = 256*3 - c
            g = 255
            b = 0
        elif c < 256*4:
            r = 0
            g = 255
            b = c - 256*3
        elif c < 256*5:
            r = 0
            g = 256*5 - c
            b = 255
        elif c < 256*6:
            r = c - 256*5
            g = 0
            b = 255
        else:
            r = 255
            g = 255
            b = 255
        img1.putpixel((i,j),(r,g,b))
    print(i)

img1.show()

path = os.getcwd()
saveImg(img1, path, f'/imgsY/p{precision}_max{maxDistance}_G{G}_start{startPos}.png')
#'''