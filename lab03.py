# Lab 3: Grading

# Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

# Concepts Covered
# input, print
# type conversion (str to int)
# comparisons (< <= > >=)
# if, elif, else
# Instructions
# Have the user enter a number representing the grade (0-100)
# Convert the number grade to a letter grade
# Numeric Ranges
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F
# Version 2
# Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, 
# or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. 
# Then you can concatenate that string with your grade string.

# Version 3
# Extract the logic used to determine the grade and its qualifier ('+', '-', or ' ') into functions. 
# Additionally, use a while loop to repeatedly ask the user if they'd like to compute another grade after each computation.


# Version 1

grade_enter = input('Please enter your grade percentage: ')

if grade_enter <= 59:
    print('You got an F.')
elif grade_enter < 70:
    print('You got a D.')
elif grade_enter < 80:
    print('You got a C.')
elif grade_enter < 90:
    print('You got a B.')
elif grade_enter <= 100:
    print('You got an A.')


