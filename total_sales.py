# Write a program that asks the user to enter a store's sales for each day of the week.
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week and
# display the result.

# Make a list of days of the week to loop through.
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday',
                ]

# Make an empty list to store each days total sales to.
total_sales = []
total = 0

# Print a simple statement of what this program does for the user.
print("Calculate your store's weekly sales with this simple program.\n")

# Begin the for loop to go through and get input for sales amounts daily.
for days in days_of_week:
    sales = float(input(f'Enter the total sales for {days}: '))
    total_sales.append(sales)

# Add all the amounts stored in the list together and assign to a variable.
for num in total_sales:
    total += num

# Display the result in a statement to inform the user.
print("Your store's weekly sales amounts to $", format(total, ',.2f') + ".")
