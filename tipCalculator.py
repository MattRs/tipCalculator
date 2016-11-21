"""
Calculate the amount your meal really costs; tips are determined when the
"""

mealCost = float(input("How much does your meal cost? \n"))
taxRate = float(input("What is the tax rate? \n"))
tipRate = float(input("What is the tip rate? \n"))

print("Your meal costs $%0.2f" % mealCost)

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= (1.0 + taxRate)
    print("With tax: $%0.2f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= (1.0 + tipRate)
    print("With tip: $%0.2f" % bill)
    return bill

mealwithTax = tax(mealCost)
mealwithTip = tip(mealwithTax)