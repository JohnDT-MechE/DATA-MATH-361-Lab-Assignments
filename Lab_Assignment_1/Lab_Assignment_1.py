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

import matplotlib
import pandas
import numpy


