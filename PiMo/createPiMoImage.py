import PIL.Image as img
import os

def createImg(size):
    createdImage = img.new('RGB', size, 'white')
    return(createdImage)

def saveImage(imageToSave, path):
    file = os.path.expanduser(path)
    imageToSave.save(file)

PiMoImage = createImg((100,100))
orange_pixels = [(0,0),(7,0),(22,0)]
for pixel in orange_pixels:
    PiMoImage.putpixel(pixel,(255,128,0))
PiMoImage.putpixel((1,0),(0,0,33))
PiMoImage.putpixel((8,0),(0,0,23))
PiMoImage.putpixel((9,0),(0,0,255))
pink_pixels = [(2,0),(3,0),(4,0),(15,0)]
for pixel in pink_pixels:
    PiMoImage.putpixel(pixel,(255,0,128))
#PiMoImage.putpixel((5,0),(0,0,255))
#PiMoImage.putpixel((16,0),(0,255,128))
PiMoImage.putpixel((5,0),(0,0,255))
PiMoImage.putpixel((18,0),(0,128,255))
PiMoImage.putpixel((19,0),(40,60,13))
PiMoImage.putpixel((20,0),(128,0,255))
PiMoImage.putpixel((23,0),(0,1,10))
PiMoImage.putpixel((25,0),(0,128,0))



PiMoImage.putpixel((80,0),(255,0,0))



saveImage(PiMoImage,os.getcwd()+'/PiMo/PiMoImage8.png')