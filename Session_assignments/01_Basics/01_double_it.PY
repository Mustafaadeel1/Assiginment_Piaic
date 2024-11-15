# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater
def double_number(num):
    while num < 100:
        num *= 2  # Double the number
        print(num,end=" ")
    print("\nThis is the final result:", num)

number = int(input("Please enter a number: "))
double_number(number)

