import PIL.Image as img
import os

def createImg(size):
    createdImage = img.new('RGB', size, 'white')
    return(createdImage)

def saveImage(imageToSave, path):
    file = os.path.expanduser(path)
    imageToSave.save(file)

PiMoImage = createImg((100,100))
orange_pixels = [(0,0),(7,0)]
for pixel in orange_pixels:
    PiMoImage.putpixel(pixel,(255,128,0))
PiMoImage.putpixel((1,0),(255,255,222))
PiMoImage.putpixel((8,0),(255,255,23))
pink_pixels = [(2,0),(3,0),(4,0)]
for pixel in pink_pixels:
    PiMoImage.putpixel(pixel,(255,0,128))
#PiMoImage.putpixel((5,0),(0,0,255))
PiMoImage.putpixel((16,0),(0,255,128))


saveImage(PiMoImage,os.getcwd()+'/PiMo/PiMoImage7.png')