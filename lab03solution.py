#partial solution



while True:
    x = input('enter something: ')
    print(x)
    if x == 'n':
        break
    elif x == 'a':
        print('you typed a')
    else:
        print(int(x) + 5)

# next

x = 0
while x > 7:
    x = input('enter an integer (q to quit): ')
    print(x)
    if x == 'n':
        break
    else:
        x = int(x)
        print(x + 5)

# next

my_flag = True

while my_flag:
    print('hey there')
    user_input = input('do you want to say hi again?')
    if user_input == 'n':
        my_flag = False