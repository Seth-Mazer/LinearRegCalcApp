No fancy preview yet.

As of this current bare-bones readme 6/05/2025,
All math works correctly, and prints both the Regression Equation and Coefficient of Determination to the terminal
This is a linear model, using lienar regression. It will work for n features.

As of this current draft, you can indeed select any CSV, and assuming all rows/columns are numerical data, calculate your yHat/reg equation and CoD based on the rest of the columns.
Now, we also can see a visual 3D plot, for 2 features. Its rough, but its getting there.

**Update 6-05-2025** Rough In-App plotting mechanics have been added. Users can now actively see their 3D graph after uploading a CSV with only 3 columns. Y, X1, X2. 
Also added some labeling for errors, like when the user 

Current caveats:
- 🚫 Delightful Looking Gui
- 🚫 2D Chart with typical scatter plot for only 1 feature
- 🚫 Error handling to only print Reg Eq and CoD when there is more than 3 features
- 🚫 Error handling to make sure all columns within the CSV are numerical (May not matter.. will look into.. It may depend)
- 🚫 Built Executable


