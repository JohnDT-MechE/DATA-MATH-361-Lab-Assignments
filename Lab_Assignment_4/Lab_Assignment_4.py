### Lab Assignment 4
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIHG-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
## SCIPY.STATS IS A SCIPY LIBRARY THAT PROVIDES VARIOUS STATISTICAL FUNCTIONS SUCH AS PROBABILITY DISTRIBUTIONS, STATISTICAL TESTS, AND DESCRIPTIVE STATISTICS
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

## SETS GIVEN MEAN AND STANDARD DEVIATION TO DEFINE NORMAL DISTRIBUTION
mean = 66
std_dev = 2

## DEFINES THE GREATER THAN AND LESS THAN SPEED VALUES FOR PROBABILITY CALCULATIONS
greater_than_speed = 70
less_than_speed = 60

## CREATES THE X-AXIS BY CREATING AN ARRAY OF 1000 EVENLY SPACED NUMBERS FROM 4 STANDARD DEVIATIONS BELOW THE MEAN TO 4 STANDARD DEVIATIONS ABOVE THE MEAN
## IN THIS CASE THE ARRAY WILL HAVE 1000 EVENLY SPACED NUMBERS FROM 58 TO 74
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)

## COMPUTES THE PROBABILITY DENSITY FUNCTION FOR EACH X FOR GIVEN NORMAL DISTRIBUTION
y = stats.norm.pdf(x, mean, std_dev)

## CALCULATES PROBABILITY OF SPEED BEING GREATER THAN DEFINED GREATER THAN SPEED
## SUBTRACTS STATS.NORM.CDF FROM 1 DUE TO THE WAY THE FUNCTION WORKS
## STATS.NORM.CDF GETS PROBABILTIY THAT VALUE LIES BETWEEN -INFINITY AND SPECIFIED VALUE (LEFT SIDE OF VALUE) A.K.A. PROBABILITY THAT SPEED IS LESS THAN OR EQUAL TO SPECIFIED VALUE
## SUBTRACT FROM 1 TO GET THE RIGHT SIDE A.K.A. PROBABILITY THAT THE SPEED IS GREATER THAN OR EQUAL TO SPECIFIED VALUE
prob_greater_than = 1 - stats.norm.cdf(greater_than_speed, mean, std_dev)

## CALCULATES PROBABILITY OF SPEED BEING LESS THAN DEFINED LESS THAN SPEED
prob_less_than = stats.norm.cdf(less_than_speed, mean, std_dev)

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize = (8, 5))

## PLOTS X AND Y VALUES ON FIGURE, LABELS THE PLOTTED DATA, SETS COLOR TO BLUE
plt.plot(x, y, label = 'Normal Distribution of Speed', color = 'blue')


x_fill_greater = np.linspace(greater_than_speed, mean + 4 * std_dev, 500)
y_fill_greater = stats.norm.pdf(x_fill_greater, mean, std_dev)
plt.fill_between(x_fill_greater, y_fill_greater, alpha = 0.5, color = 'red', label = f'P(X > {greater_than_speed}) = {prob_greater_than:.4f}')

x_fill_less = np.linspace(mean - 4 * std_dev, less_than_speed, 500)
y_fill_less = stats.norm.pdf(x_fill_less, mean, std_dev)
plt.fill_between(x_fill_less, y_fill_less, alpha = 0.5, color = 'green', label = f'P(X < {less_than_speed}) = {prob_less_than:.4f}')

plt.axvline(greater_than_speed, color = 'red', linestyle = 'dashed', label = f'X = {greater_than_speed}')
plt.axvline(less_than_speed, color = 'green', linestyle = 'dashed', label = f'X = {less_than_speed}')
plt.xlabel('Speed (mph)')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of Speed with Probabilities')
plt.legend()
plt.grid()

plt.show()

print(f'Probability of speed > {greater_than_speed} mph: {prob_greater_than:.4f}')
print(f'Probabiltiy of speed < {less_than_speed} mph: {prob_less_than:.4f}')


### Activity 2

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mean_speed = 66  # mph
std_dev = 2  # mph

greater_than_speed = 70
less_than_speed = 60

prob_greater_than = 1 - stats.norm.cdf(greater_than_speed, mean_speed, std_dev)
prob_less_than = stats.norm.cdf(less_than_speed, mean_speed, std_dev)

x_cdf = np.linspace(mean_speed - 4 * std_dev, mean_speed + 4 * std_dev, 1000)
y_cdf = stats.norm.cdf(x_cdf, mean_speed, std_dev)

plt.figure(figsize=(8, 5))
plt.plot(x_cdf, y_cdf, label="Cumulative Distribution Function", color='blue')

plt.axvline(greater_than_speed, color='red', linestyle='dashed', label=f'X = {greater_than_speed}')
plt.scatter(greater_than_speed, stats.norm.cdf(greater_than_speed, mean_speed, std_dev), color='red', zorder=3)
plt.text(greater_than_speed, stats.norm.cdf(greater_than_speed, mean_speed, std_dev) - 0.05,
         f'P(X > {greater_than_speed}) = {prob_greater_than:.4f}', color='red', ha='right')

plt.axvline(less_than_speed, color='green', linestyle='dashed', label=f'X = {less_than_speed}')
plt.scatter(less_than_speed, stats.norm.cdf(less_than_speed, mean_speed, std_dev), color='green', zorder=3)
plt.text(less_than_speed, stats.norm.cdf(less_than_speed, mean_speed, std_dev) + 0.02,
         f'P(X < {less_than_speed}) = {prob_less_than:.4f}', color='green', ha='right')

plt.xlabel("Speed (mph)")
plt.ylabel("Cumulative Probability")
plt.title("Cumulative Distribution Function (CDF) of Speed")
plt.legend()
plt.grid()

plt.show()

print(f"Probability of speed > {greater_than_speed} mph: {prob_greater_than:.4f}")
print(f"Probability of speed < {less_than_speed} mph: {prob_less_than:.4f}")
