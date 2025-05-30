#This is where all pandas/numpy/matplotlib code will be stored

#Importing external libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Importing internal data/stuffs

#Well, all the data handling!
def handleData():

    #Getting the CSV's location
    from TkinterFunctions import dataFileLocation
    print("here is da path: ", dataFileLocation)


    #Reading the csv data and storing it as df
    df = pd.read_csv(dataFileLocation)

    #The users input for the yColumn/dep var
    dependantVarColumn = 2

    #Checking if the entry field was either an integer, or a string.
    #If not string check if integer if not return error
    if not isinstance(dependantVarColumn, str):
        try:
            isinteger = isinstance(dependantVarColumn, int)
            #If it's an integer, the yColumn (the column that will be dropped), will be dVC - 1, because CSVs are 0-indexed
            yColumn = df.columns[dependantVarColumn - 1]
            print(yColumn)
        except:
            print("Error, neither string nor column index")
    else:
        #Otherwise use the column name given by the user
        yColumn = dependantVarColumn
        print(yColumn)

    #From this point forward I will refer to the yColumn as the Dependant Variable or related terminolog for the given context

    # Since .fit() uses LSR in the form of the Normal Equation, we will now define
    # what the X matrix will be, and define Y, for β̂ = (XᵗX)⁻¹ Xᵗy

    #Setting y to the column dropped, so, whatever the user wanted the dep variable to be
    y = df[yColumn]
    df = df.drop(yColumn, axis = 1) #Then dropping, since we don't want the dependant variables in our X matrix

    #Defing x Matrix
    xMatrix = df

    #Printing to make sure we got the correct stuff! Heh! That wouldn't be too great if we didn't have numbers!
    print(xMatrix)
    print("Break")
    print(y)

    #"Declaring our model to be of the LinReg "type"
    #yhat = b0 + b1(x1) + b2(x2) ..... bn(xn)
    model = LinearRegression()
    #We are now determining the regression equation via LSR, by using the Normal Equation
    #This will essentially, calculate the best values that fit into b0 b1 bn, by minimizing loss using the above
    model.fit(xMatrix,y)

    #Now we are generating yHat, aka the regression equation based on what was "fit" into the model.
    yHat = model.predict(xMatrix)

    # Generating our coefficient of determination aka R^2. Via R = 1 - RSS/TSS
    # So basically, we are calcualting R^2 by calculating both the residual sum of squares and total sum of squares
    # RSS = Σ(yi - yhat)^2 and TSS = Σ(yi - ȳ)^2, with y being every data value in the y column, and yhat being our equation, and y not being our
    # mean of y
    #In broad terms, we are comparing our predictions with yhat, to the actual values of y, which returns this number.
    CoD = r2_score(y, yHat)

    #Declaring our coefficients array and declaring the intercept
    coefficients = model.coef_
    intercept = model.intercept_


    #Generating and printing the regression equation

    #Grabbing our x1,x2.. xn names for our x's via the column names
    features = xMatrix.columns

    #Iterating over .coefficients, grabbing the float values, and tying them to the corresponding feature
    #Rounding coefs to 3
    terms = [f"{round(coef, 3)}*{feature}" for coef, feature in zip(coefficients, features)]
    #Genearting equation by printing the y = intercept, then basically putting all the coefficients
    #next to b0
    equation = f"y = {round(intercept, 3)} + " + " + ".join(terms)
    #Printing
    print(equation)
    #Printing Coeff of Det.
    print(round(CoD,5))






