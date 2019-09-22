# Write a program that asks the user for the number of miles driven and the gallons of gas.
# It should calculate the car's miles-per-gallon and display the result.

# Collect the gallons of gas in the vehicle at the start and assign it to a variable.
gallons_of_gas = float(input('How many gallons of gas were in the vehicle when you started?'))

# Collect the miles the vehicle was driven and assign it to a variable.
miles_driven = float(input('How many miles was the vehicle driven?'))

# Calculate the miles per gallon and assign it to a variable.
# Added round() function to reduce long decimals.
miles_per_gallon = round(miles_driven / gallons_of_gas, 2)

# Print the quotient in a formatted print statement.
print(f'The vehicle gets {miles_per_gallon} miles to the gallon.')
