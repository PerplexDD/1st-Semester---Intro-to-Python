# Write a program that uses nested for loops to collect data and collect the average rainfall over a period
# of years. The program should first ask for the number of years. The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask
# The user for inches of rainfall for that month. After all iterations, the program should display the number
# of months, total inches of rainfall and the average rainfall per month for the entire period.

# Set a variable for rainfall to 0.
rainfall = 0

# Asking the user for how many years.
years = int(input('How many years did you collect data for?'))

# Starting the for loop.
for year in range(years):
    for month in range(1, 13):
        rain_per_month = int(input(f'How many inches of rainfall were collected in month {month}?'))

        # Adds into running total of rain per month into rainfall
        rainfall += rain_per_month

# Convert years entered into months.
month_total = years * 12

# Get the average rainfall with a simple equation.
average_rainfall = rainfall / month_total

# Print out the results.
print(f'The average rainfall for {month_total} months was {average_rainfall} and '
      f'the total amount of rainfall was {rainfall} inches for this period.')
