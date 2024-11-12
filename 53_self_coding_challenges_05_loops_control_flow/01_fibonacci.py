# Define the maximum value as a constant
MAX_VALUE = 10000

# Initialize the first two terms of the Fibonacci sequence
fib_0 = 0
fib_1 = 1

# Print the initial terms
print(fib_0, fib_1, end=" ")

# Generate and print the Fibonacci sequence up to MAX_VALUE
while True:
    # Calculate the next term
    next_fib = fib_0 + fib_1
    
    # Break the loop if the next term exceeds the maximum value
    if next_fib >= MAX_VALUE:
        break
    
    # Print the next term
    print(next_fib, end=" ")
    
    # Update fib_0 and fib_1 for the next iteration
    fib_0 = fib_1
    fib_1 = next_fib
