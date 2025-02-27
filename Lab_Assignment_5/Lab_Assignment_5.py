### Lab Assignment 5
### John Dominguez-Trujillo

### Activity 1

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
population_size = 100000  # Large population
support_percentage = 0.55  # 55% support the policy
sample_size = 100  # Each sample contains 100 individuals
num_samples = 1000  # Number of samples to draw

# Create a population (1 represents support, 0 represents opposition)
population = np.random.choice([1, 0], size=population_size, p=[support_percentage, 1 - support_percentage])

# Collect samples and calculate proportions
sample_proportions = [
    np.mean(np.random.choice(population, size=sample_size, replace=True))
    for _ in range(num_samples)
]

# Calculate mean and standard error
mean_proportion = np.mean(sample_proportions)
standard_error = np.std(sample_proportions, ddof=1)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(sample_proportions, bins=30, edgecolor='black', alpha=0.7)
plt.axvline(mean_proportion, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_proportion:.4f}')
plt.xlabel("Sample Proportion of Support")
plt.ylabel("Frequency")
plt.title("Histogram of Sample Proportions for UBI Support")
plt.legend()
plt.show()

# Print mean and standard error
print('Activity 1:\n')
print(f"Simulated Mean Proportion: {mean_proportion:.4f}")
print(f"Simulated Standard Error: {standard_error:.4f}")


### Activity 2

import math

population_size = 100000
support_percentage = 0.55
sample_size = 100

p = support_percentage
n = sample_size

mean_proportion = p
standard_error = math.sqrt((p * (1-p)) / n)

print('Activity 2:\n')
print(f'Theoretical Mean Proportion: {mean_proportion:.4f}')
print(f'Theoretical Standard Error: {standard_error:.4f}')


