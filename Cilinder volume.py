import math

h = float(input("Please insert the height: "))
print("radius = 1; Diameter = 2")
w = int(input("Please choose between radius or Diameter: "))

if w == 1:
    r = float(input("Insert the radius: "))
    cilinder_V1 = math.pi * math.pow(r, 2) * h
    print(cilinder_V1)
elif w == 2:
    d = float(input("Insert the Diameter: "))
    r2 = d/2
    cilinder_V2 = math.pi * math.pow(r2, 2) * h
    print(cilinder_V2)
else:pass

print("END OF PROGRAM")
