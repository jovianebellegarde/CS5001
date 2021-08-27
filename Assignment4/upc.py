'''
CS5001 Fall 2019
HW 4 Prog 1, UPC
Joviane Bellegarde
10/13/19
'''

# Used global variables to get rid of any literals inside the functions
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
TEN = 10


def is_valid_upc(num_list):
    '''
    function: is_valid_upc, checks to see if the UPC is valid
    parameters: a list of integers
    returns: a boolean, if the UPC is a multiple of 10
    '''

    # Edge case 1: if length of num_list is less than 2, UPC is invalid
    if len(num_list) < TWO:
        return False
    
    # Edge case 2: if all digits in the num_list are 0s, UPC is invalid
    count = ZERO
    for i in range(len(num_list)):
        if num_list[i] == ZERO:
            count += ONE
    if count == len(num_list):
        return False

    # This step reverses the UPC numbers
    reversed_num_list = num_list[::-ONE]

    # This code is for if the number is even or odd
    # Sum of results is then checked if multiple of 10
    count_even_odd = ZERO
    for i in range(len(reversed_num_list)):

        # This sum is for the numbers in the even positions, adding 0 to them
        if i % TWO == ZERO:
            count_even_odd += reversed_num_list[i]

        # This sum is for multiplying the numbers in the odd positions by 3
        else:
            count_even_odd += reversed_num_list[i] * THREE
    
    # Checking to see if the UPC is a multiple of 10
    if count_even_odd % TEN == ZERO:
        return True
    else:
        return False
