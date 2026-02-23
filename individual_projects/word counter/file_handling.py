# LV 1st Word Counter - file handling

# import get_formatted_time from time_handling
import time_handling

# define function read_file(file_path)
    # open the file using file_path in read mode
    # read entire contents into variable file_text 
    # close the file
    # return file_text

def read_file(file_path):
    with open(file_path, 'r') as file:
        file_text = file.read()
    return file_text

# define function clean_text(raw_text)
    # remove leading and trailing whitespace
    # remove extra blank lines at the end
    # return cleaned text

def clean_text(raw_text):
    cleaned_text = raw_text.strip()
    while cleaned_text.endswith('\n'):
        cleaned_text = cleaned_text[:-1]
    return cleaned_text


# define function count_words(text)
    # split text into a list using whitespace
    # remove empty strings from the list
    # count number of items in the list
    # return word count

def count_words(raw_text):
    words = raw_text.split()
    words = [word for word in words if word.strip()]
    return len(words)

# define function write_file(file_path, updated_text)
    # open the file using file_path in write mode
    # write updated_text to the file
    # close the file

def write_file(file_path, updated_text):
    with open(file_path, 'w') as file:
        file.write(updated_text)

# define function append_to_file(file_path, text_to_add)
    # open the file using file_path in append mode
    # write text_to_add at bottom of file
    # close the file

def append_to_file(file_path, text_to_add):
    with open(file_path, 'a') as file:
        file.write(text_to_add)

# define function view_document(file_path)
    # call read_file(file_path)
    # store result in file_contents

    # call clean_text(file_contents)
    # store result in cleaned_contents

    # print blank line
    # print "Document content:"
    # print cleaned_contents

def view_document(file_path):
    file_contents = read_file(file_path)
    cleaned_contents = clean_text(file_contents)
    print()
    print("Document content:")
    print(cleaned_contents)

# define function add_content_to_document(file_path)

    # print blank line
    # print "Enter new content (press Enter twice to finish):"

    # create variable new_content
    # set new_content equal to empty string

    # start loop
        # read one line of input from user
        # if line is empty
            # break loop
        # add line plus newline character to new_content
    # end loop

    # call append_to_file(file_path, new_content)

    # print blank line
    # print "Content added successfully."

def add_content_to_document(file_path):
    print()
    print("Enter new content (press Enter twice to finish):")
    new_content = ""
    while True:
        line = input()
        if line == "":
            break
        new_content += line + "\n"
    append_to_file(file_path, new_content)
    print()
    print("Content added successfully.")

# define function update_document_info(file_path)

    # call read_file(file_path)
    # store result in file_contents

    # call clean_text(file_contents)
    # store result in cleaned_contents

    # call count_words(cleaned_contents)
    # store result in word_total

    # call get_formatted_time()
    # store result in current_timestamp

    # create variable update_block
        # set update_block equal to:
        # newline
        # "Word Count: " + word_total
        # newline
        # "Last Updated: " + current_timestamp
        # newline

    # call append_to_file(file_path, update_block)

    # print "Document updated. Word count: " + word_total
def update_document_info(file_path):
    file_contents = read_file(file_path)
    cleaned_contents = clean_text(file_contents)
    word_total = count_words(cleaned_contents)
    current_timestamp = time_handling.get_formatted_time()
    update_block = f"\nWord Count: {word_total}\nLast Updated: {current_timestamp}\n"
    append_to_file(file_path, update_block)
    print(f"Document updated. Word count: {word_total}")

#FIGURE OUT HOW TO PRINT THE UPDATE IN ITS OWN FILE, and CONECT THE THREE PAGES TOGETHER