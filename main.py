#Main file for the app
#Importing external libraries
import customtkinter as tk
from customtkinter import *


#Importing internal functions
from TkinterFunctions import uploadFile
from DataHandlingAndMath import handleData


#Creating App and App geometry, then canvas
Window = tk.CTk()
Window.geometry("800x550")
Window.title("Testy")

#Canvas creation
canvas = CTkCanvas(Window, width = 800, height = 550)
canvas.pack()




#Creating upload file button, Y entry, and Run Button
uploadButton = CTkButton(Window, text="Upload Data", command=uploadFile)
canvas.create_window(300, 450, window = uploadButton)

#Creating dependant variable or "y" entry for model to be trained on
dependantVariableGetter = CTkEntry(Window)
canvas.create_window(200,200, window = dependantVariableGetter)


#Creating run button
runButton = CTkButton(Window, text="Run", command = handleData)
canvas.create_window(500, 450, window = runButton)








#loop/pulling window to the front/disabling the ability to resize
Window.resizable(False, False)
Window.lift()
Window.mainloop()