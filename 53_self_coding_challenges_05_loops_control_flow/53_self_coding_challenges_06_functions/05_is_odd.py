def even_odd():
    li = []
    while True:
        user_input = input("Enter your number (or press Enter to end): ")
        
        if user_input == "":
            print("Exiting the program.\n")
            break
        
        try:
            user_num = int(user_input)
            li.append(user_num)  
            if user_num % 2 == 0:
                print(f"{user_num} is even")
            else:
                print(f"{user_num} is odd")
        except ValueError:
            print("Please enter a valid integer.")
    
    
    print("\nList of all numbers and their even/odd status:")
    for num in li:
        if num % 2 == 0:
            print(f"{num} is even",end=" ")
        else:
            print(f"{num} is odd",end=" ")

even_odd()

