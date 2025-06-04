#This is where any 'commands' that aren't related to the data handling/math will lay
#I.e. uploading a file

#Importing external libraries
from tkinter import filedialog
import pandas as pd


#Declaring global var for datapath
dataFileLocation = None


#Creating upload file function
def uploadFile(runButton):

    #Printing that tool was opened
    print("File Selection Opened")

    #Globalizing dFL to be used across all the files
    #Setting filePath to none
    global dataFileLocation
    filePath = None

    # Opening your generic file upload window
    # and basic error handling, only opens if DFL doesnt have a path yet and to check if CSV has valid column amount >= 2
    if dataFileLocation is None:
        filePath = filedialog.askopenfilename(
            title="Select your CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )

        #Checking if there is a valid filePath (I.e. not "")
        #If so, check to see if it has the valid column amount
        #If it does, we filePath be assigned to that specific file, if not, we reject by saying file doesnt have valid amount of columns
        if filePath:
            temp = pd.read_csv(filePath)
            if len(temp.columns) >= 2:
                temp = filePath
                dataFileLocation = filePath
                #Letting run button be.. ran
                runButton.configure(state = "normal")
            else:
                print("File does not have valid amount of columns")
        else:
            print("No File Selected")

