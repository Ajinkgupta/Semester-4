str = input("Enter the String you want to be Passed : ")
rev = str[::-1]

if str == rev:
    print(str  + " This String is Palindrome")
    print("Reason : " + str + " is Equal " + rev)
else:
    print(str + " This String is not Palindrome ")
    print("Reason : " + str + " is not Equal " + rev)

