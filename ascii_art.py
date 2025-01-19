import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    user_input = input("Enter text to convert to ASCII Art: ")
    print(generate_ascii_art(user_input))
