num1 = int(input("Enter  Number 1 : "))
num2 = int(input("Enter  Number 2 : "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these Operations \n 1 for Addition \n 2 for Subtration \n 3 for Multiplication \n 4 for Division  \n Input : ")

result = 0
if ch == '1':
    result = num1 + num2

elif ch == '2':
    result = num1 - num2
elif ch == '3':
    result = num1 * num2
elif ch == '4':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print("Your Answer :", result)