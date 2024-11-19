def student_name_manager():
    # Initialize an empty list to store student names and their corresponding IDs
    student_name_list = []
    
    # This condition is used to control the while loop
    condition = True
    
    # Initialize the student ID starting from 1
    Id = 1

    # Start a loop that continues until the user enters 'stop'
    while condition:
        # Ask the user to input a name or 'stop' to end
        user_in = input("Enter your name (if you want to exit, write 'stop'): ")

        # Check if the user input is 'stop' (ignoring case sensitivity)
        if user_in.lower() == 'stop':
            # End the loop by setting condition to False
            condition = False
        else:
            # Check for duplicate names in the list
            duplicate_found = False 
            for student in student_name_list:
                # If a name is found in the list, set duplicate_found to True
                if student[1] == user_in:
                    duplicate_found = True
                    break

            # If a duplicate is found, ask for a unique name
            if duplicate_found:
                print(f"Duplicate name '{user_in}' found. Please enter a unique name.")
            else:
                # Create a tuple with ID and name and add it to the list
                tuple1 = (Id, user_in)
                student_name_list.append(tuple1)
                # Increment the ID for the next student
                Id += 1

    # Print all students and their corresponding IDs
    print("\nComplete list of students with IDs:")
    for student in student_name_list:
        print(f"The ID {student[0]} and name {student[1]}")

    # Calculate the total number of students
    total_students = len(student_name_list)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_name_length = 0
    for student in student_name_list:
        total_name_length += len(student[1])
    print(f"Total length of all student names combined: {total_name_length}")

    # If there are students in the list, find the longest and shortest names
    if student_name_list:
        # Initially set the longest and shortest name as the first student
        longest_name = student_name_list[0]
        shortest_name = student_name_list[0]

        # Loop through the list to find the student with the longest and shortest names
        for student in student_name_list:
            # If the current student's name is longer, update longest_name
            if len(student[1]) > len(longest_name[1]):
                longest_name = student
            # If the current student's name is shorter, update shortest_name
            if len(student[1]) < len(shortest_name[1]):
                shortest_name = student

        # Print the longest and shortest name with their IDs
        print(f"Student with the longest name: {longest_name[1]} (ID: {longest_name[0]})")
        print(f"Student with the shortest name: {shortest_name[1]} (ID: {shortest_name[0]})")

# Call the function to run the program
student_name_manager()


