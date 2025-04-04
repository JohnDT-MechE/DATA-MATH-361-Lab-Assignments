### Lab Assignment 8
### John Dominguez-Trujillo

### Activity 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ##EXPLANATIONS: LOAD THE DATA FROM THE CSV FILE YOU UPLOADED
url = '/content/happiness-cantril-ladder.csv'
data = pd.read_csv(url)

# ##EXPLANATIONS: PREVIEW THE FIRST FEW ROWS TO SEE WHAT COLUMNS ARE AVAILABLE
print(data.head())

# ##EXPLANATIONS: FILTER DATA FOR YEAR 2019
data_2019 = data[data['year'] == 2019]

# ##EXPLANATIONS: DROP MISSING VALUES FROM 'Life Ladder' AND 'Log GDP per capita'
data_2019 = data_2019.dropna(subset=['Life Ladder', 'Log GDP per capita'])

# ##EXPLANATIONS: EXTRACT X (GDP) AND y (Life Satisfaction) FOR REGRESSION
X = data_2019[['Log GDP per capita']]
y = data_2019['Life Ladder']

# ##EXPLANATIONS: FIT A LINEAR REGRESSION MODEL
model = LinearRegression()
model.fit(X, y)

# ##EXPLANATIONS: MAKE PREDICTIONS USING THE MODEL
y_pred = model.predict(X)

# ##EXPLANATIONS: GET COEFFICIENTS FOR THE REGRESSION LINE
slope = model.coef_[0]
intercept = model.intercept_
r_squared = r2_score(y, y_pred)

# ##EXPLANATIONS: PLOT SCATTERPLOT AND REGRESSION LINE
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Log GDP per capita', y='Life Ladder', data=data_2019, label='Data Points')
plt.plot(X, y_pred, color='red', label=f'OLS Line: y = {slope:.2f}x + {intercept:.2f}')
plt.title('Life Satisfaction vs. Log GDP per Capita (2019)')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Life Satisfaction (Cantril Ladder)')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f'$R^2$ = {r_squared:.2f}', transform=plt.gca().transAxes)
plt.show()

