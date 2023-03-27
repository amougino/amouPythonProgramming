from PIL import Image as Img
import os

#folderPath = os.getcwd()
folderPath = 'P:\Documents\py'

chars = [' ', '!', '“', '#', '$', '%', '&', '‘', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '÷', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', ' ', 'Ã', 'Ä', 'Å', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'Б', 'Г', 'Д', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'П', 'У', 'Ф', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'б', 'в', 'г', 'д', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'п', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'Δ', 'Θ', 'Λ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'ς', 'σ', 'φ', 'ψ', 'ω']

def splitString(string):
    return [char for char in string]

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
    bits = ''
    for i in range(8):
        if num >= 2**(7-i):
            num -= 2**(7-i)
            bits += '1'
        else:
            bits += '0'
    return(bits) 

def byteToNum(byte):
    num = 0
    for i in range(len(byte)):
        num += int(byte[i]) * (2 ** (len(byte) - 1 - i))
    return(num)
   
def byteAdd(byte1, byte2):
   pass

#codeConversion

def bitsToImg(bits, size):
    img = createImg(size)
    for x in range(size[0]):
        for y in range(size[1]):
            try:
                colorBits = bits[(x * size[1]) + y]
                colors = []
                for i in colorBits:
                    colors.append(byteToNum(i))
                img.putpixel((x, y), (colors[0], colors[1], colors[2]))
            except IndexError:
                img.putpixel((x, y), (0, 0, 0))
    return(img)

def imgToBits(img):
    foo = []
    size = img.size
    for x in range(size[0]):
        for y in range(size[1]):
            pxl = img.getpixel((x,y))
            foo.append([numToBits(pxl[0]), numToBits(pxl[1]), numToBits(pxl[2])])
    return(foo)


#print('step1')
#new = getImg(folderPath, 'image4.png')
#print('step2')
#byte = imgToBits(new)
#print('step3')
#saveImg(bitsToImg(byte, ((new.size[0] + 1), (new.size[1] + 1))), folderPath, 'image3.png')

# 86 batches of 3 bytes (8 bits) -> first 256 bytes = plugboard, byte 257 = rotor 1, byte 258 = rotor 2
# plugboard -> rotor 1 -> mirror -> rotor 2 -> plugboard

def stabilizeKey(key):
    byteKey = []
    for obj in key:
        for byte in obj:
            byteKey.append(byte)
    stableKey = []
    while len(byteKey) != 0:
        plugboardKey = []
        for i in range(86):
            if i < 84:
                if len(byteKey) != 0:
                    valid = False
                    while valid == False:
                        if byteKey[0] in plugboardKey:
                           pass
            else:
               pass
    return(stableKey)
print(len(chars))
#to do: change variable names (foo), remove all "pass"