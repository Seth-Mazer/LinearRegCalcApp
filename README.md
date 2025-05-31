No fancy preview yet.

As of this current bare-bones readme 5/30/2025,
All math works correctly, and prints both the Regression Equation and Coefficient of Determination to the terminal
This is a linear model, using lienar regression. It will work for n features.

As of this current draft, you can indeed select any CSV, and assuming all rows are numerical, calculate your yHat/reg equation and CoD based on the rest of the columns.
However, GUI implementation is wonky right now. You can click upload to upload, and you can run.

Current caveats:
🚫 Delightful Looking Gui
🚫 3D Chart with Regression Plane for only 2 features (indep. variables)
🚫 2D Chart with typical scatter plot for only 1 feature
🚫 Error handling to only print Reg Eq and CoD when there is more than 3 features
🚫 Error handling to make sure all columns within the CSV are numerical (May not matter.. will look into.. It may depend)
🚫 **Proper Y Entry field** *In order to determine what data you want your model to be able to predict, I.e. the column, as of this current readme, you must specify directly
within the DataHandalingAndMath.py. Look for the variable dependantVarColumn, and set it to the number column you want, or the name. (Case sensitive and ignore 0 index)
🚫 Built Executable


