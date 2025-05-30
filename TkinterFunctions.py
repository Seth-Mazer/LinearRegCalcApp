#This is where any 'commands' that aren't related to the data handling/math will lay
#I.e. uploading a file

#Importing filedialog to allow user file "grabbing"
from tkinter import filedialog

#Declaring global var for datapath
dataFileLocation = None
uploadedFile = False


#Creating upload file function
def uploadFile():

    global dataFileLocation

    # Opening your generic file upload window
    #and basic error handling, only opens if DFL doesnt have a path yet
    if dataFileLocation is None:
        filePath = filedialog.askopenfilename(
            title="Select your CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        dataFileLocation = filePath
    if filePath:
        dataFileLocation = filePath
    #Returning the CSV's path
    return
