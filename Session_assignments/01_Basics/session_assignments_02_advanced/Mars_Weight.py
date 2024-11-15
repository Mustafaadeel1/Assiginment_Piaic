# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!
def mars_weight():
    g_earth = 9.81
    g_mars = 3.71  
    
    while True:
        user_input = input("Hi! I can convert your Earth weight into Mars weight. \nDo you want to check your weight? (Yes/Enter): ")
        
        if user_input.lower() == "yes":
            try:
                weight = float(input("Enter your weight in kg: "))
                mars_weight = weight * (g_mars / g_earth)
                print(f"Your weight on Mars is {mars_weight:.2f} kg")
            except ValueError:
                print("Invalid input! Please enter a valid number for your weight.")
        
        elif user_input.lower() == "":
            print("Thank you for visiting the Mars Weight Calculator!")
            break  # Exit the loop and end the program
        
        else:
            print("Invalid response. Please enter 'Yes' or 'No'.")
            
# Call the function to start the program
mars_weight()
