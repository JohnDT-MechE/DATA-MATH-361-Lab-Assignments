### Lab Assignment 6
### John Dominguez-Trujillo

### Activity 1
import scipy.stats as stats
import numpy as np

##EXPLANATIONS: Import necessary libraries. 
## scipy.stats for statistical functions, numpy for numerical operations.

# Part 1: Hypothesis Test for Proportion (Mask-Wearing Support)

##EXPLANATIONS: Define known values from the problem statement.
sample_size = 9593  # Total surveyed people
successes = 4125  # People who agreed on mask importance
p0 = 0.45  # Null hypothesis proportion

##EXPLANATIONS: Compute sample proportion.
p_hat = successes / sample_size

##EXPLANATIONS: Compute standard error for proportion test.
standard_error = np.sqrt((p0 * (1 - p0)) / sample_size)

##EXPLANATIONS: Compute z-score.
z_score = (p_hat - p0) / standard_error

##EXPLANATIONS: Compute p-value (one-tailed test, since we test if it's significantly fewer).
p_value = stats.norm.cdf(z_score)

##EXPLANATIONS: Print the results.
print("Part 1: Hypothesis Test for Proportion")
print(f"Sample Proportion: {p_hat:.4f}")
print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")

##EXPLANATIONS: Interpret results.
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: Significantly fewer than 45% support mask-wearing.")
else:
    print("Fail to reject the null hypothesis: No significant evidence of fewer than 45% support.")


# Activity 2

import scipy.stats as stats
import numpy as np

##EXPLANATIONS: Define given values.
sample_mean = 3.395  # Observed mean inflation rate
sample_std = 0.22  # Standard deviation of sample
n = 12  # Number of months
mu0 = 3.0  # Predicted mean inflation rate

##EXPLANATIONS: Compute standard error for mean test.
standard_error = sample_std / np.sqrt(n)

##EXPLANATIONS: Compute t-score.
t_score = (sample_mean - mu0) / standard_error

##EXPLANATIONS: Compute p-value (two-tailed test since we test if it's different, not just higher or lower).
p_value = 2 * (1 - stats.t.cdf(abs(t_score), df=n-1))

##EXPLANATIONS: Print the results.
print("\nPart 2: Hypothesis Test for Mean Inflation Rate")
print(f"Sample Mean: {sample_mean:.4f}%")
print(f"T-score: {t_score:.4f}")
print(f"P-value: {p_value:.4f}")

##EXPLANATIONS: Interpret results.
if p_value < alpha:
    print("Reject the null hypothesis: Mean inflation rate significantly differs from 3%.")
else:
    print("Fail to reject the null hypothesis: No significant evidence that inflation rate differs from 3%.")

