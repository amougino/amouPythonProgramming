import PIL.Image as img
import os

def createImg(size):
    createdImage = img.new('RGB', size, 'white')
    return(createdImage)

def saveImage(imageToSave, path):
    file = os.path.expanduser(path)
    imageToSave.save(file)

PiMoImage = createImg((10,10))
blackPixels = [(3,0),(2,3),(1,1),(0,2)]
for pixel in blackPixels:
    PiMoImage.putpixel(pixel,(0,0,0))
PiMoImage.putpixel((2,0),(255,0,0))

saveImage(PiMoImage,os.getcwd()+'/PiMo/PiMoImage2.png')