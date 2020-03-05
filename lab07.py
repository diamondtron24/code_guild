# Let's play rock-paper-scissors with the computer.

# The computer will ask the user for their choice (rock, paper, scissors)
# The computer will randomly choose rock, paper or scissors
# Determine who won and tell the user
# Let's list all the cases:

# rock vs rock (tie)
# rock vs paper
# rock vs scissors
# paper vs rock
# paper vs paper
# paper vs scissors
# scissors vs rock
# scissors vs paper
# scissors vs scissors

# Version 2 
# After playing, ask them if they'd like to play again. 
# If they say yes, restart the game, otherwise exit.

import random
            

def calc_tie(player, computer):
        print(f'You selected {player} and computer selected {computer} it\'s a tie!')

def calc_winner(player, computer):      
        if player == 'rock' and computer == 'scissors':
           print(f'You selected {player} and computer selected {computer}. You Win!')        
        elif player == 'scissors' and computer == 'paper':
            print(f'You selected {player} and computer selected {computer}. You Win!')  
        elif player == 'paper' and computer == 'rock':
            print(f'You selected {player} and computer selected {computer}. You Win!')
        else:
            print(f'you selected {player} and computer selected {computer}. You Lose!')

def main():
    play = input('Would you like to play Rock, Paper, Scissors? (y/n): ')
    while play == 'y':
            opponent_choice = ['rock', 'paper', 'scissors']
            computer = random.choice(opponent_choice)
            player = input('Please choose rock, paper, or scissors: ')
            if player == computer: 
                calc_tie(player, computer)
                play = input('Do you want to play again? (y/n) ')
            else:
                calc_winner(player, computer)
                play = input('Do you want to play again? (y/n) ')
    else:
        print('Goodbye!')   
        play == ''


main()