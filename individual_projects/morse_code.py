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

# Function to translate English to Morse code
def english_to_morse():
    """Translate English text to Morse code"""
    # Ask the user for English input
    # Make sure the input is written in english not morse code
    text = input("Enter English text to translate: ").upper()
    morse_output = []

    # Convert each character to Morse
    for char in text:
        if char in english_chars:
            index = english_chars.index(char)
            morse_output.append(morse_chars[index])
        else:
            morse_output.append('?')  # Error handling

    # Display the translated message
    print("Your message says:")
    print(' '.join(morse_output))

# Function to translate Morse code to English
def morse_to_english():
    """Translate Morse code to English text"""
    # Ask the user for Morse input
    # Make sure the input is written in morse code not english
    morse_input = input(
        "Enter Morse code (separate letters with spaces, words with /): "
    )
    english_output = []

    # Split Morse code into symbols
    symbols = morse_input.split()

    # Convert each Morse symbol to English
    for symbol in symbols:
        if symbol in morse_chars:
            index = morse_chars.index(symbol)
            english_output.append(english_chars[index])
        else:
            english_output.append('?')  # Error handling

    # Display the translated message
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
