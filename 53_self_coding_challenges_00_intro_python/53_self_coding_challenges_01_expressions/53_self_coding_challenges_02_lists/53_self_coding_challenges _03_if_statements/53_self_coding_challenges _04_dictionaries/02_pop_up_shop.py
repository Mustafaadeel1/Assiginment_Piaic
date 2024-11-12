#There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
# def fruit_shop():
#     user_buy = input("You will buy from my shop\"Yes,No\"").lower()
#     if user_buy == "yes":
#         apple = int(input("How many (Apples) do you want"))
#         banana = int(input("How many (Bananas) do you want"))
#         orange = int(input("How many (Oranges) do you want"))
#         grapes = int(input("How many (Grapes) do you want"))
#         mangoes = int(input("How many (Mangoes) do you want"))
#         fruit_price = {apple:2,banana:1.5,orange:3.3,grapes:6,mangoes:9}
#         total_cost = (apple * fruit_price[apple]) + (banana * fruit_price[banana]+ (orange * fruit_price[orange]) + (grapes * fruit_price[grapes] + (mangoes * fruit_price[mangoes])))
#         print("Thank Your For shopping",end="")
#         print(f" Your Total cost is ${total_cost}")
#     else:
#         print("Thats Ok, See you next time :)")

# fruit_shop()


def fruit_shop():
    # Ask the user if they want to buy from the shop
    user_buy = input("Would you like to buy from my shop? (Yes/No): ").lower()
    
    if user_buy == "yes":
        # Dictionary with the price of each fruit
        fruit_prices = {
            "apple": 2.0,
            "banana": 1.5,
            "orange": 3.3,
            "grapes": 6.0,
            "mango": 9.0
        }
        
        # Initialize total cost to zero
        total_cost = 0

        # Loop through each fruit in the dictionary
        for fruit, price in fruit_prices.items():
            try:
                quantity = int(input(f"How many {fruit.capitalize()}s do you want? "))
                total_cost += quantity * price  # Calculate cost for each fruit and add it to the total cost
            except ValueError:
                print("Invalid input, please enter a number for quantity.")
        
        # Print the final total cost
        print("Thank you for shopping!")
        print(f"Your total cost is ${total_cost:.2f}")

    else:
        print("That's okay, see you next time! :)")

# Run the function
fruit_shop()

