# LV 1st Simple Morse Code Translator


# 1. Display a main menu with three options
# 2. If user chooses English to Morse:
#       - Ask for English input
#       - Convert each character to Morse using tuples
# 3. If user chooses Morse to English:
#       - Ask for Morse input
#       - Convert each Morse symbol to English using tuples
# 4. Repeat menu until user chooses Exit


# Tuple of English characters
english_chars = (
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9',' ','.',',','?'
)

# Tuple of corresponding Morse code symbols
morse_chars = (
    '.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--',
    '-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',
    '-----','.----','..---','...--','....-','.....','-....','--...','---..','----.',
    '/', '.-.-.-','--..--', '..--..'
)

def is_valid_english(text):
    """Return True if text contains only valid English characters"""
    for char in text.upper():
        if char not in english_chars:
            return False
    return True

# Function to translate English to Morse code
def english_to_morse():
    # Ask the user for English input
    # Make sure the input is written in english not morse code
    # Checking for only words but it if it has . - / that are not used in a sentence then ask them to use the correct opiton get them back to the main menu

    text = input("Enter English text to translate: ").upper()

    # Validate input
    if not is_valid_english(text):
        print("Invalid input.")
        print("Please use English letters, numbers, spaces, or . , ? only.")
        print("Returning to main menu.")
        return

    morse_output = []

    for char in text:
        index = english_chars.index(char)
        morse_output.append(morse_chars[index])

    print("Your message says:")
    print(' '.join(morse_output))


def is_valid_morse(text):
    """Return True if text contains only valid Morse characters"""
    allowed = {'.', '-', '/', ' '}
    for char in text:
        if char not in allowed:
            return False
    return True

# Function to translate Morse code to English
def morse_to_english():
    # Ask the user for English input
    # Make sure the input is written in english not morse code
    # Checking for only words but it if it has . - / that are not used in a sentence then ask them to use the correct opiton get them back to the main menu

    morse_input = input(
        "Enter Morse code (separate letters with spaces, words with /): "
    )

    # Validate input
    if not is_valid_morse(morse_input):
        print("Invalid input.")
        print("Please use only '.', '-', '/', and spaces.")
        print("Returning to main menu.")
        return

    english_output = []
    symbols = morse_input.split()

    for symbol in symbols:
        if symbol in morse_chars:
            index = morse_chars.index(symbol)
            english_output.append(english_chars[index])
        else:
            english_output.append('?')

    print("Your message says:")
    print(''.join(english_output).lower())

# Function for the main menu
def main_menu():
    """Display menu and control program flow"""
    while True:
        print("\nSimple Morse Code Translator")
        print("1. Translate Morse Code to English")
        print("2. Translate English to Morse Code")
        print("3. Exit")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            morse_to_english()
        elif choice == '2':
            english_to_morse()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.")


# Start the program
main_menu()

# TEST THE CODE ONCE I HAVE MAE SURE THE USER INPUT IS CORRECT AND THAT EVERYTHING FROM THE RUBRIC HAS BEEN USED
