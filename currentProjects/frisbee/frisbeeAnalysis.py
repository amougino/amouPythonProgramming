import os
import tkinter as tk
from tkinter.ttk import Combobox
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
readableButton.place(x = 22*guiScale, y = 50*guiScale)

enterExplanation = label(interface, 'Press Enter to confirm and Esc to exit', 'black', ('Times', int(15*guiScale)), 550*guiScale, 460*guiScale)

def getContents(event):
    selectedFile = fileSelector.get()
    if selectedFile.split('.')[1] == 'txt':
        fileData = getData(folderPath + selectedFile)
        if readableVar.get() == 1:
            useful = keepUseful(fileData, ['Time', 'AccX(g)', 'AccY(g)', 'AccZ(g)', 'GyroX(°/s)', 'GyroY(°/s)', 'GyroZ(°/s)', 'AngleX(°)', 'AngleY(°)', 'AngleZ(°)'])
            print(useful)
            print('1------')
            useful.pop(0)
            beautiful = beautify(useful)
            print(beautiful)
            print('2------')
            dataStr = dataToStr(beautiful, 'Time         AccX(g)   AccY(g)   AccZ(g)   GyX(°/s)  GyY(°/s)  GyZ(°/s)  AngX(°)   AngY(°)   AngZ(°)')
            print(dataStr)
            print('3------')
            saveData(dataStr, folderPath + 'test1.txt')
            print(' i did stuff i think')
        

interface.bind('<Return>', getContents)

def exit(event):
    interface.destroy()

interface.bind('<Escape>', exit)

interface.mainloop()

print(datetime.timedelta(hours = 13, minutes = 24, seconds = 26, milliseconds = 435) - datetime.timedelta(hours = 13, minutes = 24, seconds = 21, milliseconds = 274))

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