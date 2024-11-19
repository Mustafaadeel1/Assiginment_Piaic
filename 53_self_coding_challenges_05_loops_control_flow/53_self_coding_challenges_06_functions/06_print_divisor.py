def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Get input from the user
number = int(input("Enter a number: "))

# Find and display the divisors
divisors = find_divisors(number)
print(f"Here are the divisors of {number}: ", end="")
print(" ".join(map(str, divisors)))
