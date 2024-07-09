import PIL.Image as Img
import os
from gravSim2 import *

def getImage(filePath = ''):
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Img.open(file)
        return img
    except FileNotFoundError:
        raise Exception('File does not exist')

def fuse(amount, inputPath, outputPath, size):
    fusedImg = createImg(size)
    column = 0
    for i in range(amount):
        inputImg = getImage(os.path.expanduser(inputPath + f'_v{i+1}.png'))
        for x in range(int(size[0]/amount)):
            for y in range(size[1]):
                fusedImg.putpixel((column,y),inputImg.getpixel((column,y)))
            column += 1
    saveImg(fusedImg,outputPath, '')

