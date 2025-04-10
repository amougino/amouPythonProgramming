import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random

settings1 = {
    "canvas_size" : 50,
    "alive_pixels" : [],
    "iterations" : 200,
    "speed_in_ms" : 150,
    "number_of_random_squares" : 1000
}

print('Creating random squares...')
for i in range(settings1["number_of_random_squares"]):
    settings1["alive_pixels"].append((random.randrange(100),random.randrange(100)))

class GameOfLife:

    def __init__(self,settings):
        self.canvas_size = settings["canvas_size"]
        self.alive_pixels = settings["alive_pixels"]
        self.iterations = settings["iterations"]
        self.speed_in_ms = settings["speed_in_ms"]
        self.saves = []
        self.pixels_around = []
        for x in range(-1,2):
            for y in range(-1,2):
                if not (x == 0 and y == 0):
                    self.pixels_around.append((x,y))

    def find_pixels_to_check(self):
        self.pixels_to_check = []
        for pixel in self.alive_pixels:
            for x in range(-1,2):
                for y in range(-1,2):
                    pixel_to_add = ((pixel[0] + x)%self.canvas_size,(pixel[1] + y)%self.canvas_size)
                    if not pixel_to_add in self.pixels_to_check:
                        self.pixels_to_check.append(pixel_to_add)

    def update_pixels(self):
        new_alive_pixels = []
        for pixel in self.pixels_to_check:
            alive_around_count = 0
            for coord in self.pixels_around:
                if ((pixel[0] + coord[0])%self.canvas_size,(pixel[1] + coord[1])%self.canvas_size) in self.alive_pixels:
                    alive_around_count += 1
            if pixel in self.alive_pixels:
                if alive_around_count > 1 and alive_around_count < 4:
                    new_alive_pixels.append(pixel)
            else:
                if alive_around_count == 3:
                    new_alive_pixels.append(pixel)
        self.alive_pixels = new_alive_pixels

    def save_iteration(self):
        self.saves.append(self.alive_pixels)

    def calculate_iterations(self):
        self.save_iteration()
        last_percent_said = 0
        for iteration in range(self.iterations):
            if iteration/self.iterations > last_percent_said:
                print(int(last_percent_said*100),'%')
                last_percent_said += 0.1
            self.find_pixels_to_check()
            self.update_pixels()
            self.save_iteration()
        print(100,'%')

print('Creating game...')
game = GameOfLife(settings1)
print('Calculating iterations...')
game.calculate_iterations()

fig = plt.figure()

def animate(i):
    plt.cla()
    pixel_size = 1/game.canvas_size
    for pixel in game.saves[i]:
        x = pixel[0]
        y = pixel[1]
        plt.fill([x*pixel_size,(x+1)*pixel_size,(x+1)*pixel_size,x*pixel_size], [y*pixel_size,y*pixel_size,(y+1)*pixel_size,(y+1)*pixel_size], "black") 
    plt.axis([0, 1, 0, 1])

ani = animation.FuncAnimation(fig, animate, interval=game.speed_in_ms, frames = game.iterations)
plt.show()