# Write a program that asks the user to enter a distance in kilometers, and then converts that
# distance to miles. The conversion formula is as follows:
# Miles = Kilometers x 0.6214


def kilo_to_miles(kilo):
    """
    Defines a function to convert
    kilometers to miles
    """
    return kilo * 0.6214


# Ask the user for the amount of kilometers to convert.
kilometers = float(input('Enter the amount of kilometers to be converted into miles: '))

# Displays the amount of kilometers converted to miles.
print(f'{kilometers} kilometers are equal to', format(kilo_to_miles(kilometers), '.3f') + ' miles')
