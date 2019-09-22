# Write a function named maximum that accepts two integer values as arguments and returns
# the value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
# the function, the function should return 12. Use the function in a program that prompts the
# user to enter two integer values. The program should display the value that is the greater of
# the two.


def maximum(first_num, second_num):
    """ Returns the greater of two numbers """
    if first_num > second_num:
        return first_num
    elif second_num > first_num:
        return second_num


# Ask the user for two integers.
print("Let's find the greater of two numbers.")
num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

# Call the function with the two integers given to get the answer.
greater = maximum(num1, num2)
print(f'The greater number is: {greater}.')
