print("What is your down payment?")
down = int(input())
print("For how long do you plan to pay the mortgage?")
months = int(input())
print("What is the home value in USD($)?")
value = int(input())
r = 0.065 / 12
monthly = (r * down) / (1 - (1 + r)**(-months)) 
print(monthly)