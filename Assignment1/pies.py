'''
Joviane Bellegarde
CS5001 - Fall 2019
HW 1 - Programming 3
9/17/19
'''


'''
Test 1
7 pie crusts, 9 potatoes, 4 meat, 3 corn
Can make 1 pie, have 6 crusts, 3 potatoes, 2 meat, 2 corn left

Test 2
50 pie crusts, 40 potatoes, 30 meat, 20 corn
Can make 6 pies, have 44 crusts, 4 potatoes, 18 meat, 14 corn left

Test 3
100 pie crusts, 100 potatoes, 100 meat, 100 corn
Can make 16 pies, have 84 crusts, 4 potatoes, 60 meat, 84 corn left

Test 4
50 pie crusts, 50 potatoes, 50 meat, 50 corn
Can 8 pies, have 42 crusts, 2 potatoes, 34 meat, 42 corn left

Test 5
31 pie crusts, 32 potatoes, 33 meat, 34 corn
Can make 5 pies, have 26 crusts, 2 potatoes, 23 meat, 29 corn left 
'''

CRUSTS = 1
POTATOES = 6
MEAT = 2
CORN = 1

def main():

    # input code for the user to input how much ingredients they have
    user_crusts = int(input("How many pie crusts do you have?\n"))
    user_potatoes = int(input("How many potatoes?\n"))
    user_meat = int(input("How much meat do you have?\n"))
    user_corn = int(input("How about the corn?\n"))

    # need to do int division with the ingredients needed
    # calculate how many pies possible based on "unlimited" ingredients
    crusts_possible = user_crusts // CRUSTS
    potatoes_possible = user_potatoes // POTATOES
    meat_possible = user_meat // MEAT
    corn_possible = user_corn // CORN

    # use min fuction to use limiting ingredient to multiply by
    # to figure out how many pies we can make
    maximum_pies_possible = min(crusts_possible, potatoes_possible,
                                meat_possible, corn_possible)

    # calculated how many of each ingredient we have left over
    crusts_leftover = user_crusts - (CRUSTS * maximum_pies_possible)
    potatoes_leftover = user_potatoes - (POTATOES * maximum_pies_possible)
    meat_leftover = user_meat - (MEAT * maximum_pies_possible)
    corn_leftover = user_corn - (CORN * maximum_pies_possible)

    print("Kiki made " + str(maximum_pies_possible) + " sheperds pies for"
          " NSKS!\n" + "You have these ingredients leftoever:\n" +
          str(crusts_leftover) + " crust(s)\n" + str(potatoes_leftover) +
          " potato(es)\n" + str(meat_leftover) + " meat package(s)\n" +
          str(corn_leftover) + " corn package(s)")

main()
