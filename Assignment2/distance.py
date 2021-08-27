'''
CS5001 Fall 2019
HW 2 Programming 2: Manhattan
Joviane Bellegarde
9/22/19
'''

def absolute(num):
    ''' Function: takes one number and multiplies by -1 if less than 0
        to obtain absolute value
        Parameters: a number (float or int) is passed through this function
        Returns: a number (float or int) that is absolute
    '''
    if num >= 0:
        return num
    else:
        num = num * (-1)
        return num


def manhattan(x1, y1, x2, y2):
    ''' Function: takes in 4 numbers (float or int), calculates the distance
        between 2 coordinates
        Parameters: 4 numbers, 2 sets of coordinates (x1, y1, x2, y2)
        Returns: a float, the Manhattan distance between 2 coordinates
    '''
    coordinate_1 = absolute(x2 - x1)
    coordinate_2 = absolute(y2 - y1)
    distance = coordinate_1 + coordinate_2
    return distance

def euclidean(x1, y1, x2, y2):
    ''' Function: takes in 4 numbers (float or int), calculates the distance
        between 2 coordinates
        Parameters: 4 numbers, 2 sets of coordinates (x1, y1, x2, y2)
        Returns: a float, the euclidean distance between 2 coordinates
    '''
    coordinate_1 = absolute(x2 - x1)
    coordinate_2 = absolute(y2 - y1)
    distance = ((coordinate_1) ** 2 + (coordinate_2) ** 2) ** (1/2)
    return distance
