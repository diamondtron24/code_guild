# Lab 2: Mad Libs
# Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

# Instructions
# Search the interwebs for an example Mad Lib
# Ask the user for each word you'll put in your Mad Lib
# Use string concatenation to put each word into the Mad Lib
# Example:
# >>> Give me an antonym for 'data': nonmaterial
# >>> Tell me an adjective: Bearded
# >>> Give me a sciency buzzword: half-stack
# >>> A type of animal (plural): parrots
# >>> Some Sciency thing: warp drive
# >>> Another sciency thing: Trilithium crystals
# >>> Sciency adjective: biochemical
# ...
# >>> Nonmaterial Scientist Job Description:
# >>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
# >>> Key responsibilities:
# >>> - Extract patterns from non-material
# >>> - Optimize warp drive
# >>> - Transform trilithium crystals into biochemical material.

# Version 2 (optional)
# Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then 
# use the .split() function to store each adjective and later use it in your story.
# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

# Version 3 (optional)
# Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear 
# the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could 
# then ask them if they'd like to make another story, and so on.
# Key Concepts
# Variables
# String formatting
# Handling user input

# Solution 1

# crush_name = 'Taco'
# verb_1 = 'slide'
# favorite_room = 'Laundry Room'
# plural_noun_1  = 'Ferrets'
# body_part = 'hair'
# piece_of_furniture = 'ottoman'
# adjective_1 = 'slimey'
# adverb_1 = 'rapidly'
# number_1 = '4'
# plural_body_parts = 'nostrils'
# musician = 'AC-DC'
# food = 'enchalada'
# Brand_of_shoes = 'Nikes'
# number_2 = '3'

# print()

# print(f"""You were suddenly feeling frisky so you asked {crush_name} if he wanted to {verb_1}
# in the {favorite_room} with you. Normally, you use this room to store your vast collection 
# of {plural_noun_1}, but this time you felt like switching things up.

# You just knew he was ready to go when he propped his {body_part} up on the {piece_of_furniture} 
# and gave you his {adjective_1} bedroom eyes.

# After {adverb_1} going at it for {number_1} minutes, you both climaxed at the exact same 
# time. But then you looked deep into each other's {plural_body_parts} 
# and knew exactly what the other one wanted: one more round. You put on {musician} 
# greatest hits, lit a few {food}-scented candles and knocked {Brand_of_shoes} 
# for {number_2} more hours!""")


# Solution 2

# import random

# print("Let/'s play Madlibs!")

# print()

# crush_name = input('Please enter 3 crush names, separated by commas: ')
# verb_1 = input('Please enter 3 verbs, separated by commas: ')
# favorite_room = input('Please enter 3 rooms in a house, separated by commas: ')
# plural_noun_1  = input('Please enter 3 plural nouns, separated by commas: ')
# body_part = input('Please enter 3 body parts, separated by commas: ')
# piece_of_furniture = input('Please enter 3 pieces of furniture, separated by commas: ')
# adjective_1 = input('Please enter 3 adjectives, separated by commas: ')
# adverb_1 = input('Please enter 3 adverbs, separated by commas: ')
# number_1 = input('Please enter 3 numbers, separated by commas: ')
# plural_body_parts = input('Please enter 3 plural body parts, separated by commas: ')
# musician = input('Please enter 3 musicians, seaprated by commas: ')
# food = input('Please enter 3 foods, separated by commas: ')
# brand_of_shoes = input('Please enter 3 types, or brands of shoes, separated by commas: ')
# number_2 = input('Please enter 3 numbers, separated by commas: ')

# crush = crush_name.split(", ")
# verb = verb_1.split(", ")
# room = favorite_room.split(", ")
# plural = plural_noun_1.split(", ")
# part = body_part.split(", ")
# furniture = piece_of_furniture.split(", ")
# adj_1 = adjective_1.split(", ")
# adverb = adverb_1.split(", ")
# num_1 = number_1.split(", ")
# parts = plural_body_parts.split(", ")
# music = musician.split(", ")
# foods = food.split(", ")
# shoes = brand_of_shoes.split(", ")
# num_2 = number_2.split(", ")

