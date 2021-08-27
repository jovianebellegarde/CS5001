'''
CS5001 Fall 2019
HW 2 Hurricane Tracker
Joviane Bellegarde
9/20/19
'''
    
# going to import the haversine function from same directory
from haversine import haversine

DORIAN_LATITUDE = 27.1
DORIAN_LONGITUDE = -78.4
BOSTON_LATITUDE = 42.361145
BOSTON_LONGITUDE = -71.057083
MIAMI_LATITUDE = 25.761681
MIAMI_LONGITUDE = -80.191788

def hurricane(city):

    ''' Function: calculates the distance of Dorian from the city user inputs
        Parameters: a string
        Returns: prints the number of miles that Dorian is from the city and
        a warning message depending on if the city is within 150 miles of the
        hurricane.
    '''

    # takes care of issue if user inputs upper or lower case letter
    city = city.upper() or city.lower()

    # if user enters B for Boston, this code will run
    if city == "B":

        distance = haversine(BOSTON_LATITUDE, BOSTON_LONGITUDE,
                                 DORIAN_LATITUDE, DORIAN_LONGITUDE)

        print("Huricane Dorian was " + str(round(distance, 2)) +
              " nautical miles from Boston.\n"
              "Boston is not in the hurricane zone.")

    # if user enters M for Miami, this code will run
    elif city == "M":

        distance = haversine(MIAMI_LATITUDE, MIAMI_LONGITUDE,
                                DORIAN_LATITUDE, DORIAN_LONGITUDE)

        print("Huricane Dorian was " + str(round(distance, 2)) +
              " nautical miles from Miami. \nWarning!\n"
              "Seek shelter now! Miami is in the hurricane zone!")

    # this code catches when the user doesn't enter B or M
    # the input city from the user is printed out from this block of code
    else:
        city_name = input("What is the name of the city? ")
        latitude = float(input("latitude (decimal degrees): "))
        longitude = float(input("longitude (decimal degrees): "))
        distance = haversine(latitude, longitude, DORIAN_LATITUDE,
                               DORIAN_LONGITUDE)

        print("Hurricane Dorian was " + str(round(distance, 2)) +
              " nautical miles from " + city_name + " on Sep 3, 2019.")

        # this code runs and checks if the distance is less than or equal to 150
        # or more than 150 to print out a warning or "safe message"
        if distance <= 150:
            print("Warning!", city_name, "is in hurricane zone. Seek "
                  "shelter now!")
        else:
            print(city_name, "is not in a hurricane zone.")
        
def main():

    # this code allows for the user to input which city they want to know
    # the hurricane information
    city = input("Welcome to reliable the hurricane tracker and warning "
                 "system!" + ":)\n" + "Enter a location to apply to "
                 "the radar:\n" + "B for Boston\n" + "M for Miami\n" +
                 "O for another location of your choice\n")

    hurricane(city)
          
main()
