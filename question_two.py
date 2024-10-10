#Using a function, create a program that calculates the volume of a cylinder.

import math
pie = math.pi
height = float(input("Enter the height: "))
radius = float(input("Enter the radius: "))
volume_of_a_cylinder = pie * radius **2 * height
print(f"The volume of the cylinder is {volume_of_a_cylinder}")