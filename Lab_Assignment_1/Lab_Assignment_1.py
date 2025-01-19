### Lab Assignment 1
### John Dominguez-Trujillo

### Activity 1

## ASSIGN VALUES TO VARIABLES
num1 = 5
num2 = 8

## ADD THE VALUES OF THE VARIABLES
num_sum = num1 + num2

## CREATE AN OUTPUT STRING THAT STATES VALUES OF VARIABLES AND RESULT OF SUMMATION
output = f'The sum of {num1} and {num2} is {num_sum}'
print(output)


### Activity 2

## CREATE LIST OF 5 CHOSEN NUMBERS
my_num_list = [3, 7, 9, 15, 24]

## RESET/INITIALIZE SUM TO ZERO
num_sum = 0

## LOOP THROUGH EACH NUMBER IN MY_NUM_LIST AND SUM
## CREATE AND PRINT OUTPUT STRING FOR EACH PARTIAL SUM
for number in my_num_list:
    num_sum += number
    output = f'\nAdding {number}...\nPartial Sum: {num_sum}'
    print(output)
    
## CREATE FINAL SUM OUTPUT STRING AND PRINT TO CONSOLE
final_output = f'\nThe final sum of adding {my_num_list[0]}, {my_num_list[1]}, {my_num_list[2]}, {my_num_list[3]}, and {my_num_list[4]} is {num_sum}'
print(final_output)


### Activity 3

## NUMPY IS A PYTHON LIBRARY THAT ADDS SUPPORT FOR USING AND HANDLING MULTI-DIMENSIONAL ARRAYS AND MATRICES AND ALLOWS FOR HIHG-LEVEL MATHEMATICAL FUNCTIONS TO BE PERFORMED ON THESE ARRAYS/MATRICES
## MATPLOTLIB IS A PLOTTING LIBRARY THAT PROVIDES AN OBJECT-OREINTED API FOR DISPLAYING PLOTS
## THESE LIBRARIES ESSENTIALLY GIVE PYTHON THE CAPABILITIES OF MATLAB
import numpy as np
import matplotlib.pyplot as plt

## DEFINE COEFFICIENTS FOR QUADRATIC FUNCTION
a,b,c = 2, 3, 2

## DEFINE THE QUADRATIC FUNCTION Y = 5X^2 - 13X + 7
def quad_eqn(x):
    return a * x**2 + b * x + c

## CALCULATES VERTEX OF QUADRATIC FUNCTION
vertex_x = -b / (2 * a)
vertex_y = quad_eqn(vertex_x)

## GENERATES X AND Y VALUES FOR THE PLOT
## LINSPACE CREATES AN ARRAY/MATRIX OF 500 EVENLY SPACED NUMBERS BETWEEN THE VALUES GIVEN
x = np.linspace(vertex_x - 5, vertex_x + 5, 500)
y = quad_eqn(x)

## CREATES A FIGURE AND DEFINES SIZE
## PLOT X AND Y VALUES ON FIGURE, LABEL THE PLOTTED DATA, SETS COLOR TO BLUE
## BASICALLY DONE THE SAME WAY IN MATLAB (MY MECH ENG BACKGROUND)
plt.figure(figsize = (8,6))
plt.plot(x, y, label = 'f(x)', color = 'blue')

## LIMITS X AND Y AXIS TO GIVEN PARAMETERS WHEN PLOTTING
plt.xlim(-2, 0.5)
plt.ylim(0, 5)

## MARKS AND LABELS VERTEX ON PLOT WITH A RED POINT AND TEXT
## S = 50 SETS THE SIZE OF THE RED POINT
## THE .2F ALLOWS FOR ONLY TWO DECIMAL PLACES AFTER THE X AND Y VALUE OF THE VERTEX
## THE VERTEX_Y - 0.4 ENSURES TEXT DOES NOT OVERLAP CURVE
plt.scatter(vertex_x, vertex_y, color = 'red', label = 'Vertex', s = 50)
plt.text(vertex_x, vertex_y - 0.4, f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})', fontsize = 10, color = 'red', va = 'bottom', ha = 'center')

## THIS WILL ALLOW FOR THE 2 TO BE SUPER-SCRIPTED IN THE PLOT TITLE
power = '\u00b2'

## ADDS TITLE TO PLOT AND LABELS THE X AND Y AXIS OF THE PLOT
plt.title(f'Quadratic Function and Vertex Visualization\nf(x) = {a}x{power} + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('f(x)')

## ADDS A VERTICAL LINE OF SYMMETRY AT THE X VERTEX
plt.axvline(vertex_x, color = 'grey', linewidth = 0.8, linestyle = '--', label = 'Axis of Symmetry')

## ADDS A GRID AND LEGEND TO THE FIGURE
## ALPHA CONTROLS THE TRANSPARENCY OF THE GRID LINES
plt.grid(alpha = 0.3)
plt.legend()

## SHOWS THE PLOT IN THE FIGURE
plt.show()