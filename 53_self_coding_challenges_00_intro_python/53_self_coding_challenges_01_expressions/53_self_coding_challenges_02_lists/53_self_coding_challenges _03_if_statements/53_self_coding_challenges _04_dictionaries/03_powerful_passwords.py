from hashlib import sha256

def hash_password(password):
    """
    Takes a plain password and returns its SHA256 hashed version.
    """
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Checks if the given email and password match the stored login data.

    email: the email entered by the user
    stored_logins: dictionary with emails and their hashed passwords
    password_to_check: the plain password entered by the user
    
    Returns:
    True if the login is successful, otherwise False.
    """
    # Check if the hashed entered password matches the stored hash
    return stored_logins.get(email) == hash_password(password_to_check)

# Main function to test the login system
def main():
    # Stored email-password pairs with hashed passwords
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # 'password'
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # 'Karel'
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # '123!456?789'
    }
    
    # Test logins with different email-password combinations
    print(login("example@gmail.com", stored_logins, "word"))  # Expected: False
    print(login("example@gmail.com", stored_logins, "password"))  # Expected: True
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # Expected: True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Expected: False
    
    print(login("student@stanford.edu", stored_logins, "password"))  # Expected: False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # Expected: True

# Run the main function if this script is executed
if __name__ == '__main__':
    main()
 