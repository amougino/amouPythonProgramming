from PIL import Image as Img
import os
import random

imgPath = os.path.expanduser("~/Desktop/insta/moon1.png")
newX = 10000
newY = 6000

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

def getImg(path):
    file = os.path.expanduser(path)
    img = Img.open(file)
    return(img)
   
def saveImg(img, path):
    file = os.path.expanduser(path)
    print(file)
    img.save(file)

def display(img):
    img.show()

image_to_expand = getImg(imgPath)
print(image_to_expand.size)
background = [(0,2,5),(2,5,10)]
new = createImg((newX, newY))

limitXMin = (newX - image_to_expand.size[0])/2 - 1
limitXMax = limitXMin + image_to_expand.size[0]
limitYMin = (newY - image_to_expand.size[1])/2 - 1
limitYMax = limitYMin + image_to_expand.size[1]

def rand_color(choice):
    return((random.randrange(choice[0][0],choice[1][0]),random.randrange(choice[0][1],choice[1][1]),random.randrange(choice[0][2],choice[1][2])))

#try:
for x in range(newX):
    a = x
    for y in range(newY):
        b = y
        if x <= limitXMin:
            new.putpixel((x,y), rand_color(background))
        elif x >= limitXMax:
            new.putpixel((x,y), rand_color(background))
        else:
            if y <= limitYMin:
                new.putpixel((x,y), rand_color(background))
            elif y >= limitYMax:
                new.putpixel((x,y), rand_color(background))
            else:
                pixel = image_to_expand.getpixel((x-int(limitXMin),y-int(limitYMin)-1))
                if pixel[0] + pixel[1] + pixel[2] < 50:
                    new.putpixel((x,y), rand_color(background))
                else:
                    new.putpixel((x,y), pixel)
#except IndexError:
#    print(str(a), str(b))
display(new)

saveImg(new, "~/Desktop/wallpaper3.png")
#'''

