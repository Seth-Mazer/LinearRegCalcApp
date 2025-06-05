#Main file for the app
#Importing external libraries
import customtkinter as tk
from customtkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg


#Importing internal functions
from TkinterFunctions import uploadFile
from DataHandlingAndMath import handleData
from Plotting import plot



#Creating App and App geometry, then canvas
Window = tk.CTk()
Window.geometry("800x550")
Window.title("Testy")

#Canvas creation
canvas = CTkCanvas(Window, width = 800, height = 550)
canvas.pack()

#Creating a plot widget variable so we can reference it later on
plotWidget = None

#Creating upload file button, Y entry, and Run Button
uploadButton = CTkButton(Window, text="Upload Data", command=lambda: uploadFile(statusText, runButton))
canvas.create_window(200, 450, window = uploadButton)


#Creating dependant variable or "y" entry field for model to be trained on
dependantVariableGetter = CTkEntry(Window)
canvas.create_window(400,450, window = dependantVariableGetter)


#Creating a function handle getting the data from dVG because we don't want to call get immediately and pass a null like data type
def handleRun():
    #Passing the dependant variable column
    dVGEntry = dependantVariableGetter.get()
    results = handleData(dVGEntry)

    #Generating the plot figure using the returned values from the data handling
    fig = plot(*results)

    #If a figure exists, call the display function
    if fig:
        displayPlot(fig)




#Creating run button and setting its state to disabled, so the user cant run the program without a valid file
runButton = CTkButton(Window, text="Run", command = handleRun)
canvas.create_window(600, 450, window = runButton)
runButton.configure(state="disabled")



#Status label for the GUI
statusText = CTkLabel(Window, text="", text_color="red")
canvas.create_window(200, 480, window = statusText)



#Displaying the chart onto the screen
def displayPlot(fig):
    #Globalizing the plotWidget so we can always make sure we do or dont already have a widget
    global plotWidget

    #If a plot already exits, destroy it
    if plotWidget:
        plotWidget.destroy()

    #Embedding the plotted figure into the main window
    plotCanvas = FigureCanvasTkAgg(fig, master=Window)
    plotCanvas.draw()

    #Were getting the weidget from the canvas
    #Essentially this makes our canvas a genuine widget, no different from a label or button
    plotWidget = plotCanvas.get_tk_widget()

    #Placing the chart on the screen
    canvas.create_window(400,210, anchor="center", window = plotWidget)





#loop/pulling window to the front/disabling the ability to resize
Window.resizable(True, True)
Window.lift()
Window.mainloop()


