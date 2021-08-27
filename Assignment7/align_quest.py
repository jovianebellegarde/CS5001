'''
CS 5001 Fall 2019
HW 7 Align Quest
Joviane Bellegarde
11/25/19

***Citations***

Enumerate fxn: consulted https://stackoverflow.com/questions/31787752/python
-remove-entry-in-a-nested-list

with statement: https://stackoverflow.com/questions/8011797/open-read-and-
close-a-file-in-1-line-of-code
'''

from room import *

DIRECTION = ['N', 'E', 'W', 'S']
DO_THINGS = ['I', 'L', 'U', 'T', 'D', 'T']


def read_file(file_name, mode):
    '''
    function: read_file
    parameters: file_name, and mode, 2 strings, a text file and the mode that
                is being used
    returns: a nested list from the text file
    '''
    # Initiating an empty list to store the lists of information that is being
    # passed through
    file_list = []

    # Opening the file here in reading mode using a 'with' statement
    # Python will automatically close the file each time when running this code
    with open(file_name, mode) as file:

        # Assigning a list of the text from the file
        read_file = file.readlines()

        # This loop strips and splits the file into a nested list
        for i in read_file:
            stripped_file = i.strip('\n')
            split_file = stripped_file.split('|')
            file_list.append(split_file)

        # This loop 'throws away' the metadata descriptions at the top of each
        # file
        for i, j in enumerate(file_list):
            if j[0] == 'METADATA' or j[0] == '0':
                file_list.remove(file_list[i])
                
    return file_list


def menu():
    '''
    function: menu()
    paramters: none
    returns: choice, a string, 'Y' or 'N', that the user enters
    '''
    choice = ''
    while choice not in DIRECTION or DO_THINGS:

        # User inputs a choice here
        choice = input('\nEnter N, S, E, or W to move in those directions.\n' +
                       'I for Inventory, L to look at somehting, U to Use ' +
                       '<an item>.\nT to Take an item, D to Drop an item.\n' +
                       'Q to quit and exit the game.\nYour choice: ').upper()
        
        return choice


def room_dict_fxn(class_name, lst):
    '''
    function: rooms_dict
    parameters: class, and a list of strings containing room information:
                number ID, description, adjacent rooms, puzzles, monsters,
                items, and pictures
    returns: an object and a dictionary
    '''
    # Initializing empty dictionary
    lst_dict = {}
    
    # Using nested loop to access the index within a single list nested in
    # larger list
    for i in range(len(lst)):
        for j in range(len(lst)):
            
            # Passing in these variables for these parameters from the Rooms
            # class to make rooms object: number ID, name, description,
            # adjacent rooms, and pictures
            lst_object = class_name(lst[i][0], lst[i][1], lst[i][2], lst[i][3],
                                    lst[i][6])

            # Room dictionary, with room number as the key, and room object as
            # the value
            lst_dict[lst[i][0]] = lst_object

    return lst_dict


def item_dict_fxn(class_name, lst):
    '''
    function: items_dict
    parameters: class, and a list containing item information: number ID, name,
                description, weight, value, uses remaining
    returns: an object and a dictionary
    '''
    # Initializing empty dictionary 
    lst_dict = {}
    
    # Using nested loop to access the index within a single list nested in
    # larger list
    for i in range(len(lst)):
        for j in range(len(lst)):
            
            # Passing in these variables for these parameters from the
            # Item class to make item object: number, name, description, weight,
            # value, and use
            lst_object = class_name(lst[i][0], lst[i][1], lst[i][2],
                                    lst[i][3], lst[i][4], lst[i][5])

            # Item dictionary with item name as the key, and item object as the
            # value
            lst_dict[lst[i][1]] = lst_object

    return lst_dict


