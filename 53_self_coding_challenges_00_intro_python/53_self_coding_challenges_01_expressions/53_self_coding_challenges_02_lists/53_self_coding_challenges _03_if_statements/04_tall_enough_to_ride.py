# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
def height():
    print("To ride a Roller coaster Please your Height")
    user_tall = float(input("How tall are you? :"))
    if user_tall >= 5.5:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
height()