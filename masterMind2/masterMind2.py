import os
import time
import random

settingsFile = os.path.expanduser('~/Desktop/Python/masterMind2/settings.txt')
waitTime = 0.2
welcome = ['\n - MasterMind','\x1B[3m by DrShock','\n\x1B[0mHope you enjoy!','- - - - - - - - - - - - -']
colorsChoose = ['\nChoose the colors you want to play with.','\nHere are the options :\n']
colorsChoose2 = ['\nTo choose the settings 1 : 1','To choose the settings 2 : 2','To choose the settings 3 : 3','To change the color settings : 4',]
colorsChange = ['\nWhich settings would you like to change? ( 1, 2, or 3 )']
colorsChange2 = ['\nWhat would you like to change it to? ( Format example : Red,Green,Blue,White,Black,Yellow,Orange,Purple )']
gameStart = ['\nThe game is starting...','Responses in this format are valid : Red,Blue,Green,Blue,Yellow,Orange','Correct pins will be shown by a |','Correct placements will be shown by a O','Colors that are not in the sequence will be shown by X']

def init(settings):
    file = open(settings)
    fileLines = file.readlines()
    file.close()
    settings1 = fileLines[0].split('\n')[0]
    settings2 = fileLines[1].split('\n')[0]
    settings3 = fileLines[2]
    for line in welcome:
        print(line)
        time.sleep(waitTime)
    return([settings1,settings2,settings3])

def chooseColors(colors,colorsFile):
    chose = False
    explained = False
    while chose == False:
        if explained == False:
            for line in colorsChoose:
                print(line)
                time.sleep(waitTime)
            for settings in colors:
                print('Settings ' + str(colors.index(settings) + 1) + ' : ' + settings)
                time.sleep(waitTime)
            for line in colorsChoose2:
                print(line)
                time.sleep(waitTime)
            explained = True
        decision = input('\n - Choice - ')
        time.sleep(waitTime)
        if decision == '1':
            chose = True
            chosenSettings = colors[0]
        elif decision == '2':
            chose = True
            chosenSettings = colors[1]
        elif decision == '3':
            chose = True
            chosenSettings = colors[2]
        elif decision == '4':
            explained = False
            for line in colorsChange:
                print(line)
                time.sleep(waitTime)
            chose2 = False
            acceptedResponses = ['1','2','3']
            while chose2 == False:
                decision2 = input(' - Choice - ')
                time.sleep(waitTime)
                if decision2 in acceptedResponses:
                    chose2 = True
                else:
                    print('Choice not valid')
                    time.sleep(waitTime)
            for line in colorsChange2:
                print(line)
                time.sleep(waitTime)
            change = input(' - Choice - ')
            time.sleep(waitTime)
            colors[int(decision2) - 1] = change
            file = open(colorsFile, 'w')
            file.write(colors[0] + '\n' + colors[1] + '\n' + colors[2])
            file.close()
            print('Settings ' + decision2 + ' have been changed to ' + change)
            time.sleep(waitTime)
        else:
            print('Choice not valid')
            time.sleep(waitTime)
    return(colors,decision)

def game(colors):
    for line in gameStart:
        print(line)
        time.sleep(waitTime)
    sequence = []
    unused = colors.split(',')
    for i in range(6):
        sequence.append(random.choice(unused))
        unused.pop(unused.index(sequence[-1]))
    print('Reminder of the chosen settings :\n' + colors + '\n')
    time.sleep(waitTime)
    end = False
    myGame = []
    while end == False:
        valid = False
        while valid == False:
            myGame.append(input(' - Sequence ' + str(len(myGame) + 1) + ' - \n'))
            time.sleep(waitTime)
            myGame[-1] = myGame[-1].split(',')
            if len(myGame[-1]) == 6:
                valid = True
            valid2 = 0
            for color in myGame[-1]:
                if color in colors:
                    valid2 += 1
            if valid2 == 6 and valid == True:
                valid = True
            else:
                valid = False
                print('Response not valid')
                time.sleep(waitTime)
                myGame.pop(-1)
        answer = ''
        for idx,pin in enumerate(myGame[-1]):
            if pin in sequence:
                if sequence[idx] == myGame[-1][idx]:
                    answer = answer + 'O '
                else:
                    answer = answer + '| '
            else:
                answer = answer + 'X '
        print(answer)
        time.sleep(waitTime)
        if answer == 'O O O O O O ':
            end = True
    print('You win in ' + str(len(myGame)) + ' attempts!')
    time.sleep(waitTime)

def main():
    settings = init(settingsFile)
    settings,chosenSettings = chooseColors(settings,settingsFile)
    done = False
    while done == False:
        game(settings[int(chosenSettings)-1])
        answered = False
        while answered == False:
            response = input('Would you like to stop? (Y/N)\n - ')
            time.sleep(waitTime)
            if response == 'Y':
                print('Quitting game...')
                time.sleep(waitTime)
                answered = True
                done = True
            elif response == 'N':
                print('Here we go for another round!')
                time.sleep(waitTime)
                answered = True
            else:
                print('Response not valid')
                time.sleep(waitTime)

main()
