rate = float(input("What's the current Euro to USD exchange rate? "))
amount = float(input("How many Euros do you have? "))
total = float((rate * amount) - 3)
print(f"The exachange is ${total + 3:.2f}, and after a $3 fee, your total is ${total:.2f}")