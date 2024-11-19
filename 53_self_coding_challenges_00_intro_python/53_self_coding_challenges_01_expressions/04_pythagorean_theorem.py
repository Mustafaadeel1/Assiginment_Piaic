# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem
import math
# Calculate the hypotenuse
print("Enter the lengths of the two perpendicular sides of a right triangle.")
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(a**2 + b**2)
print(f"The length of the hypotenuse is: {c:.2f}")

# Calculate a missing perpendicular side
print("\nNow, let's find the length of one of the perpendicular sides.")
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of the hypotenuse (c): "))
if c > b:  # Ensure the hypotenuse is larger than the perpendicular side
    a = math.sqrt(c**2 - b**2)
    print(f"The length of the other perpendicular side is: {a:.2f}")
else:
    print("The hypotenuse must be greater than the other side.")
