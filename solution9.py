meal_price = float(input("Enter the price of the meal: $"))

tip_percent = float(input("Enter the tip percentage you want to leave (as a percentage): "))

tip_amount = meal_price * (tip_percent / 100)

total_bill = meal_price + tip_amount

print("Tip amount: $", format(tip_amount, ".2f"), sep="")
print("Total bill (with tip): $", format(total_bill, ".2f"), sep="")