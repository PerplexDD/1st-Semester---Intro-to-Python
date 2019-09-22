# Write a program that asks the user to enter the weight of a package and then displays the shipping charges.

# Get the user's input for the weight of the package.
package_weight = float(input('How heavy is the package to be shipped?'))

# Start an if elif chain for the different pricing options.
if package_weight <= 2:
    print('Your shipping cost will be $1.50.')
elif 2 < package_weight <= 6:
    print('Your shipping cost will be $3.00.')
elif 6 < package_weight <= 10:
    print('Your shipping cost will be $4.00')
else:
    print('Your shipping cost will be $4.75.')
