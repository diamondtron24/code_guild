# Lab 6: Password Generator
# Let's generate a password of length n using a while loop and random.choice, 
# this will be a string of random characters.

# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

# Concepts Covered
# input, print
# looping
# random.choice
# the 'string builder pattern'
# Version 2
# Allow the user to enter the value of n, remember to convert its type, as input returns a string.

# Version 3 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, 
# and special characters they'd like in their password. Generate a password accordingly.


# version 1

# import random
# import string

# character = string.ascii_letters + string.digits + string.punctuation

# print('Let\'s create a random password')

# password = ''

# pass_length = int(input('How many characters do you want your password to be (1-20):  '))

# x = 0

# while x < pass_length:
#     password = password + random.choice(character)
#     x += 1

# print(f' Your randomly generated password: {password}')

# -----------------------------------------------------------------------------------------

# version 2


# import random
# import string

# character = string.ascii_letters + string.digits + string.punctuation

# def code_length():
#     pass_length = int(input('How many characters do you want your password to be (1-20):  '))
#     return pass_length

# def generator(pass_length):
#     x = 0
#     password = ''
#     while x < pass_length:
#         password = password + random.choice(character)
#         x += 1
#     print(f' Your randomly generated password: {password}')

# def main():
#     generator(code_length())

# main()

#---------------------------------------------------------------------------------------------
# Version 3 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, 
# and special characters they'd like in their password. Generate a password accordingly.

import random
import string


def lower_generator(pass_lower):
    x = 0
    lower = ''
    while x < pass_lower:
        lower = lower + random.choice(string.ascii_lowercase)
        x += 1
    return lower

def upper_generator(pass_upper):
    x = 0
    upper = ''
    while x < pass_upper:
        upper = upper + random.choice(string.ascii_uppercase)
        x += 1
    return upper

def number_generator(pass_number):
    x = 0
    number = ''
    while x < pass_number:
        number = number + random.choice(string.digits)
        x += 1
    return number

def special_generator(pass_special):
    x = 0
    special = ''
    while x < pass_special:
        special = special + random.choice(string.punctuation)
        x += 1
    return special

def generate_password(lower, upper, digits, special):
    
    mashup = list(lower + upper + digits + special)
    random.shuffle(mashup)
    print( ''.join(mashup))



def main():
    pass_lower = int(input('How many lower case characters do you want your password to be (1-20):  '))
    pass_upper = int(input('How many upper case characters do you want your password to be (1-20):  '))
    pass_number = int(input('How many number characters do you want your password to be (1-20):  '))
    pass_special = int(input('How many special characters do you want your password to be (1-20):  '))  
    generate_password(lower_generator(pass_lower), upper_generator(pass_upper), number_generator(pass_number), special_generator(pass_special))
   

main()