# print()

# print(f"""You were suddenly feeling frisky so you asked {random.choice(crush)} if he wanted to {random.choice(verb)}
# in the {random.choice(room)} with you. Normally, you use this room to store your vast collection 
# of {random.choice(plural)}, but this time you felt like switching things up.

# You just knew he was ready to go when he propped his {random.choice(part)} up on the {random.choice(furniture)} 
# and gave you his {random.choice(adj_1)} bedroom eyes.

# After {random.choice(adverb)} going at it for {random.choice(num_1)} minutes, you both climaxed at the exact same 
# time. But then you looked deep into each other's {random.choice(parts)} 
# and knew exactly what the other one wanted: one more round. You put on {random.choice(music)} 
# greatest hits, lit a few {random.choice(foods)}-scented candles and knocked {random.choice(shoes)} 
# for {random.choice(num_2)} more hours!""")


# Solution 3

import random


def madlib():
    crush_name = input('Please enter 3 crush names, separated by commas: ')
    verb_1 = input('Please enter 3 verbs, separated by commas: ')
    favorite_room = input('Please enter 3 rooms in a house, separated by commas: ')
    plural_noun_1  = input('Please enter 3 plural nouns, separated by commas: ')
    body_part = input('Please enter 3 body parts, separated by commas: ')
    piece_of_furniture = input('Please enter 3 pieces of furniture, separated by commas: ')
    adjective_1 = input('Please enter 3 adjectives, separated by commas: ')
    adverb_1 = input('Please enter 3 adverbs, separated by commas: ')
    number_1 = input('Please enter 3 numbers, separated by commas: ')
    plural_body_parts = input('Please enter 3 plural body parts, separated by commas: ')
    musician = input('Please enter 3 musicians, seaprated by commas: ')
    food = input('Please enter 3 foods, separated by commas: ')
    brand_of_shoes = input('Please enter 3 types, or brands of shoes, separated by commas: ')
    number_2 = input('Please enter 3 numbers, separated by commas: ')

    crush = crush_name.split(", ")
    verb = verb_1.split(", ")
    room = favorite_room.split(", ")
    plural = plural_noun_1.split(", ")
    part = body_part.split(", ")
    furniture = piece_of_furniture.split(", ")
    adj_1 = adjective_1.split(", ")
    adverb = adverb_1.split(", ")
    num_1 = number_1.split(", ")
    parts = plural_body_parts.split(", ")
    music = musician.split(", ")
    foods = food.split(", ")
    shoes = brand_of_shoes.split(", ")
    num_2 = number_2.split(", ")

    print()
    
    a = True
   
    while a:
        permission = input('Would you like to read your Madlib?')
        if permission == 'yes':
            print(f"""You were suddenly feeling frisky so you asked {random.choice(crush)} if he wanted to {random.choice(verb)}
            in the {random.choice(room)} with you. Normally, you use this room to store your vast collection 
            of {random.choice(plural)}, but this time you felt like switching things up.

            You just knew he was ready to go when he propped his {random.choice(part)} up on the {random.choice(furniture)} 
            and gave you his {random.choice(adj_1)} bedroom eyes.

            After {random.choice(adverb)} going at it for {random.choice(num_1)} minutes, you both climaxed at the exact same 
            time. But then you looked deep into each other's {random.choice(parts)} 
            and knew exactly what the other one wanted: one more round. You put on {random.choice(music)} 
            greatest hits, lit a few {random.choice(foods)}-scented candles and knocked {random.choice(shoes)} 
            for {random.choice(num_2)} more hours!""")
        else:
            a = False
            print('Goodbye')
            

x = True

while x: 
    response = input("Do you want to play Madlibs?")
    if response == 'yes':
        madlib()
    else: 
        x = False
        print('Goodbye')
    
