from PIL import Image as Img
import os
import time

folderPath = os.getcwd()

chars = []

#img

def getImg(path = '', name = ''):
    filePath = path + '/_/' + name
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Img.open(file)
        return(img)
    except FileNotFoundError:
        raise Exception('File does not exist')
    
def saveImg(img, path, name):
    file = os.path.expanduser(path + '/_/' + name)
    img.save(file)

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

#bits

def numToBits(num):
    foo = ''
    for i in range(8):
        if num >= 2**(7-i):
            num -= 2**(7-i)
            foo += '1'
        else:
            foo += '0'
    return(foo)

def bitsToNum(bits):
    pass

#codeConversion

def bitsToImg(bits):
    pass

def imgToBits(img):
    foo = []
    size = img.size
    for x in range(size[0]):
        for y in range(size[1]):
            pxl = img.getpixel((x,y))
            #foo.append([numToBits(pxl[0]), numToBits(pxl[1]), numToBits(pxl[2])])
            print([numToBits(pxl[0]), numToBits(pxl[1]), numToBits(pxl[2])])
    return(foo)

new = getImg(folderPath, 'image4.png')
imgToBits(new)

#to do: change variable names (foo), remove all "pass"