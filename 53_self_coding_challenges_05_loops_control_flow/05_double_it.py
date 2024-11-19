# # Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# # For example if the user enters the number 2 you would then print:
print("Enter a number, I will return the double of that number")

def double():
    user_in = int(input("Enter a number: "))
    while user_in < 100:  
        user_in = user_in * 2  
        print(user_in, end=" ")  

double()

