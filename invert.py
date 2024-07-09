import PIL.Image as Img
import os

def saveImg(img, path):
    file = os.path.expanduser(path)
    img.save(file)

def getImage(filePath = ''):
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Img.open(file)
        return img
    except FileNotFoundError:
        raise Exception('File does not exist')
    
def invert(path):
    imgToInvert = getImage(path)
    imgSize = imgToInvert.size
    for x in range(imgSize[0]):
        for y in range(imgSize[1]):
            color = imgToInvert.getpixel((x,y))
            #if color == (0,0,0):
            #    newColor = (255,255,255)
            #elif color == (255,255,255):
            #    newColor = (0,0,0)
            #elif color[0] != 0 and color[1] == 0 and color[2] == 0:
            #    newColor = (255 - color[0],255 - color[0],255)
            #elif color[0] != 0 and color[1] == 0 and color[2] == 255:
            #    newColor = (255 - color[0],0,0)
            #else:
            newColor = (color[1],color[2],color[0])
            imgToInvert.putpixel((x,y),newColor)
        if x%100 == 0:
            print(x)
    saveImg(imgToInvert,path.split('.png')[0]+'_inverted4.png')
            
            
            
'''elif color[0] == 255 and color[1] != 0 and color[2] == 0:
    newColor = (0,color[1],255)
elif color[0] != 0 and color[1] == 255 and color[2] == 0:
    newColor = (0,255,color[0])
elif color[0] == 0 and color[1] == 255 and color[2] != 0:
    newColor = (color[2],255,0)
elif color[0] == 0 and color[1] != 0 and color[2] == 255:
    newColor = (255,color[1],0)
elif color[0] == '''


invert('/Users/amou/Desktop/Python/imgsY/p4098_max2000_G20_start20_final.png')