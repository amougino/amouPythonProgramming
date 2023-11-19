# -*- coding: utf-8 -*-

from math import pi, sqrt
import os
import tkinter as tk
from tkinter.ttk import Combobox
import matplotlib
import matplotlib.pyplot as plt
import datetime
import copy
#import more_itertools

# SETTINGS

#location of the file
folderPath = os.getcwd() + '/Data/' #for ben
#folderPath = os.getcwd() + '/frisbee/' #for mac
#folderPath = 'P:/Documents/python/frisbee/' #for windows

#size
#if guiScale = 1 then window size is 800x500
guiScale = 1.3

matplotlib.use('TkAgg')

def getData(filePath):
    file = open(filePath, 'r')
    fileLines = file.readlines()
    splitFileLines = []
    for i in fileLines:
        splitFileLines.append(i.split('\t'))
    return(splitFileLines)

def keepUseful(data, useful):
    toKeepIdx = []
    for obj in data[0]:
        if obj in useful:
            toKeepIdx.append(data[0].index(obj))
    newData = []
    for line in data:
        newLine = []
        for obj in toKeepIdx:
            newLine.append(line[obj])
        newData.append(newLine)
    return(newData)

def beautify(data):
    alignData = []
    for line in data:
        newLine = []
        for idx, obj in enumerate(line):
            if idx == 0:
                newLine.append(obj)
            else:
                lenObj = len(obj)
                if obj[0] == '-':
                    if lenObj == 8:
                        obj = obj[:1] + '0' + obj[1:]
                    elif lenObj == 7:
                        obj = obj[:1] + '00' + obj[1:]
                    elif lenObj == 6:
                        obj = obj[:1] + '000' + obj[1:]
                else:
                    if lenObj == 7:
                        obj = obj[:0] + '+0' + obj[0:]
                    elif lenObj == 6:
                        obj = obj[:0] + '+00' + obj[0:]
                    elif lenObj == 5:
                        obj = obj[:0] + '+000' + obj[0:]
                    else:
                        obj = obj[:0] + '+' + obj[0:]
                newLine.append(obj)
        alignData.append(newLine)
    return(alignData)

def dataToStr(data, dataTitle):
    stringData = ''
    for line in data:
        newLine = ''
        for obj in line:
            newLine += obj + ' '
        newLine = newLine[:-1]
        newLine += '\n'
        stringData += newLine
    stringData = stringData[:-1]
    return(dataTitle + '\n' + stringData)

def saveData(strData, filePath):
    file = open(filePath, 'w')
    file.write(strData)
    file.close()

def organize(data):
    newData = []
    for i in range(len(data[0])):
        newLine = []
        for j in data:
            if i > 0:
                newLine.append(float(j[i]))
            else:
                newLine.append(j[i])
        newData.append(newLine)
    return(newData)

def dateToTime(timeValues):
    startTime = datetime.timedelta(hours = int(timeValues[0][:2]), minutes = int(timeValues[0][3:5]), seconds = int(timeValues[0][6:8]), milliseconds = int(timeValues[0][9:]))
    newTime = []
    newTime.append(0)
    timeValues = list(timeValues)
    timeValues.pop(0)
    for i in range(len(timeValues)):
        timeAsDate = datetime.timedelta(hours = int(timeValues[i][:2]), minutes = int(timeValues[i][3:5]), seconds = int(timeValues[i][6:8]), milliseconds = int(timeValues[i][9:]))
        deltaT = timeAsDate - startTime
        newTime.append(deltaT.seconds + (float(deltaT.microseconds)/10**6))
    return(newTime)

def label(window, labelText, labelColor, labelFont, labelX, labelY):
    lbl = tk.Label(window, text = labelText, fg = labelColor, font = labelFont)
    lbl.place(x = labelX, y = labelY)
    return(lbl)

def text(window, textInputBorder, textInputX, textInputY, textInputWidth, textInputText = '', textInputState = False):
    if textInputState == False:
        txtfld = tk.Entry(window, text = textInputText, bd = textInputBorder, width = textInputWidth)
    else:
        txtfld = tk.Entry(window, text = textInputText, bd = textInputBorder, width = textInputWidth, state = textInputState)
    txtfld.place(x = textInputX, y = textInputY)
    return(txtfld)

interface = tk.Tk()
interface.title('frisbeeAnalysisInterface')
interface.geometry(str(int(800*guiScale)) + 'x' + str(int(500*guiScale)) + '+' + str(int(50*guiScale)) + '+' + str(int(50*guiScale)))
interface.configure(bg = '#eeeeee')

selectFile = label(interface, 'Select file to analyse :', 'black', ('Times', int(12.5*guiScale)), 22*guiScale, 6*guiScale)

