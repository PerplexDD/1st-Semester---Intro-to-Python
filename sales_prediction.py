# Write a program that asks for the users to enter the projected amount of total sales and then
# displays the profit made from that amount.

# Assign a variable for the input from the user.
annual_sales = float(input("What is your company's projected amount of annual total sales?"))

# Assign a variable for the equation of annual_sales multiplied by 23%
annual_profit = annual_sales * .23

# Print out the product in a formatted print statement.
print("The company's annual profit is $", (format(annual_profit, ',.2f')))
