# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
def get_last_element(lst):
    last_element = lst[-1]
    print(f"This is your last value :{last_element} ")

user_list = []
user_input = int (input("Enter  the number of elements you want in your list: "))
for i  in range(user_input):
    user_input2= input(f"Enter your {i+1}-> ")
    user_list.append(user_input2)

get_last_element(user_list)

