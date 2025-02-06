### Lab Assignment 3
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## PANDAS IS A LIBRARY USED FOR DATA MANIPULATION, ANALYSIS, AND DATA STRUCTURES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
import pandas as pd
import matplotlib.pyplot as plt

## LOADS DATA FROM CSV INTO A VARIABLE
## USING A URL THAT LINKS DIRECTLY TO THE CSV FILE IN MY GITHUB SO ANYONE CAN ACCESS IT
url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/2b392369cdfa92927b351f6f749aca9cbd02a60d/Lab_Assignment_3/TwoWayTableOSS_MS.csv'
df = pd.read_csv(url)

## DROPNA() ENSURES ANY NaN DATA VALUES ARE REMOVED
df = df.dropna()

## SETS THE FIRST COLUMN OF THE DATAFRAME AS THE INDEX
## THIS ACTS AS THE LABELS FOR THE ROWS OF THE DATAFRAME
df.set_index(df.columns[0], inplace = True)

## TRANSPOSES THE DATA FOR PLOTTING
df = df.T

## CONVERTS NUMBER OF STUDENTS TO PERCENTAGE OF STUDENTS FOR BOTH SUSPENDED AND NOT SUSPENDED
df_percent = df.div(df.sum(axis = 1), axis = 0) * 100

# Create a figure (fig) and an axes (ax) using Matplotlib
# - `fig`: The entire figure or canvas where everything (subplots, titles, legends, etc.) is drawn.
# - `ax`: A single subplot (or axes) within the figure where the data is plotted.
# - `plt.subplots()` returns both the figure and axes objects, allowing explicit control over the plot.
# - `figsize=(10, 6)` sets the size of the figure in inches:
#    * 10 is the width, and 6 is the height of the figure.
## CREATES A FIGURE AND AN AXES
## FIG DEFINES A FIGURE WHERE A PLOT IS DRAWN
## AX DEFINES A SINGLE SUBPLOT WITHIN THE FIGURE WHERE THE DATA WILL BE PLOTTED
## PLT.SUBPLOT() RETURNS THE FIGURE AND AXES OBJECTS THAT ALLOWS FOR CONTROL OF THE PLOT
## FIGSIZE SETS THE SIZE OF THE FIGURE
fig, ax = plt.subplots(figsize = (10,6))

## PLOTS THE PERCENTAGE OF STUDENTS SUSPENDED AND NOT SUSPENDED AS A STACKED BAR PLOT
df_percent.plot(kind = 'bar', stacked = True, ax = ax)

## ADDS TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.title('Mississippi School Suspensions Based on Race')
plt.xlabel('Race')
plt.ylabel('Percentage of Students')

## ROTATES THE LABELS ON THE X-AXIS BY 45 DEGREES
plt.xticks(rotation = 45)

## ADDS A LEGEND TO THE FIGURE AND SPECIFIES ITS EXACT LOCATION ON THE FIGURE
plt.legend(title = 'Suspension Status', bbox_to_anchor = (1.05, 1), loc = 'upper left')

## LIMITS THE Y-AXIS TO 100
plt.ylim(0,100)

## MATPLOTLIB FUNCTION THAT IS USED TO AUTOMATICALLY ADJUST SPACING BETWEEN PLOT ELEMENTS
## ENSURES THAT NO OVERLAPPING OR CLIPPING ISSUES OCCUR
plt.tight_layout()

## SHOWS THE PLOT IN THE FIGURE
plt.show()


### Activity 2

## IMPORTS ESSENTIAL LIBRARIES
## PANDAS IS A LIBRARY USED FOR DATA MANIPULATION, ANALYSIS, AND DATA STRUCTURES
import pandas as pd

## LOADS DATA FROM CSV INTO A VARIABLE
## USING A URL THAT LINKS DIRECTLY TO THE CSV FILE IN MY GITHUB SO ANYONE CAN ACCESS IT
url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/2b392369cdfa92927b351f6f749aca9cbd02a60d/Lab_Assignment_3/Titanic.csv'
df = pd.read_csv(url)


outcome_table = df.pivot_table(
    index = ['Class', 'Sex'], 
    columns = 'Outcome', 
    aggfunc = 'size', 
    fill_value = 0
)

#total_table = df. pivot_table(
    #index = ['Class', 'Sex'],
    #aggfunc = 'size'
    #fill_value = 0
#)


print(outcome_table)
#print(total_table)