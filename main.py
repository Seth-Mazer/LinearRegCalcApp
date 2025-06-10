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
Window.title("Linear Regression Calculator")

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

    if len(results[1]) <= 2:
        # Generating the plot figure using the returned values from the data handling
        fig = plot(*results)

        # Grabbing equation
        regEquation = results[10]

        # Grabbing CoD, Im aware im defaulting to CoD (Coeff. of Determination) for the var, but in reality
        # It doesn't matter at all, because we know that itll automatically be the Correlation Coefficient for any CSV with features = 1
        # and a Coeff of Determiation for any CSV with features > 1
        CoD = results[3]
        CoD = round(CoD, 6)

        # If a figure exists, call the display function
        if fig:
            displayPlot(fig, regEquation, CoD)
    else:
        #If there are more than 2 features, we will just print the regression equation
        #Major thing here is that with multiple features its very possible the model will be overfit, thus resulting
        #In an r^2 = 1 or even > 1. I
        print(len(results[1]))
        print(len(results[1]) < 2)
        regEquation = results[10]
        CoD = results[3]
        CoD = round(CoD, 6)

        # Creating Labels for both Regression Equation, and either the Coeff (R or R^2)
        equationText = CTkLabel(Window, text=regEquation)
        canvas.create_window(400, 220, window=equationText)

        # Coeff of x label
        eitherCoeff = CTkLabel(Window, text=f"R^2 = {CoD}")
        canvas.create_window(400, 265, window=eitherCoeff)

        #Stating that since there are more than 2 features, a chart is not possible
        statusText.configure(text="⚠️ Dataset has more than 2 features, Chart not possible")




#Creating run button and setting its state to disabled, so the user cant run the program without a valid file
runButton = CTkButton(Window, text="Run", command = handleRun)
canvas.create_window(600, 450, window = runButton)
runButton.configure(state="disabled")



#Status label for the GUI
statusText = CTkLabel(Window, text="", text_color="red")
canvas.create_window(200, 480, window = statusText)



#Displaying the chart onto the screen
def displayPlot(fig, regEquation, CoD):
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

    #Creating Labels for both Regression Equation, and either the Coeff (R or R^2)
    equationText = CTkLabel(Window, text = regEquation)
    canvas.create_window(200,510, window=equationText)

    #Coeff of x label
    eitherCoeff = CTkLabel(Window, text=f"R^2 = {CoD}")
    canvas.create_window(600,510, window = eitherCoeff)





#loop/pulling window to the front/disabling the ability to resize
Window.resizable(False, False)
Window.lift()
Window.mainloop()


