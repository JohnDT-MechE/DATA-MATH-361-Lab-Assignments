### Lab Assignment 1
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## MATH IS A LIBRARY THAT ALLOWS MATHEMATICAL FUNCTIONS AND NUMERICAL COMPUTATIONS TO BE PERFORMED
## PANDAS IS A LIBRARY USED FOR DATA MANIPULATION, ANALYSIS, AND DATA STRUCTURES
## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIHG-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## LOADS DATA FROM CSV INTO A VARIABLE
df = pd.read_csv('C:/Users/domj2/Learning Python/DATA-MATH-361-Lab-Assignments/Lab_Assignment_2/prevalence_of_anemia_in_pregnant_women.csv')

## SPECIFIES THE NAME OF THE COLUMN THAT CONTAINS SIGNIFICANT DATA
column_name = 'Prevalence of anemia among pregnant women (%)'

## STORES ALL DATA IN THE SPECIFIED COLUMN IN A VARIABLE
## DROPNA() ENSURES ANY NaN DATA VALUES ARE REMOVED
data = df[column_name].dropna()

## CALCULATES MEAN, MEDIAN, STANDARD DEVIATION, MAX, AND MIN VALUES
mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data, ddof = 1)
max_value = np.max(data)
min_value = np.min(data)

## PRINTS CALCULATED VALUES FOR MEAN, MEDIAN, STANDARD DEVIATION, MAX, AND MIN
## THE .2F ALLOWS FOR ONLY TWO DECIMAL PLACES TO BE SHOWN
print(f'Mean: {mean_value:.2f}')
print(f'Median: {median_value:.2f}')
print(f'Standard Deviation: {std_dev:.2f}')
print(f'Max: {max_value:.2f}')
print(f'Minimum: {min_value:.2f}')

## UNIVERSAL EQUATION USED TO DETERMINE BIN WIDTH IN STATISTICS
bin_width = (max_value - min_value) / math.sqrt(len(data))

## NUMPY FUNCTION THAT RETURNS EVENLY SPACED VALUES WITHIN A GIVEN INTERVAL
## CAN BE DEFINED AS (START, STOP, INTERVAL SIZE)
## MORE INFO AVAILABLE AT https://numpy.org/doc/2.1/reference/generated/numpy.arange.html
bin_edges = np.arange(min_value - bin_width, max_value + bin_width, bin_width)

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize=(8,6))

## CREATES A HISTOGRAM, DEFINES BINS, DEFINES COLOR OF BORDERS OF HISTOGRAM BARS, ALPHA CONTROLS THE TRANSPARENCY
plt.hist(data, bins = bin_edges, edgecolor = 'black', alpha = 0.7)

## ADDS TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.xlabel('Prevalence of Anemia in Pregnant Women 2019 (%)')
plt.ylabel('Number of Countries')
plt.title('Histogram of Prevalence of Anemia in Pregnant Women, 2019')

## CREATES HORIZONTAL GRID LINES
## ENABLES GRID LINES ONLY ALONG Y-AXIS (HORIZONTAL LINES), THE STYLE OF GRID LINES, AND ALPHA CONTROLS THEIR TRANSPARENCY
plt.grid(axis = 'y', linestyle = '--', alpha = 0.5)

## SHOWS THE PLOT IN THE FIGURE
plt.show()