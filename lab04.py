# Lab 4: Magic 8-Ball
# Let's write a program to simulate the classic "Magic Eight Ball"

# Concepts Covered
# input, print
# import
# random.choice
# Instructions
# Print a welcome screen to the user.
# Use the random module's random.choice() to choose a prediction.
# Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
# Display the result of the 8-ball.
# Below are some example 'predictions':

# It is certain
# It is decidedly so
# Without a doubt
# Yes definitely
# You may rely on it
# As I see it, yes
# Most likely
# Outlook good
# Yes
# Signs point to yes
# Reply hazy try again
# Ask again later
# Better not tell you now
# Cannot predict now
# Concentrate and ask again
# Don't count on it
# My reply is no
# My sources say no
# Outlook not so good
# Very doubtful
# Version 2
# Using a while loop, keep asking the user for a question, if they enter 'done', exit


# version 1

# import random

# answers = [
# 'It is certain',
# 'It is decidedly so',
# 'Without a doubt',
# 'Yes definitely',
# 'You may rely on it',
# 'As I see it, yes',
# 'Most likely',
# 'Outlook good',
# 'Yes',
# 'Signs point to yes',
# 'Reply hazy try again',
# 'Ask again later',
# 'Better not tell you now',
# 'Cannot predict now',
# 'Concentrate and ask again',
# 'Don\'t count on it',
# 'My reply is no',
# 'My sources say no',
# 'Outlook not so good',
# 'Very doubtful'
# ]

# play = input('Ask the random 8 Ball a question (done to exit): ')
# if play == 'done':
#     print('OK Goodbye.')
# else:
#     print(random.choice(answers))


# version 2

import random

def eightballanswer():

    answers = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
    ]
    print(random.choice(answers))

def main():
    while True:
        play = input('Ask the random 8 Ball a question (done to exit): ')
        if play == 'done':
            break
        else:
            eightballanswer()

main()


