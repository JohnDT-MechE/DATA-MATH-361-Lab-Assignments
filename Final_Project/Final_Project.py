### Final Project
### John Dominguez-Trujillo



## IMPORT ESSENTIAL LIBRARIES

## PANDAS IS A LIBRARY USED FOR DATA MANIPULATION, ANALYSIS, AND DATA STRUCTURES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
## SEABORN IS A DATA VISUALIZATION LIBRARY BUILT ON TOP OF MATPLOTLIB THAT MAKES ATTRACTIVE AND INFORMATIVE STATISTICAL GRAPHICS
## SCIPY.STATS IS A SCIPY LIBRARY THAT PROVIDES VARIOUS STATISTICAL FUNCTIONS SUCH AS PROBABILITY DISTRIBUTIONS, STATISTICAL TESTS, AND DESCRIPTIVE STATISTICS
## STATSMODELS IS A LIBRARY USED FOR ESTIMATING STATISTICAL MODELS AND PERFORMING REGRESSION ANALYSIS, INCLUDING GENERATING REGRESSION TABLES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm



## SETUP DATA FRAME

## LOADS DATA FROM CSV INTO A VARIABLE
## USING A URL THAT LINKS DIRECTLY TO THE CSV FILE IN MY GITHUB SO ANYONE CAN ACCESS IT
url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/refs/heads/main/Final_Project/owid-co2-data.csv'
df = pd.read_csv(url)

## DROPS ROWS WITH MISSING VALUES IN 'CO2' AND 'CO2_PER_CAPITA' COLUMNS
df = df.dropna(subset=['co2', 'co2_per_capita'])

## THIS CREATES A DICTIONARY THAT MAPS COUNTRIES TO INCOME GROUPS AND THEN ASSIGNS EACH COUNTRY IN THE DATAFRAME TO ITS INCOME GROUP USING .MAP()
income_group_map = {
    'United States': 'High income',
    'Germany': 'High income',
    'Canada': 'High income',
    'United Kingdom': 'High income',
    'Australia': 'High income',
    'Japan': 'High income',
    'India': 'Lower-middle income',
    'Nigeria': 'Low income',
    'Ethiopia': 'Low income',
    'Bangladesh': 'Low income',
    'China': 'Upper-middle income',
    'Brazil': 'Upper-middle income',
    'South Africa': 'Upper-middle income',
    'Indonesia': 'Lower-middle income',
    'Mexico': 'Upper-middle income',
    'Pakistan': 'Lower-middle income'
}

df['income_group'] = df['country'].map(income_group_map)



## PLOT GLOBAL CO2 EMISSIONS OVER TIME

## EXTRACTS THE NECESSARY DATA INTO GLOBAL_EMISSIONS
global_emissions = df[df['country'] == 'World']

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize=(10,6))

## PLOT YEAR AND CO2 VALUES ON FIGURE
plt.plot(global_emissions['year'], global_emissions['co2'])

## ADDS TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.title('Global CO₂ Emissions Over Time')
plt.xlabel('Year')
plt.ylabel('CO₂ Emissions (Million Tonnes)')

## ADDS A GRID TO THE FIGURE
plt.grid(True)

## ADJUSTS SPACING TO PREVENT LABELS AND ELEMENTS FROM OVERLAPPING IN THE PLOT
plt.tight_layout()

## SHOWS THE PLOT IN THE FIGURE
plt.show()



## BAR PLOT OF INCOME GROUP COMPARISON

## EXTRACTS THE MOST RECENT YEAR FROM DATA INTO RECENT_YEAR
recent_year = df['year'].max()

## EXTRACTS THE NECESSARY DATA INTO GROUP_DATA AND CALCULATES THE AVERAGE
group_data = df[(df['year'] == recent_year) & (df['income_group'].notna())]
group_avg = group_data.groupby('income_group')['co2_per_capita'].mean().reset_index()

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize=(8,5))

## CREATES A BAR PLOT OF INCOME_GROUP AND CO2_PER_CAPITA ON FIGURE
sns.barplot(data=group_avg, x='income_group', y='co2_per_capita')

## ADDS TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.title(f'Average CO₂ Per Capita by Income Group ({recent_year})')
plt.xlabel('Income Group')
plt.ylabel('CO₂ Per Capita (Tonnes)')

## ADJUSTS SPACING TO PREVENT LABELS AND ELEMENTS FROM OVERLAPPING IN THE PLOT
plt.tight_layout()

## SHOWS THE PLOT IN THE FIGURE
plt.show()



## BAR PLOT OF COUNTRY COMPARISON

## EXTRACTS THE NECESSARY DATA FOR THE SELECTED COUNTRIES AND PUTS IT INTO COUNTRY_DATA
selected_countries = list(income_group_map.keys())
country_data = df[(df['year'] == recent_year) & (df['country'].isin(selected_countries))]

## CREATES A FIGURE AND DEFINES SIZE
plt.figure(figsize=(10,5))

## CREATES A BAR PLOT OF COUNTRY AND CO2_PER_CAPITA ON FIGURE
sns.barplot(data=country_data, x='country', y='co2_per_capita')

## ADDS TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
## PLT.XTICKS(ROTATION=45) ROTATES THE X-AXIS LABELS 45 DEGREES TO MAKE THEM EASIER TO READ
plt.title(f'CO₂ Per Capita in Selected Countries ({recent_year})')
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('CO₂ Per Capita (Tonnes)')

## ADJUSTS SPACING TO PREVENT LABELS AND ELEMENTS FROM OVERLAPPING IN THE PLOT
plt.tight_layout()

## SHOWS THE PLOT IN THE FIGURE
plt.show()



## LINEAR REGRESSION ANALYSIS

## EXTRACTS THE INDEPENDENT VARIABLE (YEAR) INTO X
## EXTRACTS THE DEPENDENT VARIABLE (CO2) INTO Y
X = global_emissions['year']
y = global_emissions['co2']

## ADDS A COLUMN OF ONES TO X SO THE REGRESSION MODEL INCLUDES AN INTERCEPT TERM
X = sm.add_constant(X)

## SM.OLS FITS A LINEAR REGRESSION MODEL USING ORDINARY LEAST SQUARES
## .FIT() TRAINS THE MODEL ON THE DATA
model = sm.OLS(y, X).fit()

## PRINTS THE FULL REGRESSION TABLE TO THE OUTPUT TERMINAL
print(model.summary())



## HYPOTHESIS TEST (LOW-INCOME AND HIGH-INCOME GROUPS)

## EXTRACTS THE NECESSARY DATA INTO HIGH_INCOME AND LOW_INCOME
high_income = group_data[group_data['income_group'] == 'High income']['co2_per_capita']
low_income = group_data[group_data['income_group'] == 'Low income']['co2_per_capita']

## CALCULATES THE T-STATISTIC AND CORRESPONDING P-VALUE
t_stat, p_val = stats.ttest_ind(high_income, low_income, equal_var=False)

## PRINT RESULTING T-STATISTIC AND P-VALUE TO THE TERMINAL
print(f"\nHypothesis Test (High vs Low Income):")
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value     = {p_val:.5f}")