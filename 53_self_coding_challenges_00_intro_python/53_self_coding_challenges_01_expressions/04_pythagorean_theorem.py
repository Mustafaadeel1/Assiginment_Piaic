# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem
import math
print("You tell me lengths of the two perpendicular sides of a right triangle")
a = float(input("Enter the length of a :"))
b = float(input("Enter  the length of b :"))
c =  math.sqrt(a**2 + b ** 2)
print(f"The length of high hypotenuse {c}")

# To find Length of other
b = float(input("Enter the value of b :"))
c = float(input("Enter the value of c :"))
a = math.sqrt(b**2 + c**2)
print(f"The len of other side {a:.2f}")