filesInFolder = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]

fileSelector = Combobox(interface, values = filesInFolder, state = 'readonly', width = int(30*guiScale))
fileSelector.place(x = 22*guiScale, y = 28*guiScale)

readableVar = tk.IntVar()
readableButton = tk.Checkbutton(interface, text = 'Turn into readable', font = ('Times', int(12.5*guiScale)), variable = readableVar)
readableButton.place(x = 22*guiScale, y = 55*guiScale)

gyroVar = tk.IntVar()
gyroButton = tk.Checkbutton(interface, text = 'Show rotation speed evolution', font = ('Times', int(12.5*guiScale)), variable = gyroVar)
gyroButton.place(x = 22*guiScale, y = 75*guiScale)

rotVar = tk.IntVar()
rotButton = tk.Checkbutton(interface, text = 'Show number of rotations evolution', font = ('Times', int(12.5*guiScale)), variable = rotVar)
rotButton.place(x = 22*guiScale, y = 95*guiScale)

accVar = tk.IntVar()
accButton = tk.Checkbutton(interface, text = 'Show acceleration evolution', font = ('Times', int(12.5*guiScale)), variable = accVar)
accButton.place(x = 22*guiScale, y = 115*guiScale)

speedVar = tk.IntVar()
speedButton = tk.Checkbutton(interface, text = 'Show speed evolution', font = ('Times', int(12.5*guiScale)), variable = speedVar)
speedButton.place(x = 22*guiScale, y = 135*guiScale)

distVar = tk.IntVar()
distButton = tk.Checkbutton(interface, text = 'Show distance evolution', font = ('Times', int(12.5*guiScale)), variable = distVar)
distButton.place(x = 22*guiScale, y = 155*guiScale)

manualTimeLabel = label(interface, 'Enter manual time in ms (empty if not manual)', 'black', ('Times', int(12.5*guiScale)), 22*guiScale, 175*guiScale)

manualTimeVar = tk.StringVar()
manualTimeEntry = tk.Entry(interface, textvariable = manualTimeVar)
manualTimeEntry.place(x = 350*guiScale, y = 175*guiScale)

magVar = tk.IntVar()
magButton = tk.Checkbutton(interface, text = 'Show magnetic evolution (not ready)', font = ('Times', int(12.5*guiScale)), variable = magVar)
magButton.place(x = 22*guiScale, y = 195*guiScale)

enterExplanation = label(interface, 'Press Enter to confirm and Esc to exit', 'black', ('Times', int(15*guiScale)), 550*guiScale, 460*guiScale)

def waspos(n):
    poscount = 0
    for i in n:
        if i>0:
            poscount +=1
    if poscount>=(len(n)-1):
        return True
    else:
        return False

def wasneg(n):
    negcount = 0
    for i in n:
        if i<0:
            negcount +=1
    if negcount>=(len(n)-1):
        return True
    else:
        return False

