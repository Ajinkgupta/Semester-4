def reverse_string(s):
    return s[::-1]

str = input("Enter the string you want to reverse: ")
print("Provided string: ", str)
rev_str = reverse_string(str)
print("Reversed string: ", rev_str)
