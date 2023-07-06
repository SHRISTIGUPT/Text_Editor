import PySimpleGUI as sg
import io
import os

Thm = ["Black","Light Brown 1","Light Brown 2","Light Brown 3","Blue"]
sg.theme(Thm[1])

scriptPath = os.path.dirname(__file__)
firstTimeApp = 1
filename = scriptPath
currentSize = 11
currentFont = "Arial"

def about():
    sg.popup('This program is developed by Shristi Gupta.',title='Information', icon="favicon.ico")

def save(data):
    if filename != '':
        with io.open(filename, "w", encoding="utf8") as f:
            f.write(data)

def save_as(data):
    global filename
    filename = sg.tk.filedialog.asksaveasfilename(
        defaultextension='txt',
        filetypes=((" ALL TXT Files,", "*.txt"), ("All Files","*.*")),
        initialdir=scriptPath,
        title="Save as"
    )
    if filename != '':
        with io.open(filename, "w", encoding="utf8") as f:
            f.write(data)

def open_file():
    fileopen = sg.popup_get_file('file to open', no_window=True)
    if fileopen != '':
        with open(fileopen, "rt", encoding="utf8") as f:
            text = f.read()
        window['-text-'].update(value=text)
        window.TKroot.title(fileopen)

menu_def = [
    ['File', ['Open', 'Save', 'Save as', 'Close']],
    ['Edit', ['Font', ['Arial', 'Courier'], ['Size', ['8', '11', '15', '22']]]],
    ['About', ['Version']]
]

layout = [
    [sg.Menu(menu_def)],
    [sg.Multiline(size=(200, 100), font=('Arial',11), key="-text-")]
]

window = sg.Window("Text_Editor", layout,resizable=True, size=(600, 400),icon="favicon.ico")
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close':
        window.close()
        break

    if event == 'Courier':
        currentFont = 'Courier'
        font = ("Courier", currentSize)
        window["-text-"].update(font=font)
    
    if event == 'Arial':
        currentFont = 'Arial'
        font = ("Arial", currentSize)
        window["-text-"].update(font=font)

    if event == '8':
        currentSize = '8'
        font = (currentFont, '8')
        window["-text-"].update(font=font)
    
    if event == '11':
        currentSize = '11'
        font = (currentFont, '11')
        window["-text-"].update(font=font)

    if event == '15':
        currentSize = '15'
        font = (currentFont, '15')
        window["-text-"].update(font=font)
    
    if event == '22':
        currentSize = '22'
        font = (currentFont, '22')
        window["-text-"].update(font=font)

    if event == "Version":
        about()

    if event == "Save":
        if firstTimeApp == 0:
            save(values["-text-"])
        else:
            save_as(values["-text-"])
            firstTimeApp = 0

    if event == "Save as":
        save_as(values["-text-"])

    if event == "Open":
        open_file()