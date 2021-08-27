'''
CS5001 Fall 2019
HW 3 PIG
Joviane Bellegarde
10/1/19
'''

# Need to import random
import random

# Making this a global
THRESHOLD = 20


def roll_die():
    '''
    function: roll_die()
    paramaters: none
    returns: an int from 1 to 6
    '''
    die = random.randint(1, 6)
    return die


def gaming():
    '''
    function: gaming()
    paramaters: none
    returns: an int, of the score from the round
    '''
    
    round_score = 0
    while round_score <= THRESHOLD:
        
        choice = ''
        
        # This loop is to prompt the user until they enter a right answer
        while choice not in ['R', 'H']:
            choice = input('Enter R to roll or H to hold.\n').upper()
            
            if choice == 'R':
                points = roll_die()
                if points == 1:
                    round_score = 0
                    print(round_score, ' is your score. You rolled a',
                          points, '\nNext players turn.')
                    break
                
                elif points != 1:
                    if round_score <= THRESHOLD:
                        round_score += points
                        print(points, 'is your points. Your score is',
                              round_score)
                        continue
                
        if choice == 'H':
            print('Your score this round is', round_score)
            break
        
    return round_score
        
def main():
    
    playerlist = ['Player 1', 'Player 2']
    overall_scorelist = [0, 0]
    
    print('Welcome to the game of PIG! The first player to 20 points or ' +
          'more wins!')
    
    name = ''
    
    # this loop is to add players to the game, but start from 2 players
    while True:
        name = input('There are already 2 players, if you want to add a 3rd ' +
                     'player, enter a name. Else, Enter Q to quit ' +
                     'adding names.\n').upper()
        
        if name == 'Q':
            break
        
        # Need to add player to the list
        playerlist.append(name)
    
        for i in range(len(playerlist)):
             overall_scorelist.append(0)

        print(playerlist)
        
        
    overall_score = 0

    result = gaming()
    overall_scorelist.append(result)
    print(overall_scorelist)

    i = 0
    
    
    if result <= THRESHOLD:
        
        # This code should allow to go through the player list
        playerlist_length = len(playerlist)
        current_player = playerlist[i % playerlist_length]
        print(current_player, 'it is your turn')
        
        overall_score += result
        
        if overall_score >= THRESHOLD:
            print(current_player, 'you have won the game!')
    
main()
    