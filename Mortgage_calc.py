class Mortgage():
    def __init__(self, name, principal, months):
        self.name = name
        self.principal = principal
        self.months = months

    def calc_mortgage(self,principal, months, r = 0.065 / 12):
        monthly = (r * principal) / (1 - (1 + r)**(-months)) 
        return "{name}, your monthly payments will come out to {monthly:.2f}$".format(name = name, monthly = monthly)

name = input("What is your name?\n")
principal = int(input("What is your down payment?\n"))
months = int(input("For how many months do you plan to pay the mortgage?\n"))

mortgage = Mortgage(name, principal, months)
print(mortgage.calc_mortgage(principal, months))