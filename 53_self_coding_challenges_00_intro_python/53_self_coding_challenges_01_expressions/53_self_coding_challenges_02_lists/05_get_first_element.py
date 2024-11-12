# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
def get_first_element(lst):
    print(lst[0])

user_input = []
user =int(input("Enter  the elements you want to enter: "))
for i in range(user):
    element= input(f"Enter value -> {i+1}")
    user_input.append(element)
      

get_first_element(user_input)



