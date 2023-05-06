#MasterMind

#Imports

import random

import time

#Variables

    #Intro

welcome = [' - MasterMind - ','','This program was created by Amou.','','Hope you enjoy!','','']

    #Colors

colorExplanation = ['First, choose the colors you want to play with.','','Here are the options :','']

colorExplanation2 = ['To choose the default colors : 0','','To choose the settings 1 : 1','','To choose the settings 2 : 2','','To choose the settings 3 : 3','','To change the color settings : 4','',]

defaultColors = ['Red','Orange','Yellow','Green','Blue','Purple']

settings1 = []

settings2 = []

settings3 = []

settingsFile = 'MasterMindSettings.txt'

    #Other

defaultAttempts = 10

minColors = 6

maxColors = 16

#Functions

def intro():
    
    for i in welcome:
        print(i)
        time.sleep(0.1)

def getColorSettings(txtFile):
    
    file = open(txtFile)
    fileLines = file.readlines()
    file.close()

    settings1 = fileLines[0].split(',')
    settings1[len(settings1)-1] = settings1[len(settings1)-1].split('\n')[0]

    settings2 = fileLines[1].split(',')
    settings2[len(settings2)-1] = settings2[len(settings2)-1].split('\n')[0]

    settings3 = fileLines[2].split(',')
    settings3[len(settings3)-1] = settings3[len(settings3)-1].split('\n')[0]
    print(settings1,settings2,settings3)
    return(settings1,settings2,settings3)
    print(settings1,settings2,settings3)

def chooseColors(txtFile):

    settings1,settings2,settings3 = getColorSettings(txtFile)
    print(settings1,settings2,settings3)
    
    for i in colorExplanation:
        print(i)
        time.sleep(0.1)

    print('Default Colors :')
    time.sleep(0.1)
    print('')
    time.sleep(0.1)
    for i in defaultColors:
        print(i)
        time.sleep(0.1)
    print('')
    time.sleep(0.1)

    print('Settings 1 :')
    time.sleep(0.1)
    print('')
    time.sleep(0.1)
    for i in settings1:
        print(i)
        time.sleep(0.1)
    print('')
    time.sleep(0.1)

    print('Settings 2 :')
    time.sleep(0.1)
    print('')
    time.sleep(0.1)
    for i in settings2:
        print(i)
        time.sleep(0.1)
    print('')
    time.sleep(0.1)

    print('Settings 3 :')
    time.sleep(0.1)
    print('')
    time.sleep(0.1)
    for i in settings3:
        print(i)
        time.sleep(0.1)
    print('')
    time.sleep(0.1)

    for i in colorExplanation2:
        print(i)
        time.sleep(0.1)

    answered1 = 0

    while answered1 == 0:

        choice1 = input(' - ')
        time.sleep(0.1)
        print('')

        if choice1 == '0':
            answered1 = 1
            colors = defaultColors
            print('You chose :')
            time.sleep(0.1)
            print('')
            time.sleep(0.1)
            for i in colors:
                print(i)
                time.sleep(0.1)

        elif choice1 == '1':
            answered1 = 1
            colors = settings1
            print('You chose :')
            time.sleep(0.1)
            print('')
            time.sleep(0.1)
            for i in colors:
                print(i)
                time.sleep(0.1)

        elif choice1 == '2':
            answered1 = 1
            colors = settings2
            print('You chose :')
            time.sleep(0.1)
            print('')
            time.sleep(0.1)
            for i in colors:
                print(i)
                time.sleep(0.1)

        elif choice1 == '3':
            answered1 = 1
            colors = settings3
            print('You chose :')
            time.sleep(0.1)
            print('')
            time.sleep(0.1)
            for i in colors:
                print(i)
                time.sleep(0.1)

        elif choice1 == '4':
            
            answered1 = 1
            
            answered2 = 0
            while answered2 == 0:

                print('Which settings would you like to change? (1,2,3)')
                time.sleep(0.1)
                print('')
                time.sleep(0.1)
                choice2 = input(' - ')
                time.sleep(0.1)
                print('')
                time.sleep(0.1)

                if choice2 == '1':
                    answered2 = 1
                    settingsToChange = 1

                elif choice2 == '2':
                    answered2 = 1
                    settingsToChange = 2

                elif choice2 == '3':
                    answered2 = 1
                    settingsToChange = 3

                else:
                    print('That answer is not valid, try again.')
                    time.sleep(0.1)
                    print('')
                    time.sleep(0.1)

            answered3 = 0
            while answered3 == 0:

                print('What do you want to change it to? (Format example : Blue,Red,Yellow,Green,Black,White)')
                time.sleep(0.1)
                print('')
                time.sleep(0.1)
                choice3 = input(' - ')
                time.sleep(0.1)
                print('')
                time.sleep(0.1)

                change = choice3

                if len(change.split(',')) >= minColors and len(change.split(',')) <= maxColors:

                    answered3 = 1

                    file = open(txtFile)
                    fileLines = file.readlines()
                    file.close()

                    settings1 = fileLines[0]
                    settings1 = settings1.split('\n')[0]
                    settings2 = fileLines[1]
                    settings2 = settings1.split('\n')[0]
                    settings3 = fileLines[2]
                    settings3 = settings1.split('\n')[0]
                    
                    newLines = [settings1,settings2,settings3]

                    newLines[settingsToChange-1] = change
                    print(newLines)

                    newLines[0] = newLines[0] + '\n'
                    newLines[1] = newLines[1] + '\n'
                    
                    newLines2 = newLines[0]
                    
                    for i in range(len(newLines)-1):
                        newLines2 = newLines2 + newLines[i]
                        
                    
                    file = open(txtFile, 'w')
                    file.write(newLines2)
                    file.close()

                    print('You changed settings',settingsToChange,'to',change,'.')
                    time.sleep(0.1)
                    print('')
                    time.sleep(0.1)
                    chooseColors(settingsFile)
                    
                else:
                    print('That answer is not valid, try again.')
                    time.sleep(0.1)
                    print('')
                    time.sleep(0.1)

        else:
            print('That answer is not valid, try again.')
            time.sleep(0.1)
            print('')
            time.sleep(0.1)

intro()
#settings1,settings2,settings3 = getColorSettings(settingsFile)
chooseColors(settingsFile)

    
    #file = open(txtFile, 'w')
    #file.write(newLines)
    #file.close()
