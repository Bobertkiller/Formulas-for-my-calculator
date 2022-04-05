import math
#circle area formula
print("You have selected the circle area formula, insert the radius or the diameter")
print("If you do not have a valor to insert, please insert 0")

r = float(input("Insert the radius: ")) #radius

if r == 0:
    pass
else:area1 = math.pi * math.pow(r,2); print(area1); exit()

d = float(input("Insert the diameter: ")) #diameter

r2 = d/2
area2 = math.pi * math.pow(r2, 2)

if d == 0:
    pass
else:print(area2)

print("END OF PROGRAM")
