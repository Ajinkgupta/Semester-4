# Grade calculator

print("Enter the marks you recieved in three subjects")
max = int(input("maximum marks in Every Subject"))

mks1 = int(input("Enter marks in Subject 1 "))

mks2 = int(input("Enter marks in Subject 2 "))

mks3 = int(input("Enter marks in Subject  "))

total = ((mks1+mks2+mks3))


ptg = total*100/(3*max)

print("Your percentage ",ptg)

if 90 < ptg <= 100:
    print("Grade is A")

elif 80 < ptg <= 89:

    print("Grade is B")

elif 70 < ptg <= 79 :

    print("Grade is C")

elif 60 < ptg <= 69:

    print("Grade is D")

elif 0 < ptg <= 59:

    print("Grade is F")
