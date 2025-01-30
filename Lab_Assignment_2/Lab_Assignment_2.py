### Lab Assignment 1
### John Dominguez-Trujillo

### Activity 1

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/domj2/Learning Python/DATA-MATH-361-Lab-Assignments/Lab_Assignment_2/prevalence_of_anemia_in_pregnant_women.csv')

column_name = 'Prevalence of anemia among pregnant women (%)'

data = df[column_name].dropna()


mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data, ddof = 1)
max_value = np.max(data)
min_value = np.min(data)


print(f'Mean: {mean_value:.2f}')
print(f'Median: {median_value:.2f}')
print(f'Standard Deviation: {std_dev:.2f}')
print(f'Max: {max_value:.2f}')
print(f'Minimum: {min_value:.2f}')

bin_width = (max_value - min_value) * math.sqrt(len(data))

bin_edges = np.arange(min_value - bin_width, max_value + bin_width, bin_width)

plt.figure(figsize=(8,6))
plt.hist(data, bins = bin_edges, edgecolor = 'black', alpha = 0.7)


plt.xlabel('Prevalence of Anemia in Pregnant Women 2019(%)')
plt.ylabel('Number of Countries')
plt.title('Histogram of Prevalence of Anemia in Pregnant Women, 2019')

plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)

plt.show()