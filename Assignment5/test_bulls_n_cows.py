'''
CS5001 Fall 2019
HW 5 Prog 1, Hanoi
Joviane Bellegarde
10/31/19
'''

from bulls_n_cows import *
TEST_GUESSES = [[1,2, 3, 4], [5, 2, 3, 4], [7, 6, 5, 4], [0, 9, 8, 5],
                [2, 4, 6, 8], [1, 3, 5, 7], [1, 2, 0, 9]]

TEST_SECRET = [[1,9,8, 7],[2,4,6, 7], [1,2,0, 9],[7,6,5, 4]]


def test_count_bulls_and_cows():
    ''' Function test_count_bulls_and_cows
        Input: None.
        Returns: Number of failing test conditions for cow/bull sequences
        Do: Test various cow/bull sequences to ensure those counters
            are working as expected. Key cases: 0 cows, 0 bulls;
            4 cows, 0 bulls; 4 bulls, 0 cows, 2 cows, 2 bulls
    '''

    num_failed = 0
    # Test 1: 0 bulls, 0 cows
    # Valid if all pass
    actual = count_bulls_and_cows([1, 2, 3, 4], [0, 0, 0, 0])
    expected = (0, 0)
    print('Input: 0 bulls, 0 cows\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!!!\n')
    else:
        print('Fail.\n')
        num_failed += 1
    

    # Test 2: 0 bulls, 4 cows
    # Valid if all pass
    actual = count_bulls_and_cows([1, 2, 3, 4], [4, 3, 2, 1])
    expected = (0, 4)
    print('Input: 0 bulls, 4 cows\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!!!\n')
    else:
        print('Fail.\n')
        num_failed += 1
        

    # Test 3: 4 bulls, 0 cows
    # Valid if all pass
    actual = count_bulls_and_cows([1, 2, 3, 4], [1, 2, 3, 4])
    expected = (4, 0)
    print('Input: 4 bulls, 0 cows\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!!!\n')
    else:
        print('Fail.\n')
        num_failed += 1


    # Test 4: 2 cows, 2 bulls
    # Valid if all pass
    actual = count_bulls_and_cows([6, 7, 8, 9], [6, 9, 8, 7])
    expected = (2, 2)
    print('Input: 2 bulls, 2 cows\nExpected result:', expected,
          '\nActual result:', actual)
    if actual == expected:
        print('Success!!!\n')
    else:
        print('Fail.\n')
        num_failed += 1

    return num_failed
        
        
def auto_play_game(secret_code, guess_book):
    ''' Function auto_play_game
        Input:  secret_code (list of digits),
                guess_book (dictionary of guess history)
        Returns: True if auto-player a winner; False otherwise
        Do: Automate the playing of Bulls and Cows for regression
        testing. Instead of using interactive input from stdin, this
        function uses test data fed directly to the function to simulate
        an entire "systems test" and complete game flow
        Concept: instead of guess = input(...), now using
        guess = TEST_GUESSES[i]
    '''


def test_regression_bull_cow(secret_code):
    ''' Function test_regression_bull_cow
        Input: secret_code: secret to test with (the one we're "cracking").
        Returns: None
        Do: Automatically exercise and test the entire bulls n cows system
        by calling auto_play_game() multiple times with both "winning" and
        "losing" data. Printed output can then be "diff'd" and examined either
        manually or automatically via tool support

        Example: code is our test data, and autoplay instead of interactive
        secret_code = TEST_SECRET[0]
        guess_book = create_guessbook(7)
        result = auto_play_game(secret_code, guess_book)
    '''
        
    
def main():
    print('Beginning test suite. Testing count bulls and cows...')
    fails = test_count_bulls_and_cows()
    if fails > 0:
        print('Something went wrong. Pls go back and fix errors')
    else:
        print('Counting Bulls and Cows Passed All Tests')
    print('Beginning Auto Play Regression Tests')
    # some example calls
    test_regression_bull_cow(TEST_SECRET[0])
    test_regression_bull_cow(TEST_SECRET[1])    

main()
