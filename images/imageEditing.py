from PIL import Image
import os

def getImage(filePath = ''):
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Image.open(file)
        return img
    except FileNotFoundError:
        raise Exception('File does not exist')

def saveImage(img, path):
    file = os.path.expanduser(path)
    img.save(file)

def getImageInfo(img):
    size = img.size
    fileType = img.format
    return size, fileType

def display(img):
    img.show()

def filter(img, size, addFilter = [0, 0, 0], multFilter = [1, 1, 1]):
    for x in range(size[0]):
        for y in range(size[1]):
            pxl = img.getpixel((x,y))
            r = (pxl[0] + addFilter[0]) * multFilter[0]
            g = (pxl[1] + addFilter[1]) * multFilter[1]
            b = (pxl[2] + addFilter[2]) * multFilter[2]
            if r > 255:
                r = 255
            elif r < 0:
                r = 0
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            if b > 255:
                b = 255
            elif b < 0:
                b = 0
            img.putpixel((x,y), (int(r), int(g), int(b)))
    return img

def switchColors(img, size, switch = ['r', 'g', 'b']):
    for x in range(size[0]):
        for y in range(size[1]):
            pxl = img.getpixel((x,y))
            if switch[0] == 'r':
                newR = pxl[0]
            elif switch[0] == 'g':
                newR = pxl[1]
            elif switch[0] == 'b':
                newR = pxl[2]
            if switch[1] == 'r':
                newG = pxl[0]
            elif switch[1] == 'g':
                newG = pxl[1]
            elif switch[1] == 'b':
                newG = pxl[2]
            if switch[2] == 'r':
                newB = pxl[0]
            elif switch[2] == 'g':
                newB = pxl[1]
            elif switch[2] == 'b':
                newB = pxl[2]
            img.putpixel((x,y), (newR, newG, newB))
    return img

def contrast(img, size, val, offset = 0):
    if offset == 0:
        for x in range(size[0]):
            for y in range(size[1]):
                pxl = img.getpixel((x,y))
                mil = (pxl[0] + pxl[1] + pxl[2])/3
                dif = mil - val
                r = pxl[0] + dif
                g = pxl[1] + dif
                b = pxl[2] + dif
                if r > 255:
                    r = 255
                elif r < 0:
                    r = 0
                if g > 255:
                    g = 255
                elif g < 0:
                    g = 0
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                img.putpixel((x,y), (int(r), int(g), int(b)))
        return img
    else:
        for x in range(size[0]):
            for y in range(size[1]):
                pxl = img.getpixel((x,y))
                mil = (pxl[0] + pxl[1] + pxl[2])/3
                if mil > val:
                    r = pxl[0] + offset
                    g = pxl[1] + offset
                    b = pxl[2] + offset
                    if r > 255:
                        r = 255
                    if g > 255:
                        g = 255
                    if b > 255:
                        b = 255
                    img.putpixel((x,y), (int(r), int(g), int(b)))
                else:
                    r = pxl[0] - offset
                    g = pxl[1] - offset
                    b = pxl[2] - offset
                    if r < 0:
                        r = 0
                    if g < 0:
                        g = 0
                    if b < 0:
                        b = 0
                    img.putpixel((x,y), (int(r), int(g), int(b)))
        return img

def percentageContrast(img, size, val, percentage):
    for x in range(size[0]):
        for y in range(size[1]):
            pxl = img.getpixel((x,y))
            mil = (pxl[0] + pxl[1] + pxl[2])/3
            if mil > val:
                r = ((255 - mil) * percentage) + pxl[0]
                g = ((255 - mil) * percentage) + pxl[1]
                b = ((255 - mil) * percentage) + pxl[2]
            else:
                r = pxl[0] - (mil * percentage)
                g = pxl[1] - (mil * percentage)
                b = pxl[2] - (mil * percentage)
            if r > 255:
                r = 255
            elif r < 0:
                r = 0
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            if b > 255:
                b = 255
            elif b < 0:
                b = 0
            img.putpixel((x,y), (int(r), int(g), int(b)))
    return img


image = getImage('~/Desktop/Python/images/image2.png')