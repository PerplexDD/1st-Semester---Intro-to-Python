# One foot equals 12 inches. Write a function named feet_to_inches that accepts a
# number of feet as an argument, and returns the number of inches in that many feet. Use the
# function in a program that prompts the user to enter a number of feet and then displays the
# number of inches in that many feet.


def feet_to_inches(feet):
    """ Converts feet to inches """
    convert = feet * 12
    return convert


# Ask the user for how many feet they would like to convert.
how_many_feet = float(input('Enter the amount of feet to convert to inches: '))

# Call the function to convert the given amount of feet into inches.
conversion = feet_to_inches(how_many_feet)

# Displays the amount of feet and the converted amount of inches.
print(f'Feet: {how_many_feet}')
print(f'Inches: {feet_to_inches(how_many_feet)}')
