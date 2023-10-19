import os
import tkinter as tk
from tkinter.ttk import Combobox

folderPath = os.getcwd() + '/currentProjects/frisbee/'
# For mac
#folderPath = 'P:\Documents\py'
# # For windows, the path to the program's folder

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
interface.geometry('1500x800+100+100')

filesInFolder = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]

fileSelector = Combobox(interface, values = filesInFolder, state = 'readonly', width = 50)
fileSelector.place(x = 45, y = 80)

enterExplanation = label(interface, 'Press Enter to confirm and Esc to exit', 'black', ('Times', 30), 1000, 730)
selectFile = label(interface, 'Select file to analyse :', 'black', ('Times', 25), 40, 40)

def getContents(event):
    print(fileSelector.get())

interface.bind('<Return>', getContents)

def exit(event):
    interface.destroy()

interface.bind('<Escape>', exit)

interface.mainloop()