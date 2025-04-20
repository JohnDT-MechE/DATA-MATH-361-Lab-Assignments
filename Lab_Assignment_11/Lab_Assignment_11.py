### Lab Assignment 11
### John Dominguez-Trujillo

### Activity 1

## IMPORTS ESSENTIAL LIBRARIES
## PANDAS IS A LIBRARY USED FOR DATA MANIPULATION, ANALYSIS, AND DATA STRUCTURES
## STATSMODELS IS A LIBRARY USED FOR ESTIMATING STATISTICAL MODELS AND PERFORMING REGRESSION ANALYSIS, INCLUDING GENERATING REGRESSION TABLES
## STATS MODELS FORMULA API (SMF) ALLOWS LINEAR MODELS TO BE SPECIFIED USING R-LIKE FORMULAS
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

## LOADS DATA FROM CSV INTO A VARIABLE
## USING A URL THAT LINKS DIRECTLY TO THE CSV FILE IN MY GITHUB SO ANYONE CAN ACCESS IT
url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/refs/heads/main/Lab_Assignment_11/Hurricanes%202024%20data.csv'
df = pd.read_csv(url)

# Drop unnecessary columns and NaN rows if any
df = df[["Year", "US Pop (millions)", "Adjusted Costs (billions USD 2024)"]].dropna()

# PART 1.1: Regression of Adjusted Costs on Year

## BUILDING THE FIRST MODEL: COST ~ YEAR
## Define the regression formula
model1 = smf.ols('Q("Adjusted Costs (billions USD 2024)") ~ Year', data=df).fit()

## DISPLAYING THE REGRESSION TABLE
print("\n--- Regression 1: Adjusted Costs vs. Year ---")
print(model1.summary())

# PART 1.2: Regression of Adjusted Costs on US Population

## ONLY DIFFERENCE: Replace 'Year' with 'US Pop (millions)' in the formula
model2 = smf.ols('Q("Adjusted Costs (billions USD 2024)") ~ Q("US Pop (millions)")', data=df).fit()
print("\n--- Regression 2: Adjusted Costs vs. US Population ---")
print(model2.summary())

# PART 1.3: Regression of Adjusted Costs on Year and US Population

## THIS MODEL USES BOTH VARIABLES
model3 = smf.ols('Q("Adjusted Costs (billions USD 2024)") ~ Year + Q("US Pop (millions)")', data=df).fit()
print("\n--- Regression 3: Adjusted Costs vs. Year and US Population ---")
print(model3.summary())
