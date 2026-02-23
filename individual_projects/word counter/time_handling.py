# LV 1st Word counter -  time handling

# import datetime module


# define function get_current_time()
    # use datetime.now() to get current date and time
    # return raw datetime object

def get_current_time():
    from datetime import datetime
    return datetime.now()

# define function format_time(raw_datetime)
    # convert raw_datetime into formatted string
    # format should be:
    # YYYY-MM-DD HH:MM:SS
    # return formatted string

def format_time(raw_datetime):
    return raw_datetime.strftime("%Y-%m-%d %H:%M:%S") # cambiuar esto porque no tiene sentido para moi

# define function get_formatted_time()
    # call get_current_time()
    # store result in raw_time

    # call format_time(raw_time)
    # store result in clean_time

    # return clean_time

def get_formatted_time():
    raw_time = get_current_time()
    clean_time = format_time(raw_time)
    return clean_time
