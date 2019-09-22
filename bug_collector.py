# Write a program that keeps a running total of bugs collected during a seven day period. The loop should ask the user
# for the number of bugs collected each day, when the loop is finished, display the total of bugs collected.

# Set a variable to 0 to start.
bugs_collected = 0

# Start the for loop to iterate the days of the week and ask how many bugs for the day collected.
for day in range(1, 8):
    how_many_bugs = int(input(f'How many bugs did you collect on day {day}?'))

    # Adds running total of bugs per day to total bugs.
    bugs_collected += how_many_bugs

# Print total amount of bugs collected.
print(f'You collected a total of {bugs_collected} bugs for the week! Great job!')
