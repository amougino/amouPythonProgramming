    #import modules
import socket
from tkinter import *
    #connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
client.send(b"I am CLIENT<br>")
#from_server = client.recv(4096)
#print(from_server)
    #functions
    ##quit server
def disconnect():
    client.close()
    ##start the game
def start(player_number):
        #create window
    HEIGHT = 800
    WIDTH = 1100
    window = Tk()
    window.title('Game')
    c = Canvas(window, height = HEIGHT, width = WIDTH, bg = 'white')
    c.pack()
        #find middle
    midx = WIDTH / 2
    midy = HEIGHT / 2
        #create sprites and move them to center
    id_sprite1 = c.create_oval(0, 0, 50, 50, outline = 'black', fill = 'blue')
    c.move(id_sprite1, midx + 50, midy)
    id_sprite2 = c.create_oval(0, 0, 50, 50, outline = 'black', fill = 'green')
    c.move(id_sprite2, midx - 50, midy)
        #make sprites move
    def move_sprite(event):
            #set speed
        speed = 10
        
            #if you start as player 1, move sprite 1
        if player_number == 1:
            if event.keysym == 'Up':
                c.move(id_sprite1, 0, -speed)
            if event.keysym == 'Down':
                c.move(id_sprite1, 0, speed)
            if event.keysym == 'Left':
                c.move(id_sprite1, -speed, 0)
            if event.keysym == 'Right':
                c.move(id_sprite1, speed, 0)
            coord1 = c.coords(id_sprite1)
            coord1x = (coord1[0] + coord1[2])/2
            coord1y = (coord1[1] + coord1[3])/2
            coord1_tobesent = 'coord1x_'+str(coord1x)+'_coord1y_'+str(coord1y)
            #print(coord1_tobesent)
            client.send(coord1_tobesent.encode('utf-8'))
            if coord1x > 1100.0:
                c.move(id_sprite1, -20, 0)
            if coord1x < 0:
                c.move(id_sprite1, 20, 0)
            if coord1y > 800.0:
                c.move(id_sprite1, 0, -20)
            if coord1y < 0:
                c.move(id_sprite1, 0, 20)
            #if you start as player 2, move sprite 2
        if player_number == 2:
            if event.keysym == 'Up':
                c.move(id_sprite2, 0, -speed)
            if event.keysym == 'Down':
                c.move(id_sprite2, 0, speed)
            if event.keysym == 'Left':
                c.move(id_sprite2, -speed, 0)
            if event.keysym == 'Right':
                c.move(id_sprite2, speed, 0)
            coord2 = c.coords(id_sprite2)
            coord2x = (coord2[0] + coord2[2])/2
            coord2y = (coord2[1] + coord2[3])/2
            coord2_tobesent = 'coord2x_'+str(coord2x)+'_coord2y_'+str(coord2y)
            #print(coord2_tobesent)
            client.send(coord2_tobesent.encode('utf-8'))
            if coord2x > 1100:
                c.move(id_sprite2, -20, 0)
            if coord2x < 0:
                c.move(id_sprite2, 20, 0)
            if coord2y > 800:
                c.move(id_sprite2, 0, -20)
            if coord2y < 0:
                c.move(id_sprite2, 0, 20)
        from_server = client.recv(4096)
        decoding = str(from_server)
        decoding = decoding.split('_')
        if decoding[0] == 1:
            if player_number != 1:
                x = decoding[1]
                y = decoding[2]
                c.move(id_sprite1, x, y)
        if decoding[0] == 2:
            if player_number != 2:
                x = decoding[1]
                y = decoding[2]
                c.move(id_sprite2, x, y)
    c.bind_all('<Key>', move_sprite)
    
    
start(1)

