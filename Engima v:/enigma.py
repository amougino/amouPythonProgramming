# Enigma version "/"
# Plugboard - 8 Rotors - Reflector - 100 Characters
# Encode number : First 8 double digit numbers = Rotor settings (Each double digit number must be less than 50) Last 50 double digit numbers = Plugboard settings (Each double digit number must be less than 50 and there can be no reptitions here)

print('')

characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.',',','?','!','(',')','-','+','*','=','<','>',' ','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','"',':',';','[',']','@','#','{','}',"'",'é','è','ê','ë','à','â','á','ô','î','ï','û','ú','ù','ç']
print(characters[99-28])
def splitString(string):
    return [char for char in string]

def unSplitString(string):
    response = ''
    for i in string:
        response = response + i
    return(response)

def readNumber(number):
    splitNumber = splitString(number)
    organizedNumber = []
    for i in range(0,len(splitNumber),2):
        a = str(splitNumber[i]) + str(splitNumber[i+1])
        organizedNumber.append(a)
    return(organizedNumber)

def plugboard(characterList,settings):
    for i in range(len(characterList)):
        characterList[i] = characters[settings[characters.index(characterList[i])+8]]
    return(characterList)     

def inversePlugboard(characterList,settings):
    for i in range(len(characterList)):
        a = characters.index(characterList[i])
        for j in range(8,len(settings)):
            if settings[j] == a:
                b = j - 8
        characterList[i] = characters[b]
    return(characterList)

def rotor(characterList,rotorNumber):
    for i in range(len(characterList)):
        loc = characters.index(characterList[i])
        loc = loc + rotorNumber
        if loc > len(characters) - 1:
            loc = loc - len(characters)
        characterList[i] = characters[loc]
    return(characterList)

def inverseRotor(characterList,rotorNumber):
    for i in range(len(characterList)):
        loc = characters.index(characterList[i])
        loc = loc - rotorNumber
        if loc < 0:
            loc = loc + len(characters)
        characterList[i] = characters[loc]
    return(characterList)

def reflector(characterList):
  for i in range(len(characterList)):
    charLoc = characters.index(characterList[i])
    charLoc = len(characters) - 1 - charLoc
    characterList[i] = characters[charLoc]
  return(characterList)

def encode(text,number):
    list = splitString(text)
    numberSettings = readNumber(number)
    print(numberSettings[57+8])
    print(list)
    for i in range(len(numberSettings)):
        numberSettings[i] = int(numberSettings[i])
    plugboardList = plugboard(list,numberSettings)
    print(plugboardList)
    rotorList = plugboardList
    for i in range(8):
        rotorLoc = numberSettings[i]
        rotorList = rotor(rotorList,rotorLoc)
    print(rotorList)
    reflectorList = reflector(rotorList)
    print(reflectorList)
    rotorList2 = reflectorList
    for i in range(8):
        inverse = 7 - i
        rotorLoc2 = numberSettings[inverse]
        rotorList2 = rotor(rotorList2,rotorLoc2)
        print(rotorList2)
    print(rotorList2)
    return(rotorList2)

def decode(text,number):
    list = splitString(text)
    numberSettings = readNumber(number)
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
    
def main():

    action = ''
    message = ''
    decodeNumber = 0

    on = 1
    while on == 1:

        answered = 0
        while answered == 0:
            answer = input('Encode ( E ) or Decode ( D ) ? - ')
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
            answer2 = input('Text ? - ')
            if answer2 != '':
                answered2 = 1
                toCheck = splitString(answer2)
                for i in toCheck:
                    if not i in characters:
                        answered2 = 0
                if answered2 == 1:
                    message = answer2
                else:
                    print('ERROR - Character not valid')
            else:
                print('ERROR - Asked for response')

        answered3 = 0
        while answered3 == 0:
            answer3 = input('Encode / Decode number ? - ')
            integer = 0
            try:
                test = int(answer3)
                integer = 1
            except ValueError:
                print('ERROR - Answer not available')
            if integer == 1:
                test2 = splitString(answer3)
                if len(test2) == len(characters) * 2 + 16:
                    splitNumber = readNumber(answer3)
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
                    print('ERROR - Value not in right format (Must be '+ str(len(characters) * 2 + 16) +' digits long)')

        if action == 'encoding':
            encoded = encode(message, decodeNumber)
            output = unSplitString(encoded)
            print('Output (between brackets) - [' + output + ']')

        elif action == 'decoding':
            decoded = decode(message, decodeNumber)
            output = unSplitString(decoded)
            print('Output (between brackets) - [' + output + ']')

        answered4 = 0
        while answered4 == 0:
            answer4 = input('Turn Off ( O ) or Keep On ( I ) ? - ')
            if answer4 == 'I':
                on = 1
                answered4 = 1
            elif answer4 == 'O':
                on = 0
                answered4 = 1
            else:
                print('ERROR - Try again')

#main()