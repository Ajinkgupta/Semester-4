#program to determine leap year
yr= int(input("Enter year to determine the is it leap or not"))

if (yr%4 == 0 ) or (yr%100 != 0 and yr%400 == 0) :

    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
