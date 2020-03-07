# Lab 8: Make Change

# Let's convert a dollar amount into a number of coins. 
# The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
# Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
# For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Concepts Covered
# conditionals, comparisons
# arithmetic
# Version 1
# Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

# Version 2
# Have the user enter a dollar amount (1.36), convert this to the total in pennies. 


# Version 1

# print("let/'s make change!")
# enter_dollar_amt = int(input('Please enter the amount in pennies to make change: (xxx)'))
# quarters = 25
# dimes = 10
# nickles = 5
# pennies = 1

# quarters_output = enter_dollar_amt // quarters
# quarters_remainder = enter_dollar_amt % quarters

# dimes_output = quarters_remainder // dimes
# dimes_remainder = quarters_remainder % dimes

# nickels_output = dimes_remainder // nickles
# nickels_remainder = dimes_remainder % nickles

# pennies_output = nickels_remainder

# print('Your change should be:')
# if quarters_output > 0:
#     print(f'{quarters_output} Quarters')
# if dimes_output > 0:
#     print(f'{dimes_output} Dimes')
# if nickels_output > 0:
#     print(f'{nickels_output} Nickles')
# if pennies_output > 0:
#     print(f'{pennies_output} Pennies')


# Version 2 no fuctions




# print("let/'s make change!")
# enter_dollar_amt = float(input('Please enter the amount in pennies to make change: (x.xx)'))
# whole_number = enter_dollar_amt * 100

# quarters = 25
# dimes = 10
# nickles = 5
# pennies = 1
# quarters_output = whole_number // quarters
# quarters_remainder = whole_number % quarters
# dimes_output = quarters_remainder // dimes
# dimes_remainder = quarters_remainder % dimes
# nickels_output = dimes_remainder // nickles
# nickels_remainder = dimes_remainder % nickles
# pennies_output = nickels_remainder


# if quarters_output > 0:
#     print(f'{int(quarters_output)} Quarters')
# if dimes_output > 0:
#     print(f'{int(dimes_output)} Dimes')
# if nickels_output > 0:
#     print(f'{int(nickels_output)} Nickles')
# if pennies_output > 0:
#     print(f'{int(pennies_output)} Pennies')


#------------------------------------------------------------------------------

# Version 3 with functions

def start():
    print("let/'s make change!")
    enter_dollar_amt = float(input('Please enter the amount in pennies to make change: (x.xx) '))
    whole_number = enter_dollar_amt * 100
    return whole_number

def calc_quarters(whole_number):
    quarters = 25
    quarters_output = whole_number // quarters
    if quarters_output > 0:
        print(f'{int(quarters_output)} Quarters')

def calc_dimes(whole_number):
    quarters = 25
    dimes = 10
    quarters_remainder = whole_number % quarters
    dimes_output = quarters_remainder // dimes
    dimes_remainder = quarters_remainder % dimes
    if dimes_output > 0:
        print(f'{int(dimes_output)} Dimes')
    return dimes_remainder
    
def calc_nickles(dimes_remainder): 
    nickles = 5  
    
    #dimes_remainder = quarters_remainder % dimes
    nickels_output = dimes_remainder // nickles
    if nickels_output > 0:
        print(f'{int(nickels_output)} Nickles')
    
def calc_pennies(dimes_remainder):
    nickles = 5
    pennies_output = dimes_remainder % nickles
    if pennies_output > 0:
        print(f'{int(pennies_output)} Pennies')

def main():
    whole_number = start()
    calc_quarters(whole_number)
    calc_dimes(whole_number)
    calc_nickles(whole_number)
    calc_pennies(whole_number)


main()