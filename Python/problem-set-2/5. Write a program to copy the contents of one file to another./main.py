file1 = open("sblc-input.txt", "r")

file2 = open("sblc-output.txt", "w")
 
for line in file1:
 file2.write(line.upper())
