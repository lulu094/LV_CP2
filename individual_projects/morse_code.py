# LV 1st Simple Morse Code Translator

# Main menu function
# has to let the user choose wether they want to translate English to Morse code or Morse code to English
# Translate English to Morse code - 1
# Translate Morse code to English - 2
# Exit - 3
def main_menu():
    """Displays the main menu and handles user input"""
    while True:
        print("Main Menu:")
        print("1. Translate English to Morse Code")
        print("2. Translate Morse Code to English")
        print("3. Exit")
        choice = input("Please choose an option (1, 2, or 3): ")
        
        if choice == '1':
            english_to_morse()
        elif choice == '2':
            morse_to_english()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Please enter a valid number (1, 2, or 3).")

# make a dictionary for Morse code so we caan easily use it in the tuples 
 morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

# smehow i need to ut translate enlish to morse and morse to english in a tuple so it is not repetitive
# Translate English to Morse Code
# has to take user input for English text and convert it to Morse code
# has to have a space between each Morse code letter
# Translate Morse Code to English
# has to take user input for Morse code and convert it to English text
def choice():


