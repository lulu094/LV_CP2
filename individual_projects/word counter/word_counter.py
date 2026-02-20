# LV 1st Word Counter

# main.py 

# import view_document from file_handling
# import add_content_to_document from file_handling
# import update_document_info from file_handling

# define function display_menu()
    # print blank line
    # print "--- Document Word Count Updater ---"
    # print "1. Update document info"
    # print "2. View document"
    # print "3. Add content to document"
    # print "4. Exit"

# define function main()

    # create variable document_path
    # set document_path equal to empty string

    # create variable user_choice
    # set user_choice equal to 0

    # start while loop that runs until user_choice equals 4

        # call display_menu()

        # ask user: "Enter your choice (1-4): "
        # store input in user_choice
        # convert user_choice to integer

        # if user_choice equals 1
            # if document_path is empty
                # ask user: "Enter the exact file path for your document: "
                # store input in document_path
            # call update_document_info(document_path)

        # else if user_choice equals 2
            # if document_path is empty
                # ask user for file path
                # store in document_path
            # call view_document(document_path)

        # else if user_choice equals 3
            # if document_path is empty
                # ask user for file path
                # store in document_path
            # call add_content_to_document(document_path)

        # else if user_choice equals 4
            # print "Exiting program..."

        # else
            # print "Invalid choice. Please select 1-4."

    # end while loop

# call main() to start program

# file_handling.py 

# import get_formatted_time from time_handling


# define function read_file(file_path)
    # open the file using file_path in read mode
    # read entire contents into variable file_text
    # close the file
    # return file_text


# define function clean_text(raw_text)
    # remove leading and trailing whitespace
    # remove extra blank lines at the end
    # return cleaned text


# define function count_words(text)
    # split text into a list using whitespace
    # remove empty strings from the list
    # count number of items in the list
    # return word count


# define function write_file(file_path, updated_text)
    # open the file using file_path in write mode
    # write updated_text to the file
    # close the file


# define function append_to_file(file_path, text_to_add)
    # open the file using file_path in append mode
    # write text_to_add at bottom of file
    # close the file


# define function view_document(file_path)
    # call read_file(file_path)
    # store result in file_contents

    # call clean_text(file_contents)
    # store result in cleaned_contents

    # print blank line
    # print "Document content:"
    # print cleaned_contents


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



# ==========================================================
#  time_handling.py 

# import datetime module


# define function get_current_time()
    # use datetime.now() to get current date and time
    # return raw datetime object


# define function format_time(raw_datetime)
    # convert raw_datetime into formatted string
    # format should be:
    # YYYY-MM-DD HH:MM:SS
    # return formatted string


# define function get_formatted_time()
    # call get_current_time()
    # store result in raw_time

    # call format_time(raw_time)
    # store result in clean_time

    # return clean_time
