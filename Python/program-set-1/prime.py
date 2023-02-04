num=int(input("Enter number: "))
k=0
for i in range(2,num//2+1):
    if(num%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")
