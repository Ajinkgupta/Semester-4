f = open("sblc-3.txt","w")
while True :
	sentence = input("Enter   lines ( enter END to stop ) :-")
	if sentence == "END" :
		break
	else :
		f.write(sentence + "\n")
f.close()
print()
print("The Lines started with Upperecase letters are :-")
f = open("sblc-3.txt","r")
print()
data = f.readlines()
for i in data :
	if i[0].isupper() :
		print(i)
f.close()
