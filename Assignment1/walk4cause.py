'''
Joviane Bellegarde
CS5001 - Fall 2019
HW 1 - Programming 1
9/17/19
'''

'''
Test 1
2 km, 2 hr, $2/mile
1.24 miles, 0.62 mph, 96 min & 46 sec, $2.48

Test 2
5 km, 4 hr, $5/mile
3.10 miles, 0.77 mph, 77 min & 16 seconds, $15.50

Test 3
20 km, 1 hr, $8/mile
12.42 miles, 12.42 mph, 4 min & 49 sec, $99.36

Test 4
0.25 km, 0.3 hr, $0.70/mile
0.15 miles, 0.5 mph, 120 min, 0 seconds, $0.11

Test 5
7 km, 1 hr, $10/mile
4.34 miles, 4.34 mph, 13 min & 48 sec, $43.50
'''

import math

# global constants for mile, hours, and minutes
MILE = 1.61
ONE_MIN = 60
ONE_HR = 60

def main():
    
    # user input for miles walked, average pace, and mph
    km_walked = float(input("How many kilometers did you walk?\n"))
    hours_walked = float(input("How many hours was your walk?\n"))
    sponsor = float(input("How much is your sponsor paying per mile?\n"))

    # convert km to miles walked
    miles_walked = km_walked / MILE

    # convert hours walked to minutes
    # calculate pace per miles (minutes and seconds)
    # minutes_walked = hours_walked * 60
    pace_min = (hours_walked / miles_walked) * ONE_HR
    # need to use modulo to get seconds after the decimal
    pace_sec = (pace_min % 1) * ONE_MIN

    # calculate the mph ran
    mph = (miles_walked * ONE_MIN) / (hours_walked * ONE_MIN)

    # calculate sponsership per mile
    total_sponsorship = sponsor * miles_walked

    # print statement to shows miles walked, mph, pace, and earnings
    print("You walked", "{:.2f}".format(miles_walked), "miles at",
          round(mph, 2), "mph.\nYour pace is", math.floor(pace_min),
          "minutes and", math.floor(pace_sec),
          "seconds per mile.\nYou also raised $"
          + str(round(total_sponsorship, 2)),
          "for Imani House. Awesome!")

main()
