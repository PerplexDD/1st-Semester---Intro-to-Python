# Many financial experts advise that property owners should insure their homes or buildings
# for at least 80 percent of the amount it would cost to replace the structure. Write a program
# that asks the user to enter the replacement cost of a building and then displays the
# minimum amount of insurance he or she should buy for the property.


def insurance(amount):
    """
    Takes in an amount that it would cost to replace
    a building and outputs the insurance minimum needs.
    """
    return amount * .80


# Asks the user for the cost of replacement.
replace_cost = float(input('Please enter the replacement cost of your structure: '))

# Prints out the minimum insurance needed for the cost they entered.
print('The minimum estimated amount of insurance needed for $',
      (format(replace_cost, ',.2f')) + ' is $',
      (format(insurance(replace_cost), ',.2f')) + ' of coverage.')
