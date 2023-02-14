def sunny():
    print("You Can Wear sneaker!")

def rainy():
    print("You Can wear gumboot!")

def snowy():
    print("You Can wear boot!")


weather_today = input("Whats the weather today (sunny, rainy, or snowy) : \n Enter 1 for Sunny \n Enter 2 for Rainy \n Enter 3 for Snowy \n Enter :  ")
if weather_today == "1":
    sunny()
elif weather_today == "2":
    rainy()
elif weather_today == "3":
    snowy()
else:
    print("I am unable to find footwear for you")