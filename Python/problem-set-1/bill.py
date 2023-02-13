# calculate your monthly bill for telephone

call = int(input("Enter your number of calls for this month: "))

if call <= 100:
    bill = 200


elif 100 < call <= 150:
    addon = call - 100
    bill = 200 + 0.60 * addon


elif 150 < call <= 200:
    addon = call - 150
    bill = 200 + 0.60 * 50 + 0.50 * addon

else:

    addon = call - 200
    bill = 200 + 0.60 * 50 + 0.50 * 50 + 0.40 * addon

print("Total bill For this month is Rs", bill)
