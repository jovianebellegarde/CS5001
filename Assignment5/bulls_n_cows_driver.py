'''
CS5001 Fall 2019
HW 5 Prog 2, Bulls n Cows
Joviane Bellegarde
10/28/19
Referenced sets https://stackoverflow.com/questions/1541797/how-do-i-check-if-
there-are-duplicates-in-a-flat-list for set function
Consulted https://www.journaldev.com/23763/python-remove-spaces-from-string
for replace function
'''

from bulls_n_cows import *

def main():

    # Initializing empty lists to make a nested dictionary, the outer one
    guess_book = {}

    # This code runs a for loop within the range of GUESSES
    for i in range(GUESSES):
        
        # Initializing list for inner dictionary
        entry = {}

        # The user input is returned here after it is validated
        validated_input = validation()

        # The bulls and cows are a tuple, so initializing them this way
        bulls, cows = count_bulls_and_cows(SECRET_CODE, validated_input)

        # Assigning variables for the nested dictionary
        entry['Guess'] = validated_input
        entry['Bulls'] = bulls
        entry['Cows'] = cows
        guess_book['Guess ' + str(i)] = entry
        
        # This code prints out the previous guess history after each user guess
        print('\nYour guess history:')
        for key in guess_book:
            print('Guess:', guess_book[key]['Guess'],'Bulls:', guess_book[key]
                  ['Bulls'], 'Cows:', guess_book[key]['Cows'])

    # This code will print out if the user successfully finds all bulls
    if bulls == WIN:
         print('\nYAS!!! You have won the game! (๑˃̵ᴗ˂̵)ﻭ')

    # This code will print out if the user doesn't find all bulls
    else:
        print('\nOof! What in tarnation?! You didn\'t win. ¯\_(ツ)_/¯')
        
main()
