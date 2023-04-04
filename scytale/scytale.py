# coding=utf8

from PIL import Image as Img
import os
import time #
import random

folderPath = os.getcwd() # For mac
#folderPath = 'P:\Documents\py' # For windows, the path to the program's folder

chars = [' ', '!', '“', '"', '#', '$', '%', '&', '‘', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '÷', '¡', '¢', '£', '€', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¿', 'À', 'Á', ' ', 'Ã', 'Ä', 'Å', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'Б', 'Г', 'Д', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'П', 'У', 'Ф', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'б', 'в', 'г', 'д', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'п', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'Δ', 'Θ', 'Λ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'ς', 'σ', 'φ', 'ψ', 'ω']

def splitString(string):
    return [char for char in string]

#img

def getImg(path = '', name = ''):
    filePath = path + '/scytale/' + name
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Img.open(file)
        return(img)
    except FileNotFoundError:
        raise Exception('File does not exist')
   
def saveImg(img, path, name):
    file = os.path.expanduser(path + '/scytale/' + name)
    img.save(file)

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

#codeConversion

def numsToImg(nums, size):
    img = createImg(size)
    pxlIdx = 0
    for x in range(size[0]):
        for y in range(size[1]):
            try:
                img.putpixel((x, y), (nums[3 * pxlIdx], nums[3 * pxlIdx + 1], nums[3 * pxlIdx + 2]))
            except IndexError:
                img.putpixel((x, y), (0, 0, 0))
            pxlIdx += 1
    return(img)

def imgToNums(img):
    nums = []
    size = img.size
    for x in range(size[0]):
        for y in range(size[1]):
            pxl = img.getpixel((x,y))
            for i in range(3):   
                nums.append(pxl[i])
    return(nums)
    
def generateRandomStableKey(length):
    timer1 = time.time() #
    stableKey, idx, plugboard = [], 0, [i for i in range(256)]
    for i in range(length):
        if idx < 256:
            num = random.choice(plugboard)
            plugboard.pop(plugboard.index(num))
            stableKey.append(num)
        else:
            stableKey.append(random.randrange(256))
        idx += 1
        if idx > 257:
            idx, plugboard = 0, [i for i in range(256)]
    while idx != 258:
        if idx < 256:
            num = random.choice(plugboard)
            plugboard.pop(plugboard.index(num))
            stableKey.append(num)
        else:
            stableKey.append(random.randrange(256))
        idx += 1    
    print('stabilizing total time ' + str(time.time() - timer1)) #
    return(stableKey)
    
def stabilizeKey(key):
    timer1 = time.time() #
    idx, plugboard = 0, []
    for i in range(len(key)):
        if idx < 256:
            while key[i] in plugboard:
                key[i] += 1
                key[i] %= 256
            plugboard.append(key[i])
        idx += 1
        if idx > 257:
            idx, plugboard = 0, []
    while idx != 258:
        if idx < 256:
            replacementNum = 0
            while replacementNum in plugboard:
                replacementNum += 1
            plugboard.append(replacementNum)
            key.append(replacementNum)
        else:
            key.append(1)
        idx += 1    
    
    print('stabilizing total time ' + str(time.time() - timer1)) #
    return(key)

#to do: change variable names (foo), remove all "pass"

print('step1')
new = getImg(folderPath, 'cassini.png')
print('step2')
nums = imgToNums(new)
print('step3')
key = stabilizeKey(nums)
print('step4')
saveImg(numsToImg(key, new.size), folderPath, 'image17.png')

# 86 batches of 3 bytes (8 bits) -> first 256 bytes = plugboard, byte 257 = rotor 1, byte 258 = rotor 2
# plugboard -> rotor 1 -> mirror -> rotor 2 -> plugboard

# to do: Julia? https://medium.com/@alienrobot/part-1-julia-images-moving-from-python-to-julia-image-i-o-basic-manipulations-eecae73fe04d

#trial 1 : 34.75253939628601 s
#trial 2 : 32.189963817596436 s
#trial 3 : 32.3187370300293 s
#trial 4 : 32.37806963920593 s
#trial 5 : 20.388001918792725 s