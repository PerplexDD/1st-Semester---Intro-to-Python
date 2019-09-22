# Assume that a file containing a series of integers is named numbers.txt and exists on the computer.
# Write a program that displays all of the numbers in the file.

# Assign the txt file a variable including the path to the file.
filename = 'numbers.txt'

# Using with open to let python control opening and closing the file as read only
# and assigning that operation to f.
with open(filename, 'r') as f:
    lines = f.readlines()          # Assign the function readlines() to a new variable.
    print('The integers in the file are: ')
    for line in lines:             # Start a for loop to loop through each line.
        print(line.strip())        # Print each line and strip any white space.
