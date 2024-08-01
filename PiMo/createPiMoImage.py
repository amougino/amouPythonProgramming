import PIL.Image as img
import os

def createImg(size):
    createdImage = img.new('RGB', size, 'white')
    return(createdImage)

def saveImage(imageToSave, path):
    file = os.path.expanduser(path)
    imageToSave.save(file)

PiMoImage = createImg((10,10))
blackPixels = [(3,0),(2,3),(1,1),(0,2),(5,2),(3,3),(4,4),(0,3),(3,7),(1,6),(2,5),(8,6),(7,8),(3,7),(6,5)]
for pixel in blackPixels:
    PiMoImage.putpixel(pixel,(0,0,0))
PiMoImage.putpixel((5,8),(255,0,0))

saveImage(PiMoImage,os.getcwd()+'/PiMo/PiMoImage3.png')