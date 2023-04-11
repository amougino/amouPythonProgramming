import scytale as scy
import os
from tkinter import *
from tkinter.ttk import Combobox

folderPath = os.getcwd()  # For mac
#folderPath = 'P:\Documents\py' # For windows, the path to the program's folder

chars = [' ', '!', '“', '"', '#', '$', '%', '&', '‘', "'", '(', ')', '*', '+', ',', '-', 
         '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', 
         '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', 
         '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', 
         '~', '÷', '¡', '¢', '£', '€', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', 
         '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¿', 'À', 'Á',
         'Ã', 'Ä', 'Å', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 
         'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 
         'ä', 'å', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 
         'õ', 'ö', 'Б', 'Г', 'Д', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'П', 'У', 'Ф', 'Ц', 'Ч', 
         'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'б', 'в', 'г', 'д', 'ж', 'з', 'и', 'й', 
         'к', 'л', 'м', 'н', 'п', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 
         'ю', 'я', 'Δ', 'Θ', 'Λ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 
         'ζ', 'η', 'θ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'ς', 'σ', 'φ', 'ψ', 'ω', '∈', '∉']

def label(window, labelText, labelColor, labelFont, labelX, labelY):
    lbl = Label(window, text = labelText, fg = labelColor, font = labelFont)
    lbl.place(x = labelX, y = labelY)
    return(lbl)

def textInput(window, textInputBorder, textInputX, textInputY, textInputWidth, textInputText = '', textInputState = False):
    if textInputState == False:
        txtfld = Entry(window, text = textInputText, bd = textInputBorder, width = textInputWidth)
    else:
        txtfld = Entry(window, text = textInputText, bd = textInputBorder, width = textInputWidth, state = textInputState)
    txtfld.place(x = textInputX, y = textInputY)
    return(txtfld)

def getContents():
    print('encode or decode : ' + str(encodeOrDecode.get()))
    print('image file : ' + imageSelector.get())
    print('message : ' + messageTextInputContents.get())
    if encodeOrDecode.get() == 1:
        operationType = 'encode'
    else:
        operationType = 'decode'
    if imageSelector.get() != '':
        image = scy.getImg(folderPath, imageSelector.get())
        messageValid = scy.checkIfMessageValid(chars, messageTextInputContents.get())
        if messageValid == True:
            if image != False:
                resultTextInput = textInput(win, 3, 40, 330, 150, textInputState = 'readonly')
                resultTextInputContents = StringVar()
                resultTextInputContents.set(scy.scytale(operationType, chars, messageTextInputContents.get(), scy.imgToNums(image)))
                resultTextInput['textvariable'] = resultTextInputContents
            else:
                resultTextInput = textInput(win, 3, 40, 330, 150, textInputState = 'readonly')
                resultTextInputContents = StringVar()
                resultTextInputContents.set('! Image not valid')
                resultTextInput['textvariable'] = resultTextInputContents
        else:
            resultTextInput = textInput(win, 3, 40, 330, 150, textInputState = 'readonly')
            resultTextInputContents = StringVar()
            resultTextInputContents.set('! Message not valid')
            resultTextInput['textvariable'] = resultTextInputContents
    else:
        resultTextInput = textInput(win, 3, 40, 330, 150, textInputState = 'readonly')
        resultTextInputContents = StringVar()
        resultTextInputContents.set('! Enter a image')
        resultTextInput['textvariable'] = resultTextInputContents

def exit(event):
    win.destroy()

win = Tk()

win.title('scytale')
win.geometry("1600x450+150+100")

operationLabel = label(win, 'Operation (encode or decode) :', 'black', ('Times', 20), 40, 40)

encodeOrDecode = IntVar()
encodeOrDecode.set(1)
encodeButton = Radiobutton(win, text = "Encode", variable = encodeOrDecode, value = 1, font = ('Times', 16))
decodeButton = Radiobutton(win, text = "Decode", variable = encodeOrDecode, value = 2, font = ('Times', 16))
encodeButton.place(x = 50, y = 80)
decodeButton.place(x = 140, y = 80)

imageFileLabel = label(win, 'Image file used for settings :', 'black', ('Times', 20), 40, 120)

#imageFileTextInput = textInput(win, 3, 50, 160, 40)
#imageFileTextInputContents = StringVar()
#imageFileTextInputContents.set('')
#imageFileTextInput['textvariable'] = imageFileTextInputContents

filesInFolder = [f for f in os.listdir(folderPath + '/scytale') if os.path.isfile(os.path.join(folderPath + '/scytale', f))]
imagesInFolder = []
for i in range(len(filesInFolder)):
    file = filesInFolder[i].split('.')
    if file[1] == 'png':
        imagesInFolder.append(filesInFolder[i])
fileVariables = []
for i in range(len(imagesInFolder)):
    fileVariables.append(IntVar())

imageSelector = Combobox(win, values = imagesInFolder, state = 'readonly')
imageSelector.place(x = 50, y = 160)

messageLabel = label(win, 'Message to encode / decode :', 'black', ('Times', 20), 40, 200)

messageTextInput = textInput(win, 3, 40, 240, 150)
messageTextInputContents = StringVar()
messageTextInputContents.set('')
messageTextInput['textvariable'] = messageTextInputContents

enterButton = Button(win, text = ' Enter ', command = getContents, font = ('Times', 24))
enterButton.place(x = 75, y = 290)

messageLabel = label(win, 'Press ESC to quit', 'black', ('Times', 14), 30, 400)

win.bind('<Escape>', exit)

win.mainloop()