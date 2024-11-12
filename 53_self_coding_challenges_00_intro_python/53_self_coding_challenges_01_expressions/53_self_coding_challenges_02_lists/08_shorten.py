# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


def li(user_list):
    max_list = 5
   
    while len(user_list) >  max_list:
        list_user = user_list.pop()
    print("This is your list after modifications ",list_user)

def main():
     user_list = [1,2,3,4,5,6,7,8,9,10]
     print(f"{user_list} This is original list :")
     li(user_list)
     print(f"{user_list} Final list")
if  __name__ == "__main__":
    main()   

