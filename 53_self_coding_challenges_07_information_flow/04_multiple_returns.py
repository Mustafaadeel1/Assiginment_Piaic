# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:
def get_user_data():
    user_data = {}
    user_name_f = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")
    user_email = input("Enter your email: ")
    user_data["First_name"] = user_name_f 
    user_data["Last_name"] = user_last_name
    user_data["Email"] = user_email
    
    recive = input("Received the following user data [Yes/No] Type: ").lower().strip()
    
    if recive == "yes":
        print("Your data is stored.")
        print(user_data)
    elif recive == "no":
        print("Data not stored.")
    else:
        print("Invalid input")

get_user_data()
