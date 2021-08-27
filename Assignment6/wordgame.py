'''
CS5001 Fall 2019
HW 6 Programming 2 - Scrabble/Word Game Driver
Joviane Bellegarde
11/15/19
'''

from scrabble_points import *

POINTS = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1,
          'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
          'F': 4, 'H': 4,'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
          'Q': 10, 'Z': 10}


FREQUENCY = {'J': 1, 'K': 1, 'Q': 1, 'X': 1, 'Z': 1, 'B': 2, 'C': 2, 'F': 2,
             'H': 2, 'M': 2, 'P': 2, 'V': 2, 'W': 2, 'Y': 2, '_': 2, 'G': 3,
             'D': 4, 'L': 4, 'S': 4, 'U': 4, 'N': 6, 'R': 6, 'T': 6, 'O': 8,
             'A': 9, 'I': 9, 'E': 12}

BAG_AMOUNT = 7

def main():
    
    print('Welcome to Word Game which is a cross between Scrabble.' +
          ' It\'s a one-player game. The player attempts to ' +
          'create words from 7 randomly-chosen letters, and they' +
          ' are awarded points according to the value of each' +
          'letter.\n')
    
    # Initializing an empty dictionary to store used words
    used_words = {}

    # Setting score to 0, will need to find the score at the end of the game
    score = 0

    # Making my bag of letters from a dictionary into a list of 7 letters to
    # play with
    my_bag = bag_of_letters(FREQUENCY)

    # Prompting the user to make a choice of D, W, P, Q
    while True:
        choice = menu()
        if choice == 'Q':
            print('You have quit the game.\n')
            break

        # Player draws letter here, a list of 7 letters
        elif choice == 'D':
            letters = draw_letters(my_bag, BAG_AMOUNT)
            print('You can make a word from these letters:\n' + str(letters))
            if len(letters) < BAG_AMOUNT:
                print('You can\'t make any more words. Game has ended.')
                break
            
        # Play chooses to enter a word in this code
        elif choice == 'W':
            # print(letters)
            word_list = get_wordlist()
            user_input = input('\nEnter a word to play ' +
                               'the Word Game.\n').upper()
            valid_input = is_valid_word(user_input, word_list, letters,
                                        used_words)

            # If user input is True, then the game continues, points obtained,
            # and score is added
            if valid_input == True:

                # Obtaining the user points for the words that they play
                points = get_word_value(user_input, POINTS)
                used_words[user_input] = points
                score += points
                print('Your score is:', score)
            else:
                print('Enter a valid word.')

        # If user chooses P, then all the words they used will print
        elif choice == 'P':
            for key in used_words:
                print('Here are the words that you used:', key)        
    
main()
