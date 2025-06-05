#Here is where all the plot logic will go

#Importing external libraries
import matplotlib.pyplot as plt
import numpy as np


def plot(intercept, coefficients, features, CoD, yHat, y, xMatrix, model, df, dependantVarColumn):

    # Plotting data only if there are either 1 OR 2 features. Else, well, we dont do anything
    if len(coefficients) == 1:
        print("e")
    elif len(coefficients) == 2:

        #Grabbing all the feature data from the 2 xMatrix columns.
        x1 = xMatrix.iloc[:, 0]
        x2 = xMatrix.iloc[:, 1]

        #Creating a meshgrid for our regression plane, using the bounds of each column
        xRange = np.linspace(x1.min(), x1.max(), 50)
        xRangeTwo = np.linspace(x2.min(), x2.max(), 50)
        #Creating grid of all vals
        xGrid, xGridTwo = np.meshgrid(xRange, xRangeTwo)

        #Compressing both grids into 1D arrays
        xFlat = xGrid.ravel()
        xFlatTwo = xGridTwo.ravel()

        # Making both into a new matrix, like, xOne1,xOne1,xOne1,xOne1,infinity... xTwo1,xTwo2,xTwo3,xTwo4, etc.
        # Until xOne2,xOne2,xOne2,infinity, xTwo1,xTwo2,xTwo3, etc.
        gridInput = np.column_stack((xFlat, xFlatTwo))

        #Generating a new yHat, because now were using the new matrix created from the grids
        #and then using that as he matrix for the normal equation,
        #as in gridInput is now our X in X in β̂ = (XᵗX)⁻¹ Xᵗy
        finalYHat = model.predict(gridInput)

        # Creating the regression plane. We are using the shape of xGrid to make sure
        # That Y grid has the same dimensions as the xGrid
        yGrid = finalYHat.reshape(xGrid.shape)

        #Plotting Regression Plane
        # Creating a figure with a width and height of 10 and 7
        fig = plt.figure(figsize=(10, 7))
        # Forcing 3D projection, creating only 1 plot
        chart = fig.add_subplot(111, projection='3d')

        # Creating scatter plot, using the xyz variables, with the plasma color gradient and a dot size of 60
        scatter = chart.scatter(x1, x2, y, c=y, cmap='Blues', s=60)

        # Plotting the regression plane
        chart.plot_surface(xGrid, yGrid, xGridTwo, alpha=0.9, color='red')

        # Creating the axes labels
        chart.set_xlabel(xMatrix.columns[0])
        chart.set_ylabel(xMatrix.columns[1])
        chart.set_zlabel(dependantVarColumn)


        # Adjusting view
        chart.view_init(elev=40, azim=195)

        #Creating title and saving image
        plt.title("3D Linear Regression with Regression Plane")
        plt.savefig("regression_plot.png")  # Saves to file

        return fig





#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     else:
#         print("Invalid amount of features, cannot plot past 3D")


















