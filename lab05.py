# Lab 5: Random Emoticon Generator
# Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Assemble and display the emoticon
# import random

# fruits = ['apple', 'banana', 'pineapple']
# fruit = random.choice(fruits)
# print(fruit)
# Example output:

# :-P
# Version 2
# Use a while loop to generate 5 emoticons.

# Version 1

# import random



# eyes = [';', ':', '>', '%', '!', 'O']
# nose = ['>', '-', '+', '=', '@', '<', '~']
# mouth = ['>', 'X', 'S', ')', '(', 'D', 'Z']
    



# while True:
#     play = input('Would you like to creat a random emoticon? (y/n)')
#     if play == 'y':
#         print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
#     else:
#         break

# Version 2

import random

def emoticon():
    eyes = [';', ':', '>', '%', '!', 'O']
    nose = ['>', '-', '+', '=', '@', '<', '~']
    mouth = ['>', 'X', 'S', ')', '(', 'D', 'Z']
    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

def main():
    play = 0
    while play < 5:
        emoticon()
        play = play + 1


main()