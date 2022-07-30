class Mortgage():
    def __init__(self, name, principal, months,r, total = 0, monthly = 0):
        self.name = name
        self.principal = principal
        self.months = months
        self.r = r
        self.total = total
        self.monthly = monthly
    
    def __repr__(self):
        description = "{name}, your monthly payments will come out to {monthly:.2f}$. Your total loan is {total:.2f}$ spread out over {months} months.".format(total = self.total, months = self.months, name = self.name, monthly = self.monthly)
        return description
    def calc_mortgage(self):
        self.monthly = (self.r * self.principal) / (1 - (1 + self.r)**(-self.months)) 
        return self.monthly
    def total_mortgage(self):
        self.total = self.monthly * self.months + self.principal
        return self.total

name = input("What is your name?\n")
r = float(input("What is the yearly interest rate?\n")) / 12 / 100
principal = float(input("What is your down payment?\n"))
months = int(input("For how many months do you plan to pay the mortgage?\n"))

mortgage = Mortgage(name, principal, months, r)
mortgage.calc_mortgage(principal, months, r)
mortgage.total_mortgage(mortgage.monthly,principal, months)
print(mortgage)