def is_palindrome(s):
    rev = s[::-1]
    
    if s == rev:
        return True
    else:
        return False


str = input("Enter the string you want to be passed: ")
if is_palindrome(str):
    print(str  + " is a palindrome string")
else:
    print(str + " is not a palindrome string")
