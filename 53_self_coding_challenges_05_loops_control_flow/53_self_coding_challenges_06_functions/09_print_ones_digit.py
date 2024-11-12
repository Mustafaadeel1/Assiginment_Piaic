#  Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!
number = int(input("Enter a number: "))
ones_digit = number % 10  # Use modulo to get the last digit
print(f"The ones digit is {ones_digit}")
