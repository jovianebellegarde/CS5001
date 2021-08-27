'''
CS5001 Fall 2019
HW 4, Prog 2 MBTA Test
Joviane Bellegarde
10/22/19
'''

from mbta import *


def test_valid_station():
    '''
    function: valid, tests for function correctness of is_valid_station
    function.
    parameters: a string, checking for station validity
    return: number of tests failed
    '''
    num_failed = 0

    # Test 1: 'Ashmont'
    # Value is True
    actual = is_valid_station('Ashmont')
    expected = True
    print('Input: Ashmont\nExpected result:', expected, '\nActual result:',
          actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 2: 'ALEWIFE'
    # Value is False
    actual = is_valid_station('ALEWIFE')
    expected = False
    print('Input: ALEWIFE\nExpected result:', expected, '\nActual result:',
          actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 3: 'Charles/MGH'
    # Value is True
    actual = is_valid_station('Charles/MGH')
    expected = True
    print('Input: Charles/MGH\nExpected result:', expected, '\nActual result:',
          actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 4: 'DaVis'
    # Value is False
    actual = is_valid_station('DaVis')
    expected = False
    print('Input: DaVis\nExpected result:', expected, '\nActual result:',
          actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 5: 'ParkSt'
    # Value is False
    actual = is_valid_station('ParkSt')
    expected = False
    print('Input: ParkSt\nExpected result:', expected, '\nActual result:',
          actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1

    return num_failed



def test_get_direction():
    '''
    function: test_get_direction(), tests validity of get_direction
    parameters: 2 strings, a starting and ending station
    returns: 1 of 3 stings, Ashmont, Alewife, or No destination found
    '''
    num_failed = 0

    # Test 1: Alewife, Ashmont
    # Valid is Ashmont
    actual = get_direction('Alewife', 'Ashmont')
    expected = 'Ashmont'
    print('Input: Alewife to Ashmont\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 2: South Station, South Station
    # Valid is No destination found
    actual = get_direction('South Station', 'South Station')
    expected = 'No destination found.'
    print('Input: South Station to South Station\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 3: ShawMut, Fields Corner
    # Valid is No destination found
    actual = get_direction('ShawMut', 'Fields Corner')
    expected = 'No destination found.'
    print('Input: ShawMut to Fields Corner\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 4: Downtown Crossing, JFK/UMass
    # Valid is Ashmont
    actual = get_direction('Downtown Crossing', 'JFK/UMass')
    expected = 'Ashmont'
    print('Input: Downtown Crossing to JFK/UMass\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 5: Downtown Crossing, JFK/UMass
    # Valid is Ashmont
    actual = get_direction('Downtown Crossing', 'JFK/UMass')
    expected = 'Ashmont'
    print('Input: Downtown Crossing to JFK/UMass\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1

    return num_failed



def test_get_num_stops():
    '''
    function: test_get_num_stops(), tests vailidity of get_num_stops
    parameters: 2 strings, starting and ending stations
    returns: an int, the number of stops to travel from start to end station
    '''
    num_failed = 0

    # Test 1: Ashmont, Alewife
    # Valid is 16
    actual = get_num_stops('Ashmont', 'Alewife')
    expected = 16
    print('Input: Ashmont to Alewife\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 2: Broadway to Downtown Crossing
    # Valid is 2
    actual = get_num_stops('Broadway', 'Downtown Crossing')
    expected = 2
    print('Input: Broadway to Downtown Crossing\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 3: Harvard to Harvard
    # Valid is No destination Found
    actual = get_num_stops('Harvard', 'Harvard')
    expected = 'No destination found.'
    print('Input: Harvard to Harvard\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 4: Andrew to POrter
    # Valid is No destination Found
    actual = get_num_stops('Andrew', 'POrter')
    expected = 'No destination found.'
    print('Input: Andrew to POrter\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 5: JFK/UMass to Charles/MGH
    # Valid is 6
    actual = get_num_stops('JFK/UMass', 'Charles/MGH')
    expected = 6
    print('Input: JFK/UMass to Charles/MGH\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!\n')
    else:
        print('Fail.\n')
        num_failed += 1

    return num_failed



def main():

    num_fail = test_valid_station()
    if num_fail == 0:
        print('All tests have passed!\n\n')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix it.')

    num_fail = test_get_direction()
    if num_fail == 0:
        print('All tests have passed!\n\n')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix it.')

    num_fail == test_get_num_stops()
    if num_fail == 0:
        print('All tests have passed!\n\n')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix it.')

main()