def getContents(event):
    g = 9.81
    selectedFile = fileSelector.get()
    split = selectedFile.split('.')
    if len(split) > 1:
        if selectedFile.split('.')[-1] == 'txt':
            fileData = getData(folderPath + selectedFile)
            #ca ne marche pas pour lordi de lecole
            useful = keepUseful(fileData, ['Time', 'AccX(g)', 'AccY(g)', 'AccZ(g)', 'GyroX(°/s)', 'GyroY(°/s)', 'GyroZ(°/s)', 'AngleX(°)', 'AngleY(°)', 'AngleZ(°)', 'MagX(μt)', 'MagY(μt)', 'MagZ(μt)'])
            #ca marche pour lordi de lecole
            #useful = keepUseful(fileData, ['Time', 'AccX(g)', 'AccY(g)', 'AccZ(g)', 'GyroX(Â°/s)', 'GyroY(Â°/s)', 'GyroZ(Â°/s)', 'AngleX(Â°)', 'AngleY(Â°)', 'AngleZ(Â°)', 'MagX(Î¼t)', 'MagY(Î¼t)', 'MagZ(Î¼t)'])
            #print(fileData)
            #print(useful)
            usefulNoTitle = copy.copy(useful)
            usefulNoTitle.pop(0)
            organized = organize(usefulNoTitle)
            graphToShow = False
            try:
                manualTime = float(manualTimeVar.get())
                timeValues = [(manualTime*i)/1000 for i in range(len(organized[0]))]
            except ValueError:
                timeValues = dateToTime(organized[0])
            #print(timeValues)
            if readableVar.get() == 1:
                beautiful = beautify(usefulNoTitle)
                dataStr = dataToStr(beautiful, 'Time         AccX(g)   AccY(g)   AccZ(g)   GyroX(°/s)  GyroY(°/s)  GyZ(°/s)  AngX(°)   AngY(°)   AngZ(°)')
                saveData(dataStr, folderPath + 'beautify_' + split[0]+ '.txt')

            #----------------------------------------------------
            #Definie les indexe des donnees
            #----------------------------------------------------
            #ca ne marche pas sur lordi de lecole
            
            gyroXIdx = useful[0].index('GyroX(°/s)')
            gyroYIdx = useful[0].index('GyroY(°/s)')
            gyroZIdx = useful[0].index('GyroZ(°/s)')
            AccXIdx = useful[0].index('AccX(g)')
            AccYIdx = useful[0].index('AccY(g)')
            AccZIdx = useful[0].index('AccZ(g)')
            AngXIdx = useful[0].index('AngleX(°)')
            AngYIdx = useful[0].index('AngleY(°)')
            AngZIdx = useful[0].index('AngleZ(°)')
            MagXIdx = useful[0].index('MagX(μt)')
            MagYIdx = useful[0].index('MagY(μt)')
            MagZIdx = useful[0].index('MagZ(μt)')

            '''
            #ca marche sur lordi de lecole
            gyroXIdx = useful[0].index('GyroX(Â°/s)')
            gyroYIdx = useful[0].index('GyroY(Â°/s)')
            gyroZIdx = useful[0].index('GyroZ(Â°/s)')
            AccXIdx = useful[0].index('AccX(g)')
            AccYIdx = useful[0].index('AccY(g)')
            AccZIdx = useful[0].index('AccZ(g)')
            AngXIdx = useful[0].index('AngleX(Â°)')
            AngYIdx = useful[0].index('AngleY(Â°)')
            AngZIdx = useful[0].index('AngleZ(Â°)')
            MagXIdx = useful[0].index('MagX(Î¼t)')
            MagYIdx = useful[0].index('MagY(Î¼t)')
            MagZIdx = useful[0].index('MagZ(Î¼t)')
            '''

            gyro = [[],[],[]]
            if rotVar.get() + gyroVar.get() > 0:
                for idx, i in enumerate([gyroXIdx, gyroYIdx, gyroZIdx]):
                    for j in organized[i]:
                        gyro[idx].append((j*pi)/180)

            
            
            acc = [[],[],[]]
            if accVar.get() + speedVar.get() + distVar.get() + rotVar.get() + gyroVar.get() > 0:
                for idx, i in enumerate([AccXIdx, AccYIdx, AccZIdx]):
                    for j in organized[i]:
                        if idx == 2:
                            acc[idx].append((j + 1) * g)
                        else:
                            acc[idx].append(j * g)


            #----------------------------------------------------
            #Donne la vitesse angulaire en fonction du temps
            #----------------------------------------------------
            RAYON = 0.00722453563
            if gyroVar.get() == 1:
                graphToShow = True
                plt.figure(1)
                plt.suptitle('Evolution of rotation speed\n x = red, y = green, z = blue')
                plt.xlabel('Time')
                plt.ylabel('Rad/s')
                colors = ['r', 'g', 'b']
                for idx, x in enumerate([gyroXIdx, gyroYIdx, gyroZIdx]):
                    newgyro = []
                    if x == gyroXIdx:
                        xa = 0
                        xb = 0
                    elif x== gyroYIdx:
                        xa = 1
                        xb = 1
                    elif x == gyroZIdx:
                        xa = 2
                        xb = 2

                    tpr = []
                    tpr_time = []
                    for i in range (len(gyro[xa])):
                        sped  = acc[xb][i]
                        print(sped)
                        if sped<0:
                            speed = -sqrt(abs(sped/RAYON))
                        else:
                            speed = sqrt(abs(sped/RAYON))
                        
                        if speed < 100:
                            tpr_time.append(timeValues[i])
                            tpr.append(speed)


                    for i in range (len(gyro[xa])):
                        if abs(gyro[xa][i]) < 30: #1700 degree sec
                            newgyro.append(gyro[xa][i])
                        else:
                            try:
                                index = list(j>=timeValues[i] for j in tpr_time).index(True)
                                #print('index=',index)
                            except:
                                index = None


                            if index != None:
                                if organized[x][i]<0:
                                    newgyro.append(-tpr[index])
                                else:
                                    newgyro.append(tpr[index])
                            else:
                                newgyro.append(gyro[xa][i])

                    if newgyro != gyro[xa]:
                        plt.plot(timeValues, gyro[xa], color= 'aquamarine')
                    #print (timeValues,len(timeValues), "\n", newgyro, len(newgyro))
                    plt.plot(timeValues, newgyro, color = colors[idx])

            #----------------------------------------------------
            #Donne l'acceration en fonction du temps
            #----------------------------------------------------
            if accVar.get() == 1:
                print('acc')
                graphToShow = True
                plt.figure(2)
                plt.suptitle('Evolution of acceration\n x = red, y = green, z = blue')
                plt.xlabel('Time')
                plt.ylabel('m/s^2')
                colors = ['r', 'g', 'b']
                for i in range(len(acc)):
                    acceleration = []
                    for j in range(len(acc[i])):
                        acceleration.append(acc[i][j])
                    plt.plot(timeValues, acceleration, color = colors[i])


            #----------------------------------------------------
            #Donne le nombre de tours en fonction du temps
            #----------------------------------------------------
            if rotVar.get() == 1:
                #print('rot')
                graphToShow = True
                plt.figure(3)
                plt.suptitle('Evolution of number of rotations\n x = red, y = blue, z = green')
                plt.xlabel('Time')
                plt.ylabel('Rotations')
                colors = ['r', 'b', 'g']
                for idx, x in enumerate([gyroXIdx, gyroYIdx, gyroZIdx]):
                    rotationValues = []
                    rotations = 0
                    for i in range(len(gyro[xa])):
                        rotationValues.append(rotations)
                        if i != len(gyro[xa]) - 1:
                            rotations += (gyro[xa][i] * (timeValues[i + 1] - timeValues[i]))/2*pi
                    plt.plot(timeValues, rotationValues, color = colors[idx])
            #----------------------------------------------------
            #Donne la vitesse et ou la distance en fonction du temps
            #----------------------------------------------------
            if speedVar.get() == 1 or distVar.get() == 1:
                graphToShow = True
                speed = [[],[],[]]
                for idx, i in enumerate(acc):
                    speedVal = 0
                    for j in range(len(i) - 1):
                        speedVal += (i[j] - 1)*(timeValues[j + 1] - timeValues[j])
                        speed[idx].append(speedVal)
                speedTimeValues = copy.copy(timeValues)
                speedTimeValues.pop(-1)
                if speedVar.get() == 1:
                    #print('speed')
                    plt.figure(4)
                    plt.suptitle('Evolution of Speed\n x = red, y = green, z = blue')
                    plt.xlabel('Time')
                    plt.ylabel('m/s')
                    colors = ['r', 'g', 'b']
                    for i in range(3):
                        plt.plot(speedTimeValues, speed[i], color = colors[i])
                    #print(len(speedTimeValues), len(speed[0]))
                if distVar.get() == 1:
                    #print('distance')
                    distance = [[],[],[]]
                    for xyz in range(3):
                        distVal = 0
                        for i in range(len(speed[xyz]) - 1):
                            distVal += speed[xyz][i]*(speedTimeValues[i + 1] - speedTimeValues[i])
                            distance[xyz].append(distVal)
                    plt.figure(5)
                    plt.suptitle('Evolution of Distance\n x = red, y = green, z = blue')
                    plt.xlabel('Time')
                    plt.ylabel('m')
                    colors = ['r', 'g', 'b']
                    distanceTimeValues = copy.copy(speedTimeValues)
                    distanceTimeValues.pop(-1)
                    #print(len(distanceTimeValues))
                    #print(len(distance[0]))
                    for i in range(3):
                        plt.plot(distanceTimeValues, distance[i], color = colors[i])

            #Donne les valeurs de magnetique brutes



            if magVar.get() == 1:
                #print('mag')
                graphToShow = True
                plt.figure(6)
                plt.suptitle('Evolution of magnetic\n x = red, y = green, z = blue')
                plt.xlabel('Time')
                plt.ylabel('μt/s')
                colors = ['r', 'g', 'b']
                for idx, i in enumerate([MagXIdx, MagYIdx, MagZIdx]):
                    magnetic = []
                    for j in range(len(organized[i])):
                        magnetic.append(organized[i][j])
                    plt.plot(timeValues, magnetic, color = colors[idx])

            if graphToShow == True:
                plt.show()


interface.bind('<Return>', getContents)

def exit(event):
    interface.destroy()

interface.bind('<Escape>', exit)

interface.mainloop()

#print(datetime.timedelta(hours = 13, minutes = 24, seconds = 26, milliseconds = 435) - datetime.timedelta(hours = 13, minutes = 24, seconds = 21, milliseconds = 274))

'''
To do
Graphics
Done    - Acceration
        - speed evolution (all, x, y, z)
Done    - gyro evolution (all, x, y, z)
        - distance evolution (all, x, y, z)
File with all data on the flight: (find beginning / end flight)
 - rotations
 - start rotation speed
 - start speed
 - start height
 - distance
 - wobble amount
3d visualization
'''