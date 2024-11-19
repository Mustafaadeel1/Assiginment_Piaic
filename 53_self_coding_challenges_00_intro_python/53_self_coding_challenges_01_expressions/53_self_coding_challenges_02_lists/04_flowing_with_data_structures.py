print("To break the program, say 'stop'")
li = []  # Initialize an empty list

while True:
    user_input = input("Enter a value (or type 'stop' to end): ")
    if user_input.lower() == "stop":  
        break
    li.append(user_input)  

print("The collected values are:", li)
