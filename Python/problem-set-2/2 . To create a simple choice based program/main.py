from os import system


  # Function to write data to a file 
def WriteToFile(data,filename):
        fileobj=open(filename,"w")
        fileobj.write(data)
        fileobj.close()

# Function to read data from a file 
def ReadFromFile(filename):
    fileobj=open(filename,"r")
    data=fileobj.read()
    fileobj.close()
    return data
 

def main():
    # Choice for options for user to select 
    ans=True
    while(ans):
        
        print("File Menu")
        print("1. Read Data ")
        print("2. Write Data ")
        print("3. Exit")

        ch=int(input("Enter Choice(1-3) : "))

        if ch==1:
            fileName = input("Enter File name : ")
            # calling the function from FileManager.py
            data = ReadFromFile(fileName)
            print("Content of File:\n",data)
          
        elif ch==2:
            data = input("Enter Data : ")
            fileName = input("Enter File name : ")
            # calling the function from FileManager.py
            WriteToFile(data,fileName)
            print("Data is Saved.")
        elif ch==3:
            ans=False
        else:
            print("Invalid Choice")

        input("\n\nPress any key .........")

if __name__=="__main__":main()
 
