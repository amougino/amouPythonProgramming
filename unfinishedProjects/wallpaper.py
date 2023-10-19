from PIL import Image as Img
import os

imgPath = os.path.expanduser("~/Desktop")
newX = 10000
newY = 6000

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

def getImg(path):
    file = os.path.expanduser(path)
    img = Img.open(file)
    return(img)
   
def saveImg(img, path, name):
    file = os.path.expanduser(path + name)
    print(file)
    img.save(file)

def display(img):
    img.show()

enceladus = getImg(imgPath)

new = createImg((newX, newY))

limitXMin = (newX - enceladus.size[0])/2 - 1
limitXMax = limitXMin + enceladus.size[0]
limitYMin = (newY - enceladus.size[1])/2 - 1
limitYMax = limitYMin + enceladus.size[1]

try:
    for x in range(newX):
        a = x
        for y in range(newY):
            b = y
            if x <= limitXMin:
                new.putpixel((x,y), (0,0,0))
            elif x >= limitXMax:
                new.putpixel((x,y), (0,0,0))
            else:
                if y <= limitYMin:
                    new.putpixel((x,y), (0,0,0))
                elif y >= limitYMax:
                    new.putpixel((x,y), (0,0,0))
                else:
                    new.putpixel((newX - x,newY -y), enceladus.getpixel((x-int(limitXMin),y-int(limitYMin)-1)))
except IndexError:
    print(str(a), str(b))
display(new)

saveImg(new, os.getcwd(), "wallpaperenceladus3.png")