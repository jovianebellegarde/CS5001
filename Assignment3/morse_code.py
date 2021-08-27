'''
CS5001 Fall 2019
HW 2 Back to Alpha, Programming 2
Joviane Bellegarde
9/30/19
'''

# Placed the global constant at the top of code
CODE_LIST = [[' ',  '/'], ['A', '.-'], ['B', '-...'], ['C', '-.-.'],
            ['D', '-..'], ['E',  '.'], ['F', '..-.'], ['G', '--.'],
            ['H', '....'], ['I', '..'], ['J', '.---'], ['K', '-.-'],
            ['L', '.-..'], ['M', '--'], ['N', '-.'], ['O', '---'],
            ['P', '.--.'], ['Q', '--.-'], ['R', '.-.'], ['S', '...'],
            ['T', '-'], ['U', '..-'], ['V', '...-'], ['W', '.--'],
            ['X', '-..-'], ['Y', '-.--'],['Z', '--..'], ['0', '-----'],
            ['1', '.----'], ['2', '..---'], ['3', '...--'], ['4', '....-'],
            ['5', '.....'], ['6', '-....'], ['7', '--...'], ['8',  '---..'],
            ['9', '----.'], ['?', '..--..'], ['!', '-.-.--'], ['\'', '.----.'],
            ['"',  '.-..-.'], [',', '--..--']]

ZERO = 0
ONE = 1
THANKS = ('Thank you for using our application.')

def menu():
    '''
    function: menu()
    parameters: none
    returns: choice - user is offered a choice from the options presented
    The choice from the user is then returned to main
    '''

    # Printing so the user knows what to input to use the menu
    print('Welcome to the Morse Code Application. We love dots and dashes!\n' +
          'Choose:\n' + 'A: Alpha to Morse Converter\n' +
          'M: Morse to Alpha Converter\n' +
          'Q: Quit\n')

    
    # Going to assume good input, so will not examine user input
    choice = input('A, M, or Q? ')

    # Going to uppercase the inputso we can match with the available options
    choice = choice.upper()

    return choice


def alpha_morse(message):
    '''
    function: alpha_morse(message)
    parameters: message, a string passed through
    returns: a string, translated into morse code from the string
    that the user put in
    '''
    
    # Have to upper the input to eventually match with the capitilzed letters
    # in the CODE_LIST
    morse = message.upper()

    # Initializing a new string to eventually add the matched letter/morse
    # code pair to it
    morse_message = ''

    # This for loop iterates through the outer list
    for letter in morse:

        # Need to set flag to false, the flag will help python know what to do
        flag = False

        # Iterating through the inner loop
        for symbol in CODE_LIST:

            # Matching the letter the user inputted in with the letter in the
            # CODE_LIST
            if letter == symbol[ZERO]:
                # Adding the morse component of the letter that the user put
                # in to the morse message
                morse_message += symbol[ONE] + ' '

                # If the letter is found, then everything checks out and is
                # flagged as true
                flag = True

        # If flagged as false, it will return to main and print out that the
        # user had put in unrecognizable characters
        if flag == False:
            return False

    return morse_message


def morse_alpha(message):
    '''
    function: morse_alpha(message)
    parameters: a message, a string from the user is passed through
    returns: returns an alphanumeric string from the morse code that the user
    'inputted' in
    '''

    # Need to split the message by white space, there is a white space
    # identifier in the giant code list
    alpha = message.split()

    # Need to initialize a new string to place the alphanumeric words after
    # decoding the morse
    alpha_word = ''

    # Going through the outer list with this for loop
    for symbol in alpha:

        # Need to set the flag to false
        flag = False

        # Going through the inner list with this loop
        for nlist in CODE_LIST:

        # If morse code matches, it will be added to the alph_word list         
            if symbol == nlist[ONE]:
                alpha_word += nlist[ZERO]
                flag = True

        # If an unknown character is entered, the message will return in main
        # and print that the message had unknown characters
        if flag == False:
            return False
        
    return alpha_word
    
        
def main():

    # Calling the menu fuction for the choice
    choice = menu()

    # Initiating an empty string
    message = ''

    # This outer loop takes care of when the user quits out of the entire app
    while True:
        if choice == 'Q':
            print(THANKS)
            break

        
        # This while statement takes care of what to do with the code if user
        # inputs A, M, or Q
        while True:
            if choice == 'A':

                # User inputs their string here
                morse = input('\nWelcome to the Morse Code Application. ' +
                              'We love dots and dashes!\n' +
                              'Enter your alphanumeric messages '
                              'and I\'ll convert ' +
                              'them to Morse.\n' +
                              'Enter :q: to stop and return ' + 
                              'to the main menu.\n')
                
                # This code takes care of the user to go back to the main menu
                # without having to go through the program
                if morse == ':q:':
                    print('Back to the main menu.\n')
                    choice = menu()
                    break

                morse_message = alpha_morse(morse)
                
                # If message not returned false, then the morse message will
                # print out
                if morse_message != False:
                    print('Original message:', morse,
                          '\nTranslated message:', morse_message)

                # If message is false, then this will print
                if morse_message == False:
                    print('Your message had unknown characters and',
                          'I couldn\'t convert it. Please try again.')

                    # The user can also go back to the menu after going through
                    #the application
                    if morse_message == ':q:':
                        print('Back to the main menu.\n')
                        choice = menu()
                        break

            

            if choice == 'M':

                
                # User inputs thier string here
                alpha = input('Insert a space between signals and / between ' +
                              'words.\nEnter morse messages and I\'ll convert ' +
                              'them to alphanumeric.\n' +
                              'Enter :q: to stop and return to the main menu.'
                              '\n')

                # The user can choose to quit to the main menu instead of
                # going through the entire program 
                if alpha == ':q:':
                    print('Back to the main menu.\n')
                    choice = menu()
                    break

                alpha_message = morse_alpha(alpha)

                
                # If message is found in the list, this code runs
                if alpha_message != False:
                    print('Original message:', alpha,
                          '\nTranslated message:', alpha_message)

                
                # If the message is false, then this code runs
                if alpha_message == False:
                    print('Your message had unknown characters and',
                          'I couldn\'t convert it. Please try again.')

                    # If the user wants to quit after translating, this code
                    # runs
                    if alpha_message == ':q:':
                        print('Back to the main menu.\n')
                        choice = menu()
                        break

main()
