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

import random

# Amount of digits can be changed so that you can play with any number of digits
DIGITS = 4

SECRET_CODE = list(random.sample(range(10), DIGITS))

# The game can be changed here so that the player can guess > or < 7 times
GUESSES = 7
WIN = 4


def length_check(user):
    '''
    function: length_check
    paramaters: the user input, a list, checks to see if it is the
    same length as the SECRET_CODE
    returns: a boolean
    '''
    if len(user) == len(SECRET_CODE):
        return True
    else:
        return False


def duplicates(user):
    '''
    function: duplicates()
    parameters: the user input, a list, it checks to see if there are duplicates
    of numbers in the user list
    returns: a boolean
    '''
    if len(user) == len(set(user)):
        return False
    else:
        return True


def split(user):
    '''
    function: split()
    parameters: the user input, a string and turns into a list
    returns: user input, into a list of ints
    '''
    # Need to split first before tuning into an integer
    guess = user.split(' ')
    for i in range(0, len(guess)):
        guess[i] = int(guess[i])
    return guess


def is_digit(user):
    '''
    function: is_digit()
    parameters: the user input, it removes the spaces in the string,
    and verifies that each intput is a digit
    returns: a string, with the space
    '''
    # The spaces from user input are removed here
    user_guess = user.replace(' ', '')

    # Actual digit check is in this code
    user_digit = user_guess.isdigit()
    return user_digit


def validation():
    '''
    functions: validation()
    parameters: none, however this function calls the length_check,
    is_digit, split, and duplicate functions to validate the user input.
    only when the user input is true, it then returns it back to main to 
    play the game
    returns: a validated list of numbers from the user
    '''
    while True:

        # An infinte loop is used to prompt the user until a valid input
        # is given
        user_input = input('\n\nWelcome to the Bulls and Cows!\nEnter 4 guesses'
                           + ' from 0 to 9 inclusive separated by a space. ')

        # Checking to see if the user input 4 digits   
        digit = is_digit(user_input)
        if digit == True:
            user_list = split(user_input)
        else:
            continue

        # Checking to see if the user input is the same length
        # as the secret word
        length = length_check(user_list)
        dupes = duplicates(user_list)
        if dupes == False and length == True:
            break
        else:
            continue
    return user_list
    

def count_bulls_and_cows(SECRET_CODE, user):
    '''
    function: count_bulls_and_cows()
    parameters: this function takes in 2 lists of integers, the computer
    generated SECRET_CODE and the list from the user
    returns: a tuple, the sum of the amount of bulls and cows
    '''
    bulls = 0
    cows = 0

    for i in range(len(SECRET_CODE)):
        if user[i] == SECRET_CODE[i]:
            bulls += 1
        elif user[i] in SECRET_CODE:
            cows += 1
    return bulls, cows


