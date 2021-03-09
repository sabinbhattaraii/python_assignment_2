'''
Write an if statement to determine whether a variable holding a year is
a leap year.
'''

year = int(input("enter a year"))

if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
else:
    print(year, "is not a Leap Year")