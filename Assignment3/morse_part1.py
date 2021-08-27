'''
CS5001 Fall 2019
HW 3 Programming 1 - Morse
Joviane Bellegarde
9/30/19
'''

# Placed the global constant at the top of code
CODE_LIST = [[' ',  '/'], ['A', '.-'], ['B', '-...'],
             ['C', '-.-.'], ['D', '-..'], ['E',  '.'],
['F', '..-.'], ['G', '--.'], ['H', '....'], ['I', '..'], ['J', '.---'],
['K', '-.-'], ['L', '.-..'], ['M', '--'], ['N', '-.'], ['O', '---'],
['P', '.--.'], ['Q', '--.-'], ['R', '.-.'], ['S', '...'], ['T', '-'],
['U', '..-'], ['V', '...-'], ['W', '.--'], ['X', '-..-'], ['Y', '-.--'],
['Z', '--..'], ['0', '-----'], ['1', '.----'], ['2', '..---'], ['3', '...--'],
['4', '....-'], ['5', '.....'], ['6', '-....'], ['7', '--...'],
['8',  '---..'], ['9', '----.'], ['?', '..--..'], ['!', '-.-.--'],
['\'', '.----.'], ['"',  '.-..-.'], [',', '--..--']]

# Changed positions to letters to avoid using literals
ZERO = 0
ONE = 1

def translate(message):
    ''' Function: This function takes the string from main, runs the characters
                  in the string and matches to the code list.
                  If the match is found, then the morse portion is returned
                  to main and printed. If the match isn't found,
                  then the function returns the value as false and let's
                  the user know that the characters are unknown.
        Parameters: A string from the user.
        Returns: A string, the [1] position from the nested list.
    '''
    # Need to 'upper' my string because the list has all capital letters
    message = message.upper()
    
    # Need to initialize a new string to add the morse characters into it
    new_message = ''
    for letter in message:
        # Flagged this condition to False so that if the symbol in CODE_LIST
        # isn't found, then it would go back to main and print that it is an
        # unknown.
        flag = False
        # Iterating through the out list
        for symbol in CODE_LIST:

            # Iterating through the inner list
            if letter == symbol[ZERO]:
                # adding space for morse code
                new_message += symbol[ONE] + ' '
                flag = True
                
        # If the message is returned False, then this code would run letting the
        # user know that there are unknown characters
        if flag == False:
            print('Your message had unknown characters and',
                  'I couldn\'t convert it. Please try again.')
            
            return False
    
    return new_message
    
            
def main():
    
    # Initializing the message to use in the while loop
    message = ''
    
    # While loop is to prompt the user each time until they :q: the program
    while message != ':q:':
        message = input('\nWelcome to the Morse Code Application! ' +
                        'We love dots and dashes.\nEnter your alphanumeric ' +
                        'messages and I\'ll convert them to Morse.\n'
                        'Enter :q: to stop and return to the main menu.\n')
        
        # The program will stop running here if the user enters :q:
        if message == ':q:':
            print('Thanks for using our app!\n',
                  translate('Thanks for using our app!'))
            break
    
        # Calling the function here 
        morse = translate(message)
        
        # This code will run because this was flagged false in my function
        if morse != False:
            print('Your original message is:', message,
                  '\nYour message in morse code is:', morse)
            
main()
