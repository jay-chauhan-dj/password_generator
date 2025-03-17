import random  # Importing the random module to randomly generate characters
import string  # Importing the string module to access letters, digits, and punctuation

def generate_password():
    # Get password length from user input
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))  # Prompt user for password length
            if length < 6:  # Ensure password length is at least 6 characters
                print("Password length must be at least 6.")  # Inform user of minimum length requirement
                continue  # Restart loop if condition is not met
            break  # Exit loop if valid input is received
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle non-integer inputs
    
    # Check if user wants a prefix for the password
    use_prefix = input("Do you want a prefix? (yes/no, y/n): ").strip().lower()  # Prompt for prefix choice and standardize input
    prefix = ""  # Initialize prefix as an empty string
    if use_prefix in ['y', 'yes']:  # Check if user opted for a prefix
        while True:
            prefix = input("Enter the prefix: ")  # Prompt user to enter prefix
            max_prefix_length = length - 6  # Calculate maximum allowed prefix length (to leave space for strong characters)
            if len(prefix) > max_prefix_length:  # Check if prefix exceeds allowed length
                print(f"Prefix length should be at most {max_prefix_length} characters.")  # Inform user of maximum length
            else:
                break  # Exit loop if valid prefix is provided
    
    # Define remaining length for the password excluding the prefix
    remaining_length = length - len(prefix)  # Calculate remaining space for password characters
    if remaining_length < 6:  # Ensure there is enough space for secure characters
        print("Password length must allow for at least 6 random characters after the prefix.")  # Inform user if not enough space
        return  # Exit function
    
    # Define allowed special characters
    special_characters = "#$&!@%"  # Limited set of special characters
    
    # Ensure at least one character from each category is included
    characters = (
        random.choice(string.ascii_uppercase) +  # At least one uppercase letter
        random.choice(string.ascii_lowercase) +  # At least one lowercase letter
        random.choice(string.digits) +  # At least one digit
        random.choice(special_characters)  # At least one special character
    )
    
    # Generate the rest of the password with random choices from all allowed character types
    other_chars = ''.join(random.choices(
        string.ascii_letters + string.digits + special_characters,  # Pool of characters to choose from
        k=remaining_length - 4  # Remaining number of characters needed after ensuring minimum constraints
    ))
    
    # Combine mandatory characters with randomly selected characters
    password_body = list(characters + other_chars)  # Convert to list to allow shuffling
    random.shuffle(password_body)  # Shuffle characters to avoid predictable patterns
    strong_password = prefix + ''.join(password_body)  # Append prefix (if any) and combine characters into a final string
    
    # Display the generated password
    print(f"Generated Strong Password: {strong_password}")

# Execute function only when script is run directly
if __name__ == "__main__":
    generate_password()  # Call the password generation function
