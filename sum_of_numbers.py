# Write a program with a while loop that asks the user to enter a series of positive numbers. The user should
# enter a negative number to signal the end of the series. After all the positive numbers have been entered,
# the program should display their sum.

# There are two ways of doing this I know of I put in both, one commented out and the other active.

# Set a empty variable to store the integers given by user.
# numbers = []

# Set variable at 0 for adding to throughout loop.
number_sum = 0

print('Lets calculate a sum from positive integers, '
      'enter a negative integer to end and see the sum.')

# Start a while loop.
while True:

    # Ask the user for integers.
    number = int(input('Enter a number: '))

    # Set a conditional block to take in numbers and end loop if a negative integer is given.
    if number < 0:
        # Once a negative integer is given take the sum of all the numbers.
        # Print a statement giving the sum and break the loop.
        # number_sum = sum(numbers) if done with the list method.
        print(f'The sum of your numbers is {number_sum}.')
        break
    elif number >= 0:
        # Adds the numbers entered by the user into the list numbers.
        # numbers.append(number) if using list method.
        number_sum += number
