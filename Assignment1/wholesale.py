'''
Joviane Bellegarde
CS5001 - Fall 2019
HW 1 - Programming 2
9/17/19
'''

'''
Test 1
7 books, $104.79 cost, $7.50 shipping, $112.29 total cost

Test 2
3 books, $44.91 cost, $4.50 shipping, $49.41 total cost

Test 3
50 books, $748.50 cost, $39.75 shipping, $788.25 total cost
'''

PRICE = 24.95
DISCOUNT = 0.40
SHIP3 = 3.00
SHIP075 = 0.75

def main():
    
    books = int(input("How copies of this book are you buying?\n"))

    # each book cost $24.95 pre-discount
    cost_books = books * PRICE

    # need to calculate the 40% discount now
    discounted_price = cost_books - (cost_books * DISCOUNT)

    # calculate the shipping price for 1 or more books
    shipping = SHIP3 + ((books - 1) * SHIP075)

    # need to now incoporate the shipping to the total cost
    total_cost = discounted_price + shipping
    
    print("The books are discounted at $" +
          str("{:.2f}".format(round(discounted_price, 2))) + ".\n" +
          "The shipping price is $" + str("{:.2f}".format(round(shipping, 2))) + ".\n"
          + "The total cost is now $" + str("{:.2f}".format(round(total_cost, 2))) +
          ".\n")

main()
