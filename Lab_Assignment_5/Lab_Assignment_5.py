### Lab Assignment 5
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIHG-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
import numpy as np
import matplotlib.pyplot as plt

## DEFINES POPULATION AND SAMPLE PARAMETERS
population_size = 100000        ## CREATES LARGE POPULATION SIZE
support_percentage = 0.55       ## SETS SUPPORT FOR POLICY AT 55%
sample_size = 100               ## DEFINES SAMPLE SIZE AS 100
num_samples = 1000              ## DEFINES NUMBER OF SAMPLES TO TAKE

## CREATES A RANDOMIZED POPULATION USING NP.RANDOM.CHOICE() BASED ON DEFINED POPULATION PARAMETERS
## IN THIS CASE, 1 IS TRUE (OR SUPPORT POLICY) AND 2 IS FALSE (OR DOES NOT SUPPORT POLICY)
population = np.random.choice([1, 0], size = population_size, p = [support_percentage, 1 - support_percentage])

## COLLECTS RANDOM SAMPLES FROM THE POPULATION CREATED IN THE PREVIOUS STEP AND CALCULATES SAMPLE PROPORTIONS
sample_proportions = [
    np.mean(np.random.choice(population, size = sample_size, replace = True))
    for _ in range(num_samples)
]

## CALCULATES THE MEAN PROPORTION AND STANDARD ERROR FROM THE SAMPLES TAKEN
mean_proportion = np.mean(sample_proportions)
standard_error = np.std(sample_proportions, ddof=1)

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize = (10, 6))

## CREATES A HISTOGRAM FROM SAMPLE PROPORTIONS, DEFINES BINS, DEFINES COLOR OF BORDERS OF HISTOGRAM BARS, ALPHA CONTROLS THE TRANSPARENCY
plt.hist(sample_proportions, bins = 30, edgecolor = 'black', alpha = 0.7)

## ADDS A VERTICAL LINE AT THE CALCULATED MEAN_PROPORTION VALUE, SETS THE COLOR TO RED, SETS THE LINETYPE TO DASHED, DEFINES LINE WIDTH, AND ADDS A LABEL TO BE INCLUDED IN THE LEGEND
plt.axvline(mean_proportion, color = 'red', linestyle = 'dashed', linewidth = 2, label = f'Mean: {mean_proportion:.4f}')

## ADDS A TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.xlabel('Sample Proportion of Support')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Proportions for UBI Support')

## ADDS A LEGEND TO THE FIGURE
plt.legend()

## SHOWS THE PLOT IN THE FIGURE
plt.show()

## PRINTS THE CALCULATED MEAN PROPORTION AND STANDARD ERROR FROM THE SIMULATED POPULATION
print('Activity 1:\n')
print(f'Simulated Mean Proportion: {mean_proportion:.4f}')
print(f'Simulated Standard Error: {standard_error:.4f}')


### Activity 2

## IMPORTS ESSENTIAL LIBRARIES
## MATH IS A LIBRARY THAT ALLOWS MATHEMATICAL FUNCTIONS AND NUMERICAL COMPUTATIONS TO BE PERFORMED
import math

## DEFINES POPULATION AND SAMPLE PARAMETERS
population_size = 100000
support_percentage = 0.55
sample_size = 100

## SETS NECESSARY PARAMETERS TO VARIABLES USED IN THEORETICAL CALCULATIONS FOR EASE OF UNDERSTANDING
p = support_percentage
n = sample_size

## CALCULATES MEAN PROPORTION AND STANDARD ERROR USING THE THEORETICAL MODEL
mean_proportion = p
standard_error = math.sqrt((p * (1 - p)) / n)

## PRINTS THE CALCULATED MEAN PROPORTION AND STANDARD ERROR FROM THEORETICAL CALCULATIONS
print('Activity 2:\n')
print(f'Theoretical Mean Proportion: {mean_proportion:.4f}')
print(f'Theoretical Standard Error: {standard_error:.4f}')
