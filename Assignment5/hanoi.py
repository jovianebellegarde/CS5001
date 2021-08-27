'''
CS5001 Fall 2019
HW 5 Prog 1, Hanoi
Joviane Bellegarde
10/27/19
'''

from hanoi_viz import *

# Constants: 3 annoying bosses from the Final Fantasy XIV video game (-_-)
TOWER1 = 'Susano'
TOWER2 = 'Suzaku'
TOWER3 = 'Shinryu'

# Initializing a list of disks, numbered 1 through 8
DISKS = [1, 2, 3, 4, 5, 6, 7, 8]

def move_tower(num_disks, tower1, tower2, tower3, towers):
    '''
    function: move_tower - recursive function also calling the move_disk
              function
    parameters: num_disks - this function takes in 5 parameters, an int,
                3 strings, and a dictionary with lists
    returns: nothing, but prints output of the disks/towers hanoi game
    '''
    # Base case, this will move the remaining disk to the destination
    # Recursion will stop once base case is reached
    if num_disks < 2:
        move_disk(tower1, tower2, towers)

    # For disks number >= 2, but < number of disks, this code will run
    else:
        move_tower(num_disks - 1, tower1, tower3, tower2, towers)
        move_disk(tower1, tower2, towers)
        move_tower(num_disks - 1, tower3, tower2, tower1, towers)


def main():
    # The while loop is to prompt the user until they enter a valid response
    while True:
        user = input('Enter a number from 1 to 8 to play. ')

        # Checking to see that the user input is a digit/valid
        user_input = user.isdigit()
        if user_input == True:

            # Need to turn the original user input into an integer or else an
            # infinite while loop will occur in the code
            user_number = int(user)
            if user_number in DISKS:
                break

    # The initialize tower function is initialized and called here
    towers_initialized = initialize_towers(user_number, TOWER1, TOWER2, TOWER3)

    # Move tower function is called, passing towers_initialized as a parameter
    move_tower(user_number, TOWER1, TOWER2, TOWER3, towers_initialized)


main()
