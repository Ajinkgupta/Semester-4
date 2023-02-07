no = int(input("Enter the number of letters per line: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
with open("alphabet.txt", "w") as f:
  
 for i in range(0, len(alphabet), no):
  f.write(alphabet.upper()[i:i+no] + "\n")
