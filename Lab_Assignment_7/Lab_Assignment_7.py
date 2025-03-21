### Lab Assignment 6
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## SCIPY.STATS IS A SCIPY LIBRARY THAT PROVIDES VARIOUS STATISTICAL FUNCTIONS SUCH AS PROBABILITY DISTRIBUTIONS, STATISTICAL TESTS, AND DESCRIPTIVE STATISTICS
## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIHG-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
import scipy.stats as stats
import numpy as np

## DEFINE SAMPLE SIZE, GIVEN VALUES, AND NULL HYPOTHESES
sample_size = 9593  ## TOTAL SURVEYED
successes = 4125    ## TOTAL IN FAVOR OF MASKS
p0 = 0.45           ## NULL HYPOTHESIS PROPORTION

## COMPUTE SAMPLE PROPORTION
p_hat = successes / sample_size

## COMPUTE STANDARD ERROR FOR ONE SAMPLE CATEGORICAL HYPOTHESES TEST
standard_error = np.sqrt((p0 * (1 - p0)) / sample_size)

## COMPUTE Z-SCORE
z_score = (p_hat - p0) / standard_error

## COMPUTE P-VALUE, ONE-TAILED TEST SINCE WE ARE TESTING IF IT SUPPORT IS SIGNIFICANTLY FEWER THAN THE NULL HYPOTHESIS PROPORTION
p_value = stats.norm.cdf(z_score)

## PRINT RESULTING Z-SCORE AND P-VALUE
print('Part 1: Hypothesis Test for Proportion\n')
print(f'Z-score: {z_score:.6f}')
print(f'P-value: {p_value:.6f}')

## INTERPRET P-VALUE AND DETERMINE CONCLUSIONS BASED ON THE STATISTICAL EVIDENCE
alpha = 0.05    ## SIGNIFICANCE LEVEL
if p_value < alpha:
    print('Reject the Null Hypothesis: Significantly fewer than 45% support mask-wearing.')
else:
    print('Fail to Reject the Null Hypothesis: No significant evidence of fewer than 45% support.')


### Activity 2

## IMPORTS ESSENTIAL LIBRARIES
## SCIPY.STATS IS A SCIPY LIBRARY THAT PROVIDES VARIOUS STATISTICAL FUNCTIONS SUCH AS PROBABILITY DISTRIBUTIONS, STATISTICAL TESTS, AND DESCRIPTIVE STATISTICS
## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIHG-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
import scipy.stats as stats
import numpy as np

##EXPLANATIONS: Define given values.
## DEFINE SAMPLE MEAN, SAMPLE STANDARD DEVIATION, N, AND NULL HYPOTHESIS AVERAGE
sample_mean = 3.395 ## OBSERVED MEAN INFLATION RATE
sample_std = 0.22   ## STANDARD DEVIATION OF SAMPLE
n = 12              ## NUMBER OF MONTHS SAMPLED
mu0 = 3.0           ## PREDICTED MEAN INFLATION RATE

## COMPUTE STANDARD ERROR FOR ONE SAMPLE QUANTITATIVE HYPOTHESIS TEST
standard_error = sample_std / np.sqrt(n)

## COMPUTE T-SCORE
t_score = (sample_mean - mu0) / standard_error

## COMPUTE P-VALUE, MULTIPLIED BY TWO FOR TWO-TAILED TEST SINCE WE ARE TESTING IF IT IS DIFFERENT FROM THE NULL HYPOTHESIS
p_value = 2 * (1 - stats.t.cdf(abs(t_score), df=n-1))

## PRINT RESULTING T-SCORE, P-VALUE, SAMPLE MEAN, AND NULL HYPOTHESIS MEAN
print('\n\nPart 2: Hypothesis Test for Mean Inflation Rate\n')
print(f'T-score: {t_score:.6f}')
print(f'P-value: {p_value:.6f}')
print(f'Sample Mean: {sample_mean:.3f}')
print(f'Null Hypothesis Mean: {mu0:.1f}')

## INTERPRET P-VALUE AND DETERMINE CONCLUSIONS BASED ON THE STATISTICAL EVIDENCE
alpha = 0.05    ## SIGNIFICANCE LEVEL
if p_value < alpha:
    print('Reject the Null Hypothesis: Mean inflation rate significantly differs from 3%.')
else:
    print('Fail to Reject the Null Hypothesis: No significant evidence that inflation rate differs from 3%.')
