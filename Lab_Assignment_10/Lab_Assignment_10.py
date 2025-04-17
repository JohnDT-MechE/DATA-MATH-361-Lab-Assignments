### Lab Assignment 9
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## PANDAS IS A LIBRARY USED FOR DATA MANIPULATION, ANALYSIS, AND DATA STRUCTURES
## STATSMODELS IS A LIBRARY USED FOR ESTIMATING STATISTICAL MODELS AND PERFORMING REGRESSION ANALYSIS, INCLUDING GENERATING REGRESSION TABLES
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load the dataset
df = pd.read_csv("/content/Income.csv")  # Adjust path if needed for local Colab environment
df.head()

# PART 1

## 1. REGRESSION OF INCOME ON AGE
## THIS MODEL USES 'AGE' AS THE ONLY PREDICTOR FOR 'INCOME'
## WE USE statsmodels TO PERFORM OLS REGRESSION
model_age = smf.ols('Income ~ Age', data=df).fit()
print("Regression: Income ~ Age")
print(model_age.summary())

## 2. REGRESSION OF INCOME ON EXPERIENCE
## ONLY DIFFERENCE IS THAT THE PREDICTOR IS NOW 'EXPERIENCE'
model_exp = smf.ols('Income ~ Experience', data=df).fit()
print("\nRegression: Income ~ Experience")
print(model_exp.summary())

## 3. REGRESSION OF INCOME ON AGE AND EXPERIENCE
## THIS MODEL INCLUDES BOTH 'AGE' AND 'EXPERIENCE' AS PREDICTORS
model_both = smf.ols('Income ~ Age + Experience', data=df).fit()
print("\nRegression: Income ~ Age + Experience")
print(model_both.summary())
