# Main.py
# Entry for DeltaHacks V
# Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

import warnings 
warnings.filterwarnings("ignore", category=UserWarning)
# Ignores Warning from higher version of pickle

import PySimpleGUI as sg

from Confusion import *
from DataFrame import genDataFrame
from FileIO import *
from Process import *

def main():
    targetDialogue = [
        [sg.Text("Select the type of image to measure:", size=(35, 1))], 
        [sg.Radio("Standard", "Target", default=True)],
        [sg.Radio("With Particles", "Target", default=False)],
        [sg.Radio("Poor Lighting + Particles", "Target", default=False)],
        [sg.Radio("Testing with New Inputs", "Target", default=False)],
        [sg.CloseButton("Select")]
    ]

    targetWindow = sg.Window('Graynne').Layout(targetDialogue)
    button, values = targetWindow.Read()

    target = values.index(True) + 1 # to be used to determine pickle file

    if target == 4:
        targetDataDialogue = [
            [sg.Text("Select the target database to utilize:", size=(35, 1))], 
            [sg.Radio("Standard", "Target", default=True)],
            [sg.Radio("With Particles", "Target", default=False)],
            [sg.Radio("Poor Lighting + Particles", "Target", default=False)],
            [sg.CloseButton("Select")]
        ]

        targetDataWindow = sg.Window('Graynne').Layout(targetDataDialogue)
        button, values = targetDataWindow.Read()

        targetData = values.index(True) + 1 # to be used to determine pickle file
    else:
        targetData = target

    fileName = "Select File"
    while fileName == "Select File":
        fileDialogue = [      
            [sg.Text("Choose an Input File", size=(35, 1))], 
            [sg.Text("Input File", size=(15,1), auto_size_text=False, justification="right"),
             sg.InputText("Select File"), sg.FileBrowse()],     
            [sg.CloseButton("Select"), sg.CloseButton("Cancel")]
        ]
        
        fileWindow = sg.Window('Graynne').Layout(fileDialogue)
        button, values = fileWindow.Read()

        fileName = values[0]
        if fileName == "Select File" and button == "Select":
            wrongDialogue = [
                [sg.Text("You must specify a file path.")],
                [sg.CloseButton("OK")]
            ]

            wrongWindow = sg.Window('Graynne').Layout(wrongDialogue)
            button = wrongWindow.Read()
        elif button == "Cancel":
            exit()

    if fileName[-6] == "_":
        num = int(fileName[-5])
        outPath = fileName[:-40]
    elif fileName[-7] == "_":
        num = int(fileName[-6:-4])
        outPath = fileName[:-41]
    elif fileName[-8] == "_":
        num = int(fileName[-7:-4]) 
        outPath = fileName[:-42]
    else:
        raise Exception("Image number not in expected format.")

    shortFile = "image_" + str(num)
    
    logmodel    = genLogModel(targetData)
    predictions = genPredictions(fileName, logmodel)

    fractionDark = writeGraynne(predictions)

    outString = "The fraction of dark phase in {} is {:.5}, and the output has been written to: \n".format(shortFile, fractionDark)
    outFile   =  outPath + "DeltaHacks V/src/output.png"
    outDialogue = [
        [sg.Text(outString + outFile)],
        [sg.CloseButton("OK")]
    ]

    outWindow = sg.Window('Graynne').Layout(outDialogue)
    button = outWindow.Read()

main()