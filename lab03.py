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

# grade_enter = input('Please enter your grade percentage: ')

# if grade_enter <= 59:
#     print('You got an F.')
# elif grade_enter < 70:
#     print('You got a D.')
# elif grade_enter < 80:
#     print('You got a C.')
# elif grade_enter < 90:
#     print('You got a B.')
# elif grade_enter <= 100:
#     print('You got an A.')


# Version 2




# while True:
#     grade_enter = int(input('Please enter your grade percentage: '))    

#     if grade_enter <= 59:
#         letter = 'F'
#     elif grade_enter < 70:
#         letter = "D"
#     elif grade_enter < 80:
#         letter = 'C'
#     elif grade_enter < 90:
#         letter = 'B'
#     elif grade_enter <= 100:
#         letter = 'A'
#     elif grade_enter > 100:
#         print('Invalid precentage entered')
#         print('Goodbye')
#         break

#     percent = grade_enter % 10
#     if grade_enter < 60:
#         print(letter)
#     elif percent < 5:
#         print(f'Your grade = {letter}-')
#     elif percent == 5:
#         print(f'Your grade = {letter}')
#     elif percent > 5:
#         print(f'Your grade = {letter}+')

#     again = input('Would you like to enter another grade percentage? y/n: ')
#     if again != 'y':
#         print('OK, Goodbye')
#         break

    # Version 3


# this is the get lettergrade() function. it's returning the grade letter to pass into gradepercent() function

def lettergrade():
    if grade_enter <= 59:
        letter = 'F'
        return letter
    elif grade_enter < 70:
        letter = "D"
        return letter
    elif grade_enter < 80:
        letter = 'C'
        return letter
    elif grade_enter < 90:
        letter = 'B'
        return letter
    elif grade_enter <= 100:
        letter = 'A'
        return letter
    elif grade_enter > 100:
        print('Invalid precentage entered')
        print('Goodbye')

# This is the gradepercent() function. it has letter passed in from lettergrade()

def gradepercent(letter):
    percent = grade_enter % 10
    if grade_enter < 60:
        print(letter)
    elif percent < 5:
        print(f'Your grade = {letter}-')
    elif percent == 5:
        print(f'Your grade = {letter}')
    elif percent > 5:
        print(f'Your grade = {letter}+')


# this is the loop that asks for grade percentage, returns the letter grade with +- and asks if you would like to enter another. 

while True:
    grade_enter = int(input('Please enter your grade percentage: '))
    letter = lettergrade()
    gradepercent(letter)
    again = input('Would you like to enter another grade percentage? y/n: ')
    if again != 'y':
        print('OK, Goodbye')
        break


