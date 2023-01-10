print("Employee Gross Salary Calculator")

a = input("Enter Name of Employee :  ")

h= input("Enter Name of Company : ")

b= input ("Enter Basic salary of Employee : ")

c = input(" Dearness allowance percentage : ")

d = input(" House Rent allowance percentage : ")

print("Gross salaray Reciept of  ",a)

print(" Base salary Offered By company : ",b)

e= int(b)*int(c)/int(100)

print("Dearness allowance offered by company : ",e)

f= int(b)*int(d)/int(100)
print("House Rent Allowance offerd by Company : ",f)

g=int(b)+int(e)+int(f)
print(" Gross Salary : ",g)

print(h)
