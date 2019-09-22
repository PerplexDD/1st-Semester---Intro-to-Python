# Assume that a file containing a series of names (as strings) is named names.txt and exists
# on the computer’s disk. Write a program that displays the number of names that are stored
# in the file (Hint: Open the file and read every string stored in it. Use a variable to keep a count
# of the number of items that are read from the file.) Here is a copy of names.txt

# Assign a variable the txt file including path where located.
filename = 'names.txt'

# Using with open to let python open and close the text file.
with open(filename, 'r') as f:
    lines = list(f.readlines())                                           # Assign readlines() to a variable.
    print(f'There are {len(lines)} names in the file and they are: ')     # Print the count of names in file.
    for line in lines:                                                    # For loop to display each name neatly.
        print(line.title().strip())                                       # Print and strip off any white space.
