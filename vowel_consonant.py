# Write a program with a function that accepts a string as an argument and returns the number of vowels
# the string contains. The application should have another function that accepts a string and returns the
# number of consonants. The application should let the user enter a string and should display the number of
# consonants and vowels.


def show_vowel(string, vowels):
    """ Shows the vowels in a string """
    # Writing statements such as this help me build list comprehensions.
    # Checks the string for the vowels in list vowel and if vowels in vowel
    # counts it and displays it in a print statement.
    vow_count = [vow for vow in string if vow in vowels]
    print('The vowels in your statement are:')
    for letter in vow_count:
        print(letter, end=' ')


def count_vowel(string, vowels):
    """ Counts the amount of vowels in a statement """
    vow_count = [vow for vow in string if vow in vowels]
    return len(vow_count)


def show_consonant(string, vowels):
    """ Shows the consonants in the string """
    # Writing statements such as this help me build list comprehensions.
    # Checks the string for the vowels in list vowel and if vowels in vowel
    # counts it and displays it in a print statement.
    cons_show = [cons for cons in string if cons not in vowels]
    print('The consonants in your string are:')
    for letter in cons_show:
        print(letter, end=' ')


def count_consonant(string, vowels):
    """ Counts the amount of consonants """
    cons_count = [cons for cons in string if cons not in vowels]
    return len(cons_count)


# Asks user input for a string.
user_string = input('Please type in a word: ')

# Make a list of vowels covering both cases.
vowel = 'aAeEiIoOuU'

# Run function with user input compared against the list of vowels.
show_vowel(user_string, vowel)
numb_vowel = count_vowel(user_string, vowel)
print(f'\nVowels: {numb_vowel}')

# Run function with user input to find consonants.
show_consonant(user_string, vowel)
numb_cons = count_consonant(user_string, vowel)
print(f'\nConsonants: {numb_cons}')
