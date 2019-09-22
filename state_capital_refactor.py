# Import modules used in the program.

import random
import time


class CapitalGuess:
    """ A class to create a game and hold its methods """
    FILENAME = 'StateCapital.txt'          # My path for the txt file, may need changed for your use.
    STATE_CAPITAL = {}                                # Empty dict to hold states and capitals.
    with open(FILENAME, 'r') as f:                    # Opens txt file and reads it into the dict.
        for line in f:                                # Reads line by line stripping white space,
            key = line.strip().split(':')             # and splits on the :.
            STATE_CAPITAL[key[0]] = key[1].strip()    # Assigns state before the : and capital after as key/value.
    CORRECT_GUESS = 0                                 # Class attributes not effected by my reset method.
    INCORRECT_GUESS = 0                               # Keeps pure total of guesses.

    def __init__(self):
        """ Initialize the magic """
        self.guess = ''
        self.guess_right = 0
        self.guess_wrong = 0
        self.guessing = True
        self.selection = self.pick_state_cap()

    def pick_state_cap(self):
        """
        Returns a list of a random chosen
        state/capital pairs in list format
        """
        return list(random.choice(list(self.STATE_CAPITAL.items())))

    def user_guess(self):
        """
        Controls the guessing and tracking
        of guesses, showing guesses and hints.
        """
        print('\n')
        while self.guessing:
            print("""Enter your guess: 
            Enter 'hint' for help(Increases incorrect guesses by 1) or 'quit'.
            You can also enter 'show guess' to see your guess totals.
            """)
            self.guess = input('')
            if self.guess.lower() == self.selection[1].lower():
                self.CORRECT_GUESS += 1
                self.guess_right += 1
                self.guessing = False
                self.win()
            elif self.guess.lower() == 'hint':
                self.INCORRECT_GUESS += 1
                self.guess_wrong += 1
                self.give_hint()
            elif self.guess.lower() == 'show guess':
                self.show_guesses()
            elif self.guess.lower() == 'quit':
                self.quit_game()
            else:
                print('Incorrect. Keep guessing...')
                self.INCORRECT_GUESS += 1
                self.guess_wrong += 1

    def win(self):
        """
        Wins the game and checks if the dict
        runs out of states to end game
        """
        print(f'Correct! {self.selection[1]} was correct!')
        if self.guess_right + self.guess_wrong <= 1:
            print(f'\nYou solved it in {self.guess_right + self.guess_wrong} guess!')
        else:
            print(f'\nYou solved it in {(self.guess_right + self.guess_wrong)} guesses!')

        del self. STATE_CAPITAL[self.selection[0]]           # Deletes each pair after correct guess is made.
        try:                                                 # Tells the program to go to another state if the
            print('Good job, here is another one!\n')        # the dict isn't empty causing an index error.
            self.reset()                                     # If not empty, resets constructor for new key/value pair
        except IndexError:                                   # or lets user know out of states, you did it and ends.
            print('Opps! You ran out of states, great job!')
            self.show_guesses()
            print('Thanks for playing!')
            time.sleep(3)
            quit()
        time.sleep(1)
        self.play()

    def quit_game(self):
        """
        Asks the user if they are
        sure they want to quit and quits
        """
        option = input('\nAre you sure you want to quit? Yes or No?')
        if option.lower() == 'yes':
            quit()
        elif option.lower() == 'no':
            self.play()
        else:
            print('Invalid selection.')
            self.quit_game()

    def play(self):
        """ Starts main loop """

        while self.STATE_CAPITAL.items():
            print(f"\nYour state is {self.selection[0]}!", end='')
            self.user_guess()

    def reset(self):
        """ Resets the game """
        self.__init__()

    def start(self):
        """ Starts the game and intro """
        self.reset()
        print("Let's play a game called...\n")
        time.sleep(2)
        print('''
            \t\t\t*************************************
            \t\t\t*                                   *
            \t\t\t*        Guess That Capital         *
            \t\t\t*                                   * 
            \t\t\t*************************************
            ''')
        option = input('Press [1] to play [2] to quit!')
        if option == '1':
            self.play()
        elif option == '2':
            quit()
        else:
            print('Invalid selection!')
            self.start()

    def give_hint(self):
        """
        Gives the first two letters
        as a hint of the capital
        """
        hints = []
        for char in self.selection[1]:                        # Breaks down the capital in a list of characters
            hints.append(char)                                # appends them to hints list.
        print(hints[0] + hints[1] + ("-" * len(hints[2:])))   # Prints the first two indexes and rest as - .

    def show_guesses(self):
        """ Shows total guesses """
        print(f'You made a total of {self.CORRECT_GUESS} correct guesses')
        print(f'and {self.INCORRECT_GUESS} incorrect guesses.')


if __name__ == '__main__':
    game = CapitalGuess()
    game.start()
