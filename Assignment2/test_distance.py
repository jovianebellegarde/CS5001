'''
CS5001 Fall 2019
HW 2 Written
Joviane Bellegarde
9/23/19
Consulted the euclidean test code that was provided for us for this assignment
http://www.ccs.neu.edu/home/
kbagley/cs5001/fall2019/code/homework2/test_euclidean.py

One major error that may have happened with my tests is that when I entered
0 for my absolute, the code may have broken. Since I had my absolute function
to return a number if the number is greater or equal to 0, this helped prevent
this.
'''

# Import functions

from distance import absolute
from distance import manhattan


# Setting EPSILON so that the test code can run correctly
# with slight differences.

EPSILON = .0001

def test_absolute():

    ''' Function: this function tests for the correctness of the absolute
        function that I made.
        Parameters: and int or a float that is being tested, a positive number
        Return: the number of tests failed
    '''

    # This code tests the absolute code. If the input is correct,
    # the code will let us know all tests have passed. If incorrect,
    # the code will let us know that the tests have failed.
    num_failed = 0

    # Test 1: -77
    # Value is 77
    actual = absolute(-77)
    expected = 77
    print("Input -77\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1

    # Test 2: 0.85
    # Value is 0.85

    actual = absolute(0.85)
    expected = 0.85
    print("Input 0.85\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1

    # Test 3: -385.76
    # Value is 385.76

    actual = absolute(-385.76)
    expected = 385.76
    print("Input -385.76\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1

    # Test 4: 0
    # Value is 0

    actual = absolute(0)
    expected = 0
    print("Input 0\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1
              
    return num_failed




def test_manhattan():

    ''' Function: this function tests for the correctness of the absolute
        function that I made.
        Parameters: and int or a float that is being tested
        Return: the number of tests failed
    '''

    # This code tests the manhattan equation. If the input is correct,
    # the code will let us know all tests have passed. If incorrect,
    # the code will let us know that the tests have failed.

    # Test 1: (1, 2), (3, 4)
    # Value is 4
    num_failed = 0
    actual = manhattan(1, 2, 3, 4)
    expected = 4
    print("Input (1, 2), (3, 4).\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1

    # Test 2: (-1, -2), (-3, -4)
    # Value is 4
    num_failed = 0
    actual = manhattan(-1, -2, -3, -4)
    expected = 4
    print("Input (-1, -2), (-3, -4).\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1

    # Test 3: (-7.5, -8.2), (-9.7, -10.4)
    # Value is 4.4
    num_failed = 0
    actual = manhattan(-7.5, -8.2, -9.7, -10.4)
    expected = 4.4
    print("Input (-7.5, -8.2), (-9.7, -10.4).\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1

    # Test 4: (0, 0), (0, 0)
    # Value is 0
    num_failed = 0
    actual = manhattan(0, 0, 0, 0)
    expected = 0
    print("Input (0, 0, 0, 0).\n"
          "Expected result", expected, "and actual result =", actual)
    if absolute(actual - expected) < EPSILON:
        print("Success!\n")
    else:
        print("Fail.\n")
        num_failed += 1
    

    return num_failed


    
def main():

    # This code calls the two functions that are above and will allow for
    # print outs of the number of tests passed/failed.
   
    num_fail = test_absolute()
    if num_fail == 0:
        print("All tests passed!\n\n")
    else:
        print("Sorry", num_fail, "tests failed. Please go back and fix it.")

    
    num_fail = test_manhattan()
    if num_fail == 0:
        print("All tests passed!\n\n")
    else:
        print("Sorry", num_fail, "tests failed. Please go back and fix it.")

main()
