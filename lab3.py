'''use input year to check the year is leap year or not. if the year is divided by 400 and 100,
it is leap year and also if divided by 4.'''

year = int(input('enter the year :'))
print(year)
while year < 0:
    print("Invalid year")
    year = int(input("enter a valid year"))
if (year % 400 == 0 or year % 4 == 0) & (year % 100 != 0):
    print(" the leap year is {0} ".format(year))
else:
    print(year, "  is not leap year ")




