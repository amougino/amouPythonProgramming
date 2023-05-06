from tkinter import *
Height1 = 1000
Width1 = 1600
window = Tk()
window.title('Space Rocket')
c = Canvas(window, height = Height1, width = Width1, bg ='black')
c.pack()
id_rocket1 = c.create_polygon(5, 5, 5, 25, 30, 15, fill = 'blue')
id_rocket2 = c.create_oval(-10, -10, 40, 40, fill = 'darkgrey')
x_mid = Width1 / 2
y_mid = Height1 / 2
c.move(id_rocket1, x_mid, y_mid)
c.move(id_rocket2, x_mid, y_mid)
c.tag_lower(id_rocket2)
speed = 20
def move_rocket(event):
    if event.keysym == 'Up':
        c.move(id_rocket1, 0, -speed)
        c.move(id_rocket2, 0, -speed)
    elif event.keysym == 'Down':
        c.move(id_rocket1, 0, speed)
        c.move(id_rocket2, 0, speed)
    elif event.keysym == 'Left':
        c.move(id_rocket1, -speed, 0)
        c.move(id_rocket2, -speed, 0)
    elif event.keysym == 'Right':
        c.move(id_rocket1, speed, 0)
        c.move(id_rocket2, speed, 0)
c.bind_all('<Key>', move_rocket)
print(id_rocket1)
print(id_rocket2)
