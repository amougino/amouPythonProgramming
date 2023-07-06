import os

textFile = os.getcwd() + '/currentProjects/esolangTest.txt'

myEsolangSettings = {'characters':[' ', '!', '"', '#', '%', '&', "'", '(', 
                                 ')', '*', '+', ',', '-', '.', '/', '0', 
                                 '1', '2', '3', '4', '5', '6', '7', '8', 
                                 '9', ':', ';', '<', '=', '>', '?', '@', 
                                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                                 'y', 'z', '[', '\\', ']', '_', '|', '~'],
                   'base8Characters':['_', '&', '~', '.', ',', ';', ':', '|'], 
                   'dotForFloats':'/',
                   'importCharacter':'>',
                   'variableCharacter':';',
                   'equalCharacter':'!',
                   'stringCharacter':'#',
                   'integerCharacter':'_',
                   'listCharacter':'/'}

def base8ToText(esolangSettings, text):
    newText = ''
    for charPair in range(int(len(text)/2)):
        newText += (esolangSettings['characters'][(esolangSettings['base8Characters'].index(text[charPair * 2]) * 8) + esolangSettings['base8Characters'].index(text[(charPair * 2) + 1])])
    return(newText)

def esolang(esolangSettings, filePath):
    
    file = open(filePath, 'r')
    fileLines = file.read()
    newFileLines = []

    depth = 0

    for lineIdx, line in enumerate(fileLines.split('\n')):
        newFileLines.append('')
        if line != '':
            if line[0] == esolangSettings['importCharacter']:
                if depth == 0:
                    newFileLines[-1] += 'import ' + base8ToText(esolangSettings, line[1:])
                else:
                    return(f'Error - line {lineIdx}, please place import in an area with no depth')
            elif line[0] == esolangSettings['variableCharacter']:
                variable = line[1:].split(esolangSettings['equalCharacter'])
                for tab in range(depth):
                    newFileLines[-1] += '   '
                newFileLines[-1] += base8ToText(esolangSettings, variable[0]) + ' = '
                if variable[1][0] == esolangSettings['stringCharacter']:
                    newFileLines[-1] += "'" + base8ToText(esolangSettings, variable[1][1:]) + "'"


    for line in newFileLines:
        print(line)

esolang(myEsolangSettings, textFile)