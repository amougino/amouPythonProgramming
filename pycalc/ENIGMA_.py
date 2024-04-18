# Enigma version "/"
# Plugboard - 8 Rotors - Reflector - 100 Characters
# Encode number : First 8 double digit numbers = Rotor settings (Each double digit number must be less than 50) Last 50 double digit numbers = Plugboard settings (Each double digit number must be less than 50 and there can be no reptitions here)

import random

print('')

charactersEnigma = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.',',','?','!','(',')','-','+','*','=','<','>',' ','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','"',':',';','[',']','@','#','{','}',"'",'é','è','ê','ë','à','â','á','ô','î','ï','û','ú','ù','ç']
print(charactersEnigma[99-28])
def splitString(string):
    return [char for char in string]

def unSplitString(string):
    response = ''
    for i in string:
        response = response + i
    return(response)

def readNumberEnigma(number):
    splitNumber = splitString(number)
    organizedNumber = []
    for i in range(0,len(splitNumber),2):
        a = str(splitNumber[i]) + str(splitNumber[i+1])
        organizedNumber.append(a)
    return(organizedNumber)

def plugboard(characterList,settings):
    for i in range(len(characterList)):
        characterList[i] = charactersEnigma[settings[charactersEnigma.index(characterList[i])+8]]
    return(characterList)     

def inversePlugboard(characterList,settings):
    for i in range(len(characterList)):
        a = charactersEnigma.index(characterList[i])
        for j in range(8,len(settings)):
            if settings[j] == a:
                b = j - 8
        characterList[i] = charactersEnigma[b]
    return(characterList)

def rotor(characterList,rotorNumber):
    for i in range(len(characterList)):
        loc = charactersEnigma.index(characterList[i])
        loc = loc + rotorNumber
        if loc > len(charactersEnigma) - 1:
            loc = loc - len(charactersEnigma)
        characterList[i] = charactersEnigma[loc]
    return(characterList)

def inverseRotor(characterList,rotorNumber):
    for i in range(len(characterList)):
        loc = charactersEnigma.index(characterList[i])
        loc = loc - rotorNumber
        if loc < 0:
            loc = loc + len(charactersEnigma)
        characterList[i] = charactersEnigma[loc]
    return(characterList)

def reflector(characterList):
  for i in range(len(characterList)):
    charLoc = charactersEnigma.index(characterList[i])
    charLoc = len(charactersEnigma) - 1 - charLoc
    characterList[i] = charactersEnigma[charLoc]
  return(characterList)

def encodeEnigma(text,number):
    list = splitString(text)
    numberSettings = readNumberEnigma(number)
    for i in range(len(numberSettings)):
        numberSettings[i] = int(numberSettings[i])
    plugboardList = plugboard(list,numberSettings)
    rotorList = plugboardList
    for i in range(8):
        rotorLoc = numberSettings[i]
        rotorList = rotor(rotorList,rotorLoc)
    reflectorList = reflector(rotorList)
    rotorList2 = reflectorList
    for i in range(8):
        inverse = 7 - i
        rotorLoc2 = numberSettings[inverse]
        rotorList2 = rotor(rotorList2,rotorLoc2)
    return(rotorList2)

def decodeEnigma(text,number):
    list = splitString(text)
    numberSettings = readNumberEnigma(number)
    for i in range(len(numberSettings)):
        numberSettings[i] = int(numberSettings[i])
    rotorList = list
    for i in range(8):
        rotorLoc = numberSettings[i]
        rotorList = inverseRotor(rotorList,rotorLoc)
    reflectorList = reflector(rotorList)
    rotorList2 = reflectorList
    for i in range(8):
        inverse = 7 - i
        rotorLoc2 = numberSettings[inverse]
        rotorList2 = inverseRotor(rotorList2,rotorLoc2)
    inversePlugboardList = inversePlugboard(rotorList2,numberSettings)
    return(inversePlugboardList)

def randomEncoder():
    numberList = []
    myList = []
    numberStr = ''
    for i in range(0,8):
        numberList.append(str(random.randrange(0,100)))
    for i in range(0,100):
        myList.append(str(i))
    for i in range(0,100):
        a = random.choice(myList)
        myList.pop(myList.index(a))
        numberList.append(a)
    for i in numberList:
        if len(i) == 1:
            numberList[numberList.index(i)] = '0' + i
    for i in numberList:
        numberStr = numberStr + i
    return(numberStr)
    
def main():

    print('')
    action = ''
    message = ''
    decodeNumber = 0

    on = True
    while on == True:

        answered = 0
        while answered == 0:
            answer = input('Encode (E) or Decode (D)? - ')
            if answer == 'E':
                action = 'encoding'
                answered = 1
            elif answer == 'D':
                action = 'decoding'
                answered = 1
            else:
                print('ERROR - Try again')

        answered2 = 0
        while answered2 == 0:
            answer2 = input('Text? - ')
            if answer2 != '':
                answered2 = 1
                toCheck = splitString(answer2)
                for i in toCheck:
                    if not i in charactersEnigma:
                        answered2 = 0
                if answered2 == 1:
                    message = answer2
                else:
                    print('ERROR - Character not valid')
            else:
                print('ERROR - Asked for response')

        answered3 = 0
        while answered3 == 0:
            answer3 = input('Encode / Decode number? - ')
            integer = 0
            try:
                test = int(answer3)
                integer = 1
            except ValueError:
                if answer3 == 'r':
                    print(' - Random Encoding - ')
                else:
                    print('ERROR - Answer not available')
            if integer == 1:
                if len(answer3) == len(charactersEnigma) * 2 + 16:
                    splitNumber = readNumberEnigma(answer3)
                    notValid = 0
                    test3 = []
                    for i in range(8,len(splitNumber)):
                        if splitNumber[i] in test3:
                            notValid = 1
                        else:
                            test3.append(splitNumber[i])
                    if notValid == 0:          
                        answered3 = 1
                        decodeNumber = answer3
                    else:
                        print('ERROR - Value not readable')
                else:
                    print('ERROR - Value not in right format (Must be '+ str(len(charactersEnigma) * 2 + 16) +' digits long)')
            elif answer3 == 'r':
                decoder = randomEncoder()
                print(decoder)
                decodeNumber = decoder
                answered3 = 1

        if action == 'encoding':
            encoded = encodeEnigma(message, decodeNumber)
            output = unSplitString(encoded)
            print('[Output] - [' + output + ']')

        elif action == 'decoding':
            decoded = decodeEnigma(message, decodeNumber)
            output = unSplitString(decoded)
            print('[Output] - [' + output + ']')

        answered4 = 0
        while answered4 == 0:
            answer4 = input('Turn Off (O) or Keep On (I) ? - ')
            if answer4 == 'I':
                on = True
                answered4 = 1
            elif answer4 == 'O':
                on = False
                answered4 = 1
            else:
                print('ERROR - Try again')

main()