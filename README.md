# Formulas-for-my-calculator
i just started programing and i am going to attempt at making a calculator

import math #baskara formula

print("Insert a valor, for a, b and c that follows this format: ax^2 + bx + c")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

Delta = b ** 2 - 4 * a * c
#I did this if else statement to avoid an error in math domain

if Delta < 0:
    print("Delta has no square roots")
    exit()
else:
    pass
#because i just realized that the program calculates the variables even if you don't use them
x0 = -b / (2 * a)
x1 = (-b + math.sqrt(Delta)) / (2*a)
x2 = (-b - math.sqrt(Delta)) / (2*a)

if Delta == 0:
    print(x0)
elif Delta > 0:
    print(f"x1 = {x1}", f"\n x2 = {x2}")
else:
    pass
print("End of program.")
