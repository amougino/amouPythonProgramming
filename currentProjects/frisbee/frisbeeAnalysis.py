import os
import tkinter as tk
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
import datetime

# SETTINGS

#location of the file
folderPath = os.getcwd() + '/currentProjects/frisbee/' #for mac
#folderPath = 'P:/Documents/python/frisbee/' #for windows

#size
#if guiScale = 1 then window size is 800x500
guiScale = 1.6

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
        newTime.append(int(1000*(deltaT.seconds + (deltaT.microseconds/1000000)))/1000)
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
interface.geometry(f'{int(800*guiScale)}x{int(500*guiScale)}+{int(50*guiScale)}+{int(50*guiScale)}')
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

enterExplanation = label(interface, 'Press Enter to confirm and Esc to exit', 'black', ('Times', int(15*guiScale)), 550*guiScale, 460*guiScale)

def getContents(event):
    selectedFile = fileSelector.get()
    split = selectedFile.split('.')
    if len(split) > 1:
        if selectedFile.split('.')[-1] == 'txt':
            fileData = getData(folderPath + selectedFile)
            useful = keepUseful(fileData, ['Time', 'AccX(g)', 'AccY(g)', 'AccZ(g)', 'GyroX(°/s)', 'GyroY(°/s)', 'GyroZ(°/s)', 'AngleX(°)', 'AngleY(°)', 'AngleZ(°)'])
            usefulNoTitle = useful.copy()
            usefulNoTitle.pop(0)
            organized = organize(usefulNoTitle)
            graphToShow = False
            timeValues = dateToTime(organized[0])
            if readableVar.get() == 1:
                beautiful = beautify(usefulNoTitle)
                dataStr = dataToStr(beautiful, 'Time         AccX(g)   AccY(g)   AccZ(g)   GyX(°/s)  GyY(°/s)  GyZ(°/s)  AngX(°)   AngY(°)   AngZ(°)')
                saveData(dataStr, folderPath + 'beautify_' + split[0]+ '.txt')
            elif gyroVar.get() == 1:
                graphToShow = True
                gyroXIdx = useful[0].index('GyroX(°/s)')
                gyroYIdx = useful[0].index('GyroY(°/s)')
                gyroZIdx = useful[0].index('GyroZ(°/s)')
                plt.figure(1)
                plt.suptitle('Evolution of rotation speed\n x = red, y = blue, z = green')
                plt.xlabel('Time')
                plt.ylabel('Degrees/s')
                colors = ['r', 'b', 'g']
                for idx, x in enumerate([gyroXIdx, gyroYIdx, gyroZIdx]):
                    plt.plot(timeValues, organized[x], colors[idx])
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
 - acceleration evolution (all, x, y, z)
 - speed evolution (all, x, y, z)
 - gyro evolution (all, x, y, z)
 - distance evolution (all, x, y, z)
File with all data on the flight: (find beginning / end flight)
 - rotations
 - start rotation speed
 - start speed
 - start height
 - start height
 - distance
 - wobble amount
3d visualization
'''