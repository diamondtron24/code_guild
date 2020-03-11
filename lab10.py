# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

# The code below shows how to loop through an array, and prints the elements one at a time.

# nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

# nums = []
# nums.append(5)
# print(nums)
# Below is an example input/output:

# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4

# Version 1

# nums = [5, 0, 8, 3, 4, 1, 6]

# x = 0
# y = 0

# for num in nums:
#     x = x + num
# print(x)

# for i in range(len(nums)):
#     y = y + 1   
# print(y)

# print(x / y)


# Version 2

# nums = []

# a = 0
# x = 0
# y = 0

# while a == 0:
#     numbers = input('Please select a number to average in the list: If done appending please type done - ')
#     if numbers == 'done':
#         break
#     else:
#         nums.append(numbers)

# for num in nums:
#     x = x + int(num)
# print(x)

# print(nums)



# for i in range(len(nums)):
#     y = y + 1   
#     print(y)

# print(x / y)

def list(nums):
    a = 0
    while a == 0:
        numbers = input('Please select a number to average in the list, If done appending the list please type done: ')
        if numbers == 'done':
            break
        else:
            nums.append(numbers)


def count(nums):
    x = 0
    for num in nums:
        x = x + int(num)
    print(f'The total of your list is: {x}')
    return x

def calc(nums, number_1):
    number_2 = 0
    for i in range(len(nums)):
        number_2 = number_2 + 1   
    print(f'The total numbers in your list is: {number_2}')
    answer = number_1 / number_2
    print(f'Your average number is {answer}')   
    

def main():
    nums = []
    list(nums)  
    print(nums)
    number_1 = count(nums)     
    calc(nums, number_1)
    

main()