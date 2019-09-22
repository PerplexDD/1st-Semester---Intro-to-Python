# Write a program that gets a string containing a person’s first, middle, and last names, and
# then display their first, middle, and last initials. For example, if the user enters John William Smith
# the program should display J. W. S.

# Ask the user for their full name and split the string.
name = input('Enter your full name(first, middle, last): ').split()

# Start a for loop to iterate over the separated name.
for char in name:
    sep = char[0]                            # Assigns a new variable for index 0 of each name.
    print(sep.title().join(' .'), end='')    # Prints each 0 index, capitalized and joined with a . on one line.
