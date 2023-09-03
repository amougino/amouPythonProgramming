import os

textFile = os.getcwd() + '/currentProjects/esolang/esolangTest.txt'

myEsolangSettings = {'characters':[' ', '!', '"', '#', '%', '&', "'", '(', 
                                 ')', '*', '+', ',', '-', '.', '/', '0', 
                                 '1', '2', '3', '4', '5', '6', '7', '8', 
                                 '9', ':', ';', '<', '=', '>', '?', '@', 
                                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                                 'y', 'z', '[', '\\', ']', '_', '|', '~'],
                   'base8Characters':['_', '&', '~', '.', ',', ';', '<', '>'], 
                   'dotForFloats':'/',
                   'importCharacter':'>',
                   'variableCharacter':';',
                   'equalCharacter':'!',
                   'stringCharacter':'#',
                   'integerCharacter':'_',
                   'listCharacter':'/'}

def base8ToText(esolangSettings, text):

    newText = ''
    try:
        for charPair in range(int(len(text)/2)):
            newText += (esolangSettings['characters'][(esolangSettings['base8Characters'].index(text[charPair * 2]) * 8) + esolangSettings['base8Characters'].index(text[(charPair * 2) + 1])])
    except ValueError:
        return(False)

    return(newText)

def insertDollar(string, index):
    return(string[:index] + '$' + string[index:])

def saveToFile(lines, filePath):

    linesAsStr = ''
    for idx, line in enumerate(lines):
        if idx != len(lines) - 1:
            linesAsStr += line + '\n'
        else:
            linesAsStr += line
    f = open(filePath, "w")
    f.write(linesAsStr.replace('$', '\\'))
    f.close()

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
                    text = base8ToText(esolangSettings, line[1:])
                    if text != False:
                        newFileLines[-1] += 'import ' + text
                    else:
                        return(f'Error - line {lineIdx}, unknown symbols were found when defining the name of the module to import')
                else:
                    return(f'Error - line {lineIdx}, please place import in an area with no depth')
                
            elif line[0] == esolangSettings['variableCharacter']:
                variable = line[1:].split(esolangSettings['equalCharacter'])
                for tab in range(depth):
                    newFileLines[-1] += '   '
                text = base8ToText(esolangSettings, variable[0])
                if text != False:
                    newFileLines[-1] += text + ' = '
                else:
                    return(f'Error - line {lineIdx}, unknown symbols were found when defining the name of the variable')
                if variable[1][0] == esolangSettings['stringCharacter']:
                    text = base8ToText(esolangSettings, variable[1][1:])
                    if text != False:
                        if "'" in text:
                            if '"' in text:
                                for idx, char in enumerate(text):
                                    if char == "'":
                                        text = insertDollar(text, idx)
                                newFileLines[-1] += "'" + text + "'"
                            else:
                                newFileLines[-1] += "'" + text + "'"
                        elif '"' in text:
                            newFileLines[-1] += "'" + text + "'"
                    else:
                        return(f'Error - line {lineIdx}, unknown symbols were found when giving the value of the variable')

            else:
                return(f'Error - line {lineIdx}, please start a line with a known function')
    return(newFileLines)

new = esolang(myEsolangSettings, textFile)
print(new)
newPythonProgram = os.getcwd() + '/currentProjects/esolang/esolangTest2.py'
saveToFile(new, newPythonProgram)