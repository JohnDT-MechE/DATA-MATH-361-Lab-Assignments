### Final Project
### John Dominguez-Trujillo

### Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# 1. Load the dataset from GitHub
url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/refs/heads/main/Final_Project/owid-co2-data.csv'
df = pd.read_csv(url)

# 2. Clean data
df = df.dropna(subset=['co2', 'co2_per_capita'])

# 3. Add income group classification (manual mapping)
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

# 4. Global CO₂ Emissions Over Time
global_emissions = df[df['country'] == 'World']
plt.figure(figsize=(10,6))
plt.plot(global_emissions['year'], global_emissions['co2'])
plt.title('Global CO₂ Emissions Over Time')
plt.xlabel('Year')
plt.ylabel('CO₂ Emissions (Million Tonnes)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Income Group Comparison (Bar Plot for Recent Year)
recent_year = df['year'].max()
group_data = df[(df['year'] == recent_year) & (df['income_group'].notna())]
group_avg = group_data.groupby('income_group')['co2_per_capita'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=group_avg, x='income_group', y='co2_per_capita')
plt.title(f'Average CO₂ Per Capita by Income Group ({recent_year})')
plt.xlabel('Income Group')
plt.ylabel('CO₂ Per Capita (Tonnes)')
plt.tight_layout()
plt.show()

# 6. Country-Level Comparison (Bar Plot)
selected_countries = list(income_group_map.keys())
country_data = df[(df['year'] == recent_year) & (df['country'].isin(selected_countries))]

plt.figure(figsize=(10,5))
sns.barplot(data=country_data, x='country', y='co2_per_capita')
plt.title(f'CO₂ Per Capita in Selected Countries ({recent_year})')
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('CO₂ Per Capita (Tonnes)')
plt.tight_layout()
plt.show()

# 7. Regression: Global CO₂ Over Time
X = global_emissions['year']
y = global_emissions['co2']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# 8. Hypothesis Test: High vs Low Income
high_income = group_data[group_data['income_group'] == 'High income']['co2_per_capita']
low_income = group_data[group_data['income_group'] == 'Low income']['co2_per_capita']
t_stat, p_val = stats.ttest_ind(high_income, low_income, equal_var=False)

print(f"\nHypothesis Test (High vs Low Income):")
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value     = {p_val:.5f}")

