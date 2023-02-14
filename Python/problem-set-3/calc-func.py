
def add_num(a,b):
    sum=a+b;
    return sum;

def sub_num(a,b):
    sub=a-b;
    return sub;

def mul_num(a,b):
    mul=a*b;
    return mul;


def div_num(a,b):
    div=a/b;
    return div;


num1=int(input("input the number one: "))
num2=int(input("input the number one :"))

calc = input("Enter any of these Operations \n 1 for Addition \n 2 for Subtration \n 3 for Multiplication \n 4 for Division  \n Input : ")

if calc == '1':
 print("The sum is",add_num(num1,num2))
elif calc == '2':
 print("The subtraction is",sub_num(num1,num2))

elif calc == '3':
 print("The multiplication is",mul_num(num1,num2))

elif calc == '4':
 print("The Division is",div_num(num1,num2))

else :
    print("Wrong Operator code : : ")