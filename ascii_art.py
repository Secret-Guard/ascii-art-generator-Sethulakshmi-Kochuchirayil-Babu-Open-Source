import pyfiglet

def generate_ascii_art(text):
    # Issue 1: Missing Argument for figlet_format
    ascii_art = pyfiglet.figlet_format()  # No argument is passed
    return ascii_art

if __name__ == "__main__":
    user_input = input("Enter text to convert to ASCII Art: ")
    
    # Issue 2: No Input Validation
    # (No check if input is empty, will break if nothing is entered)
    
    print(generate_ascii_art(user_input))
    
    # Issue 3: No Exit Option
    # (No way to exit the program without using Ctrl+C)
