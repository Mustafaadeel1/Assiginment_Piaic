# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:
print("Welcome To my Fruit_store :)\n")
def fruit_in_stock(f):
    li = ["Mango","apple","banana","cherry","Watermalon","malon"]
    if f in li:
        avai=int(input("\nThis fruit is available in stock:How many do you want to buy?\n"))
        print(f"{avai} = {user_fruit}")
    else:
        print("\nThis fruit is not available in stock")
user_fruit = input("Enter a fruit:")
fruit_in_stock(user_fruit)