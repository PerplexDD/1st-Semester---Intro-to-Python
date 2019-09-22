# Write a program that generates a seven-digit lottery number. The program should generate
# seven random numbers, each in the range of 0 through 9, and assign each number to a list
# element using a loop. (Random numbers were discussed in Chapter 6.) Then write another
# loop that displays the contents of the list.

# Import random module.
import random

# Make a list of 7 random integers from range of 0 - 9 using
# a list comprehension, this takes increases readability.
# It also takes less lines than a for loop and .append().
lottery_numbers = [random.randint(0, 9) for i in range(7)]

# Print a statement to let the user know what the numbers are.
print('Your lucky lottery numbers are: ')

# Use a for loop to go through each integer in the list and the end parameter
# to replace the usual built in \n at the end of a print statement to show the
# numbers in a single line.
for numb in lottery_numbers:
    print(numb, end=' ')
