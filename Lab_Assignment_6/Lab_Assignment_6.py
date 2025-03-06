### Lab Assignment 6
### John Dominguez-Trujillo

### Activity 1 and Activity 2

## IMPORTS ESSENTIAL LIBRARIES
## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIGH-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
import numpy as np
import matplotlib.pyplot as plt

## DEFINES POPULATION PARAMETERS
mu = 98.2       ## MEAN BODY TEMPERATURE
sigma = 0.73    ## STANDARD DEVIATION

## DEFINES SAMPLE PARAMETERS
num_samples = 1000  ## NUMBER OF SAMPLES
sample_size = 100   ## SAMPLE SIZE

## GENERATES SAMPLE MEANS FROM THE DEFINED POPULATION AND SAMPLE PARAMETERS
sample_means = [
    np.mean(np.random.normal(mu, sigma, sample_size))
    for _ in range(num_samples)
]

## SELECTS ONE RANDOM SAMPLE
random_sample = np.random.normal(mu, sigma, sample_size)

## COMPUTES THE SAMPLE MEAN AND STANDARD DEVIATION OF THE RANDOM SAMPLE
sample_mean = np.mean(random_sample)
sample_std = np.std(random_sample, ddof=1)

## DEFINES THE Z-SCORE FOR THE 95% CONFIDENCE INTERVAL
z_critical = 1.96

## CALCULATES THE MARGIN OF ERROR BY MULTIPLYING THE STANDARD ERROR BY THE DEFINED Z-SCORE FOR THE 95% CONFIDENCE INTERVAL
margin_of_error_z = z_critical * (sample_std / np.sqrt(sample_size))

## COMPUTES THE LOWER AND UPPER VALUES OF THE 95% CONFIDENCE INTERVAL
confidence_interval_z = (sample_mean - margin_of_error_z, sample_mean + margin_of_error_z)

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize=(10, 6))

## CREATES A HISTOGRAM FROM THE SAMPLE_MEANS, DEFINES BINS, DEFINES COLOR OF BORDERS OF HISTOGRAM BARS, ALPHA CONTROLS THE TRANSPARENCY
plt.hist(sample_means, bins=30, edgecolor='black', alpha=0.7)

## ADDS A VERTICAL LINE AT THE CALCULATED SAMPLE_MEAN VALUE, SETS THE COLOR TO BLUE, SETS THE LINETYPE TO DASHED, DEFINES LINE WIDTH, AND ADDS A LABEL TO BE INCLUDED IN THE LEGEND
plt.axvline(sample_mean, color='blue', linestyle='dashed', linewidth=2, label=f'Random Sample Mean: {sample_mean:.2f}')

## ADDS A VERTICAL LINE AT THE CALCULATED LOWER 95% CONFIDENCE INTERVAL VALUE, SETS THE COLOR TO RED, SETS THE LINETYPE TO DASHED, DEFINES LINE WIDTH, AND ADDS A LABEL TO BE INCLUDED IN THE LEGEND
plt.axvline(confidence_interval_z[0], color='red', linestyle='dashed', linewidth=2, label=f'95% CI Lower: {confidence_interval_z[0]:.2f}')

## ADDS A VERTICAL LINE AT THE CALCULATED UPPER 95% CONFIDENCE INTERVAL VALUE, SETS THE COLOR TO GREEN, SETS THE LINETYPE TO DASHED, DEFINES LINE WIDTH, AND ADDS A LABEL TO BE INCLUDED IN THE LEGEND
plt.axvline(confidence_interval_z[1], color='green', linestyle='dashed', linewidth=2, label=f'95% CI Upper: {confidence_interval_z[1]:.2f}')

## ADDS A TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.xlabel('Sample Mean Temperature (°F)')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Mean Body Temperatures with 95% CI Using Z-Scores')

## ADDS A LEGEND TO THE FIGURE
plt.legend()

## SHOWS THE PLOT IN THE FIGURE
plt.show()

## PRINTS THE SAMPLE MEAN AND 95% CONFIDENCE INTERVAL
print(f'Sample Mean: {sample_mean:.2f}°F')
print(f'95% Confidence Interval: ({confidence_interval_z[0]:.2f}, {confidence_interval_z[1]:.2f})')
