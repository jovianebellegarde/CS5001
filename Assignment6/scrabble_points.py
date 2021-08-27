'''
CS5001 Fall 2019
HW 6 Programming 1 - Scrabble Fxns
Joviane Bellegarde
11/15/19
'''

from wordlist import *
import random


def menu():
    '''
    function: is_valid_word():
    parameters: none
    returns: a list 
    '''
    CHOICES = ['D', 'W', 'P', 'Q']
    word_list = get_wordlist()

    choice = ''
    while choice not in CHOICES:
        choice = input('\nChoose:\nD: Draw letter from the bag\n' +
                       'W: Make a word from the letters in play\n' +
                       'P: Print all words played so far\nQ: Quit\n').upper()
        return choice


    
def bag_of_letters(frequency):
    '''
    function: bag_of_letters(frequency)
    parameters: a dictionary, frequency of letters
    returns: a list of the frequency of letters
    '''
    # Initializing an empty list
    frequency_list = []

    # Iterating through the keys in the dictionary to add the letters to list
    # according to their frequency 
    for key in frequency:
        for i in range(frequency[key]):
            frequency_list.append(key)
    return frequency_list



def draw_letters(bag, bag_amount):
    '''
    function: draw_letters(bag, bag_amount)
    parameters: a list (bag), and an integer (bag_amount)
    returns: a list of 7 words to make a word from
    '''
    seven_letters = random.sample(bag, bag_amount)
    seven_letters_list = list(seven_letters)
    for i in seven_letters_list:
        bag.remove(i)
    return seven_letters_list

    

def is_valid_word(user_word, word_list, letters, used_words):
    '''
    function: draw_is_valid_word(user_word, word_list, letters, used_words)
    parameters: a string (user word), the list of strings (word list),
    a list of 7 strings (letters), a dictionary of strings (used_words)
    returns: a boolean, True if the word is valid, False if invalid
    '''
    # Checking to see if the user_word is in the word list
    if user_word in word_list:

        # Checking to see that the user word was not already used
        if user_word not in used_words:

            # Going through each letter in the user word to see if the letters
            # the user gave us is in the list of 7 letters that we have and
            # will use the blank tile if the letter is not in the list
            for letter in user_word:
                if letter not in letters:
                    if '_' in letters:
                        letters.remove('_')
                    else:
                        return False
            return True
        
    return False


    
def get_word_value(user_word, points):
    '''
    function: get_word_value(user_word, points)
    parameters: a validated user word, a dictionary
    returns:
    '''
    # Getting the numerical value from the dictionary to return the point
    # value for each letter back to main
    count = 0
    for letter in user_word:
        count += points[letter]
        
    return count
        
