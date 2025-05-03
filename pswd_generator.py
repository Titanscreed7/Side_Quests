import itertools
import string
import time
import threading

# Global variable to keep track of password count
password_count = 0
running = True  # Flag to control the password generation

def generate_passwords(length, username):
    global password_count  # Use the global variable

    # Discard everything from the @ sign onward if the username looks like an email
    if '@' in username:
        username = username.split('@')[0]  # Keep only the part before the @

    # Define the character set to include lowercase, uppercase letters, and digits
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Generate all possible combinations of the given length
    for password_tuple in itertools.product(characters, repeat=length):
        password = ''.join(password_tuple)
        
        # Increment the password count
        global password_count
        password_count += 1
        
        # Check if the password contains the username
        if username.lower() in password.lower():  # Case insensitive check
            # You can add logic here if needed for similar passwords
            pass

    # Write all passwords to the file
    with open("generated_passwords.txt", "w") as file:
        for password in itertools.product(characters, repeat=length):
            file.write(''.join(password) + "\n")  # Write each password to the file

def display_password_count():
    while running:
        print(f"Passwords Created: {password_count}")  # Display the count in the console
        time.sleep(20)  # Wait for 20 seconds before updating

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")  # Ask for the username
    length = int(input("Enter character length: "))  # Define the desired password length

    # Start the password generation in a separate thread
    threading.Thread(target=generate_passwords, args=(length, username)).start()
    
    # Start displaying the password count
    display_password_count()

    # Optionally, you can join the thread if you want to wait for it to finish
    # Note: This will block the main thread until the password generation is complete
    # password_thread.join()
