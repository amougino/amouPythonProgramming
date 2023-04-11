# coding=utf8

from PIL import Image as Img
import os

folderPath = os.getcwd()  # For mac
#folderPath = 'P:\Documents\py' # For windows, the path to the program's folder

chars = [' ', '!', '“', '"', '#', '$', '%', '&', '‘', "'", '(', ')', '*', '+', ',', '-', 
         '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', 
         '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', 
         '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', 
         '~', '÷', '¡', '¢', '£', '€', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', 
         '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¿', 'À', 'Á',
         'Ã', 'Ä', 'Å', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 
         'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 
         'ä', 'å', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 
         'õ', 'ö', '÷', 'Б', 'Г', 'Д', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'П', 'У', 'Ф', 'Ц', 
         'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'б', 'в', 'г', 'д', 'ж', 'з', 'и', 
         'й', 'к', 'л', 'м', 'н', 'п', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 
         'э', 'ю', 'я', 'Δ', 'Θ', 'Λ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 
         'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'ς', 'σ', 'φ', 'ψ', 'ω', '∈']

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
        
def stabilizeKey(key):
    keySet = set(key[0:255])
    for i in range(256):
        if not i in keySet:
            keySet.add(i)
    return([list(keySet), [key[256], key[257]]])
    

def messageToNums(charactersList, message):
    for idx, i in enumerate(message):
        message[idx] = charactersList.index(i)
    return(message)
    
def numsToMessage(charactersList, message):
    for idx, i in enumerate(message):
        message[idx] = charactersList[i]
    return(message)

def rotor(character, rotorSetting, type):
    if type == 'encode':
        character += rotorSetting
    else:
        character += 256 - rotorSetting
    character %= 256
    return(character)

def plugboard(character, plugboardSetting, type):
    if type == 'encode':
        return(plugboardSetting[character])
    else:
        return(plugboardSetting.index(character))

def mirror(character):
    return(255 - character)

def scytale(operation, characters, message, imageNumbers):
    messageList = [char for char in message]
    messageNums = messageToNums(characters, messageList)
    possibleSetsInImgNums = len(imageNumbers) % 258
    if operation == 'encode':
        rotorChange = 0.5
    else:
        rotorChange = -0.5
    for idx in range(len(messageNums)):
        setNumber = idx % possibleSetsInImgNums
        stableKey = stabilizeKey(imageNumbers[(setNumber * 258):((setNumber * 258) + 258)])
        messageNums[idx] = plugboard(messageNums[idx], stableKey[0], operation)
        messageNums[idx] = rotor(messageNums[idx], stableKey[1][int(0.5 - rotorChange)], operation)
        messageNums[idx] = mirror(messageNums[idx])
        messageNums[idx] = rotor(messageNums[idx], stableKey[1][int(0.5 + rotorChange)], operation)
        messageNums[idx] = plugboard(messageNums[idx], stableKey[0], operation)
    return(''.join(numsToMessage(characters, messageNums)))
    
myText = 'en-Sydney College in Virginia, looked up one of the more'
img1Nums = imgToNums(getImg(folderPath, 'image.png'))
a = scytale('encode', chars, myText, img1Nums)
print(a)
print(scytale('decode', chars, a, img1Nums))

#71
#71
#107
#148
#179
#179
#[71, 80, 15, 53, 91, 70, 80, 71, 91, 0, 37, 81, 78, 78, 71, 73, 71, 0, 75, 80, 0, 56, 75, 84, 73, 75, 80, 75, 67, 14, 0, 78, 81, 81, 77, 71, 70, 0, 87, 82, 0, 81, 80, 71, 0, 81, 72, 0, 86, 74, 71, 0, 79, 81, 84, 71]

# 86 batches of 3 bytes (8 bits) -> first 256 bytes = plugboard, byte 257 = rotor 1, byte 258 = rotor 2
# plugboard -> rotor 1 -> mirror -> rotor 2 -> plugboard

# to do: Julia? https://medium.com/@alienrobot/part-1-julia-images-moving-from-python-to-julia-image-i-o-basic-manipulations-eecae73fe04d