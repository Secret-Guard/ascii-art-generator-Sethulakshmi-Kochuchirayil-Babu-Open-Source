import pyfiglet

def generate_ascii_art(text):
    try:
        # Fixed Issue 1: Added Argument to figlet_format
        ascii_art = pyfiglet.figlet_format(text)
        return ascii_art
    except Exception as e:
        # Fixed Issue 4: Error Handling for pyfiglet
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_input = input("Enter text to convert to ASCII Art (or type 'exit' to quit): ")
        
        # Fixed Issue 2: Input Validation
        if not user_input:
            print("Error: Input cannot be empty. Please enter some text.")
            continue
        
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break

  
        print(generate_ascii_art(user_input))