def puzz_n_mon_dict_fxn(class_name_1, class_name_2, lst):
    '''
    function: puz_n_mon
    parameters: class name, and a list of strings containing information 2
                types of information. For puzzles: name, description, target,
                active, affects_target, solution, and effect. For monsters:
                name, description, target, active, affects_target, solution,
                effect, can_attack, and attack.
    returns: an object and a dictionary
    '''
    # Initializing empty dictionary
    lst_dict = {}
    
    # Using nested loop to access the index within a single list nested in
    # larger list
    for i in range(len(lst)):
        for j in range(len(lst)):

            # If the last element in the list is an asterisk, that means that
            # the object is a puzzle
            if lst[i][-1] == '*':
                
                # Passing in these variables for these parameters from the
                # Puzzle class to make puzzle object: name, description,
                # target, active, affects_target, solution, and effect
                lst_object = class_name_2(lst[i][0], lst[i][1], lst[i][5],
                                          lst[i][2], lst[i][3], lst[i][4],
                                          lst[i][6])

                # Puzzle dictionary, with puzzle name as the key, and puzzle
                # object as the value
                lst_dict[lst[i][0]] = lst_object

            # Last element in the list is not an asterisk, meaning that the
            # object is a monster
            else:
                
                # Passing in these variables for these parameters from the
                # Monster class to make monster object: name, description,
                # target, active, affects_target, solution, effect, can_attack,
                # and attack
                lst_object = class_name_1(lst[i][0], lst[i][1], lst[i][5],
                                          lst[i][2], lst[i][3], lst[i][4],
                                          lst[i][6], lst[i][7], lst[i][8])

                # Monster cictionary, with monster name as the key, and monster
                # object as the value
                lst_dict[lst[i][0]] = lst_object

    return lst_dict


def default(room_list, item_list):
    print('You are now in the: ' + room_list[0][1] + '\n' + room_list[0][2] +
          '\nA ' + item_list[3][1] + ' is here in the room.')


def direction(DIRECTION, choice, room_list):
    for i in range(len(room_list)):
        for j in range(len(room_list)):
            pass

    room_list[i][3] = room_list.split(' ')
    for i in range(len(room_list)):
        for j in range(len(room_list)):
            room_list[i][j] = int(room_list[i][j])
    return room

    pass

def do_things(DO_THINGS, choice):
    pass


def main():
    print('\n***************************************************')
    print('*                   Align Quest                   *')
    print('*               C5001 Homework # 7                *')
    print('***************************************************\n')
    print('Welcome to Align Quest! You are in a mansion and will need to ' +
          'find a way out of it.\n')

    # Opening/saving the rooms, items, and puzzles and monsters files
    room_list = read_file('aquest_rooms.txt', 'r')
    item_list = read_file('aquest_items.txt', 'r')
    puzz_n_mon_list = read_file('puzzles_n_monsters.txt', 'r')

    # Initializing room, item, and puzzle/monster dictionaries by passing their
    # lists through their respective functions
    room_dictionary = room_dict_fxn(Room, room_list)
    item_dictionary = item_dict_fxn(Item, item_list)
    puzz_n_mon_dictionary = puzz_n_mon_dict_fxn(Monster, Puzzle,
                                                puzz_n_mon_list)
    '''
    # Initializing the game object
    game = Game(item_dictionary, room_dictionary, puzz_n_mon_dictionary,
                target = '')

    game = Game(tem_dictionary, room_dictionary, puzz_n_mon_dictionary,
                target = '
    '''

    # Initializing the courtyard to print out
    courtyard = default(room_list, item_list)

    # While loop prompts the menu, and user choice
    # User can drop, look, take, or use an item or user can move instead to
    # another room. Can have only one room in each direction, can repesent in 3
    # ways, can have a room here, no room, or room is blocked.
    while True:
        
        # Calling the menu function here to return user choice back
        choice = menu()
        if choice == 'Q':
            print('You have chosen to quit the game.')
            break
        elif choice in DIRECTION:
            print(choice + ' direction\n')
            moving = direction(DIRECTION, choice, room_list)
            print(moving, 'moving')
            break
        elif choice in DO_THINGS:
            print(choice + ' do things\n')
            break
        
    # can use a list to print out the classes and objects
    
main()
