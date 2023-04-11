# coding=utf8

from PIL import Image as Img
import os

def getImg(path = '', name = ''):
    filePath = path + '/scytale/' + name
    file = os.path.expanduser(filePath)
    if file == '':
        raise Exception('File not defined')
    try:
        img = Img.open(file)
        return(img)
    except FileNotFoundError:
        return(False)
   
def saveImg(img, path, name):
    file = os.path.expanduser(path + '/scytale/' + name)
    img.save(file)

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

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
    
def checkIfMessageValid(charactersList, message):
    valid = True
    for i in message:
        if not i in charactersList:
            valid = False
    return(valid)

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

# 86 batches of 3 bytes (8 bits) -> first 256 bytes = plugboard, byte 257 = rotor 1, byte 258 = rotor 2
# plugboard -> rotor 1 -> mirror -> rotor 2 -> plugboard

# to do: Julia? https://medium.com/@alienrobot/part-1-julia-images-moving-from-python-to-julia-image-i-o-basic-manipulations-eecae73fe04d