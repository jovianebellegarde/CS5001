'''
CS5001 Fall 2019
HW 4 Prog 2, MBTA
Joviane Bellegarde
10/13/19
'''

RED_LINE = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard", "Porter",
            "Davis", "Alewife"]


def is_valid_station(station):
    '''
    function: is_valid_station(station)
    paramaters: a list of strings
    returns: a boolean, True if station is in RED_LINE, False if not
    '''
    for i in range(len(RED_LINE)):
        if RED_LINE[i] == station:
            return True
    else:
        return False
    

def get_direction(starting, ending):
    '''
    function: get_direction
    parameters: 2 strings, start and end stations
    returns: first or last stop on Orange line, or no destination found if
    it does not exist in the list
    '''
    # This code runs to see if the station is even valid by looking at its
    # position in the list
    if is_valid_station(starting) == True and is_valid_station(ending) == True:
        for i in range(len(RED_LINE)):
           if starting == RED_LINE[i]:
                answer_1 = i
        for i in range(len(RED_LINE)):
            if ending == RED_LINE[i]:
                answer_2 = i
    elif is_valid_station(starting) == False or \
            is_valid_station(ending) == False:
        return 'No destination found.'

    # This code runs to give us the direction to Alewife or Ashmont and giving
    # a string
    # Position 1 is then subtracted from position 2
    # If the position is positive, traveling towards Ashmont
    # If position is negative, traveling towards Alewife
    answer = answer_1 - answer_2
    if answer > 0:
        return 'Ashmont'
    elif answer < 0:
        return 'Alewife'
    else:
        return 'No destination found.'


def get_num_stops(starting, ending):
    '''
    function: get_num_stops(starting, ending)
    parameters: 2 strings, which will be converted into 2 numbers
    returns: a positive result, smaller number may have to subtract from
    larger number, this tells how many stops in either direction
    '''

    # This code runs to see if the station is even valid by looking at its
    # position in the list
    if is_valid_station(starting) == True and is_valid_station(ending) == True:
        for i in range(len(RED_LINE)):
           if starting == RED_LINE[i]:
                answer_1 = i
        for i in range(len(RED_LINE)):
            if ending == RED_LINE[i]:
                answer_2 = i
    elif is_valid_station(starting) == False or \
            is_valid_station(ending) == False:
        return 'No destination found.'

    # This code runs to give us the direction to Alewife or Ashmont, by looking
    # at position but returns an integer this time
    answer = answer_1 - answer_2
    if answer > 0:
        return answer
    elif answer < 0:
        return answer * (-1)
    else:
        return 'No destination found.'
