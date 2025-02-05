### Lab Assignment 3
### John Dominguez-Trujillo

### Activity 1
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/2b392369cdfa92927b351f6f749aca9cbd02a60d/Lab_Assignment_3/TwoWayTableOSS_MS.csv'
df = pd.read_csv(url)

df = df.dropna()

df.set_index(df.columns[0], inplace = True)

df = df.T

df_percent = df.div(df.sum(axis = 1), axis = 0) * 100

fig, ax = plt.subplots(figsize = (10,6))
df_percent.plot(kind = 'bar', stacked = True, ax = ax)

plt.title('Mississippi School Suspensions Based on Race')
plt.xlabel('Race')
plt.ylabel('Percentage of Students')
plt.xticks(rotation = 45)
plt.legend(title = 'Suspension Status', bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.ylim(0,100)

plt.tight_layout()
plt.show()


### Activity 2
import pandas as pd

url = 'https://raw.githubusercontent.com/JohnDT-MechE/DATA-MATH-361-Lab-Assignments/2b392369cdfa92927b351f6f749aca9cbd02a60d/Lab_Assignment_3/Titanic.csv'
df = pd.read_csv(url)

two_way_table = df.pivot_table(index = ['Class', 'Sex'], columns = 'Outcome', aggfunc = 'size', fill_value = 0)

print(two_way_table)