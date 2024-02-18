"""
you are building an online shopping application and need to create a python program that
calculates the total cost of a purchase after applying discounts based on the total purchase
amount. the program should apply those discounts :
10% discount for purchases above $100
20% discount for purchases above $200
30% discount for purchases above $300
"""

purchases = int(input("Enter amount : "))

if purchases > 300:
    print("30% discount ")
    print("Total cost after discount ", (purchases - (purchases * 0.3)))
elif purchases > 200:
    print("20% discount ")
    print("Total cost after discount ", (purchases - (purchases * 0.2)))
elif purchases > 100:
    print("10% discount  ")
    print("Total cost after discount ", (purchases - (purchases * 0.1)))
else:
    print("No discount")
    print("Total cost after discount ", purchases)
