### Lab Assignment 6
### John Dominguez-Trujillo

### Activity 1 and Activity 2

import numpy as np
import matplotlib.pyplot as plt

# Given population parameters
mu = 98.2  # Mean body temperature
sigma = 0.73  # Standard deviation

# Sampling parameters
num_samples = 1000  # Number of samples
sample_size = 100  # Size of each sample

# Generate sample means
sample_means = [
    np.mean(np.random.normal(mu, sigma, sample_size))
    for _ in range(num_samples)
]

# Select one random sample
random_sample = np.random.normal(mu, sigma, sample_size)

# Compute the sample mean and standard deviation
sample_mean = np.mean(random_sample)
sample_std = np.std(random_sample, ddof=1)

# Compute the 95% confidence interval using Z-score
z_critical = 1.96  # Z-score for 95% confidence interval
margin_of_error_z = z_critical * (sample_std / np.sqrt(sample_size))
confidence_interval_z = (sample_mean - margin_of_error_z, sample_mean + margin_of_error_z)

# Plot histogram with differently colored CI limits using Z-score method
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, edgecolor='black', alpha=0.7, density=True)

# Plot the sample mean
plt.axvline(sample_mean, color='blue', linestyle='dashed', linewidth=2, label=f'Sample Mean: {sample_mean:.2f}')

# Plot the confidence interval with different colors
plt.axvline(confidence_interval_z[0], color='orange', linestyle='dashed', linewidth=2, label=f'Lower 95% CI: {confidence_interval_z[0]:.2f}')
plt.axvline(confidence_interval_z[1], color='purple', linestyle='dashed', linewidth=2, label=f'Upper 95% CI: {confidence_interval_z[1]:.2f}')

# Labels and title
plt.xlabel('Sample Mean Temperature (°F)')
plt.ylabel('Density')
plt.title('Histogram of Sample Mean Body Temperatures with 95% CI (Z-score)')
plt.legend()
plt.show()

# Print the sample mean and 95% confidence interval
print(f"Sample Mean: {sample_mean:.2f}°F")
print(f"95% Confidence Interval: [{confidence_interval_z[0]:.2f}, {confidence_interval_z[1]:.2f}]")

