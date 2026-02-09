# LV 1st Movie 

# This program recommends movies to the user using information stored

# The CSV file is read at the start of the program and each movie is
# stored as a dictionary inside a list. Each movie dictionary contains:
# title, year, genres, director, actors, and length.

# While loading the CSV file, text data is cleaned by trimming spaces
# and converting strings to lowercase so that searches are not affected
# by capitalization.

# The program includes separate functions to filter movies by:
# - Genre
# - Director
# - Actor
# - Length
import csv
def filter_by_genre(movies, genre):
    results = []
    for movie in movies:
        for g in movie["genres"]:
            if genre in g:
                results.append(movie)
                break
    return results

# Each filter function loops through the current list of movies and
# returns a smaller list that only includes movies matching the user’s
# input.

# After loading the movie list, the program displays a main menu that
# continues to run until the user chooses to exit.

# MAIN MENU OPTIONS:
# 1. Search / Get Recommendations
#    - The user selects one or more filters to apply.
#    - The program starts with the full movie list and applies each
#      selected filter one at a time, narrowing the list.

# 2. Print Full Movie List
#    - Displays every movie from the CSV file in a formatted output.

# 3. Exit
#    - Stops the program.

# SEARCH PROCESS:
# When searching, the user chooses filters by number.
# For each selected filter, the program asks the user for input and
# updates the movie list by calling the matching filter function.

# For genre and actor filters, a movie matches if any genre or actor
# contains the user’s input.

# For the length filter, the user may enter a minimum length, a maximum
# length, or both.

# If no movies match all selected filters, the program displays a
# message telling the user there were no matching results.

# After displaying results, the program returns to the main menu and
# continues running until the user chooses to exit.


def filter_by_director(movies, director):
    results = []
    for movie in movies:
        if director in movie["director"]:
            results.append(movie)
    return results


def filter_by_actor(movies, actor):
    results = []
    for movie in movies:
        for a in movie["actors"]:
            if actor in a:
                results.append(movie)
                break
    return results


def filter_by_length(movies, min_len, max_len):
    results = []

    for movie in movies:
        length = movie["length"]

        if min_len is not None and length < min_len:
            continue
        if max_len is not None and length > max_len:
            continue

        results.append(movie)

    return results


movie_file = "movies.csv"

def load_movies(filename):
    """Load and normalize movie data from CSV."""
    movies = []

    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    movies.append({
                        "title": row["title"].strip(),
                        "year": int(row["year"]),
                        "genres": [g.strip().lower() for g in row["genres"].split("|")],
                        "director": row["director"].strip().lower(),
                        "actors": [a.strip().lower() for a in row["actors"].split("|")],
                        "length": int(row["length"])
                    })
                except (KeyError, ValueError):
                    # Skip malformed records
                    continue
    except FileNotFoundError:
        print("Movie file not found.")
    
    return movies


def print_movie(movie, index=None):
    """Pretty print a single movie."""
    prefix = f"{index}. " if index is not None else ""
    print(
        f'{prefix}Title: "{movie["title"]}" — '
        f'Year: {movie["year"]} — '
        f'Genres: {"|".join(movie["genres"])} — '
        f'Director: {movie["director"].title()} — '
        f'Actors: {", ".join(movie["actors"])} — '
        f'Length: {movie["length"]} min'
    )


def print_movies(movies):
    """Print a list of movies."""
    for i, movie in enumerate(movies, start=1):
        print_movie(movie, i)


def search_movies(movies):
    """Interactive search flow."""
    print("\nChoose filters (comma-separated):")
    print("1. Genre")
    print("2. Director")
    print("3. Actor")
    print("4. Length")

    selected = input("Your choice: ").split(",")

    filtered = movies[:]

    if "1" in selected:
        genre = input("Enter genre: ").strip().lower()
        filtered = filter_by_genre(filtered, genre)

    if "2" in selected:
        director = input("Enter director: ").strip().lower()
        filtered = filter_by_director(filtered, director)

    if "3" in selected:
        actor = input("Enter actor: ").strip().lower()
        filtered = filter_by_actor(filtered, actor)

    if "4" in selected:
        min_len = input("Minimum length (blank for none): ").strip()
        max_len = input("Maximum length (blank for none): ").strip()

        min_len = int(min_len) if min_len else None
        max_len = int(max_len) if max_len else None

        filtered = filter_by_length(filtered, min_len, max_len)

    if not filtered:
        print("\nNo movies match those filters. Try removing one filter.")
    else:
        print("\nResults:\n")
        print_movies(filtered)


def main():
    movies = load_movies(movie_file)

    print("Movie Recommender")
    print("Find movies using genre, director, actor, and length filters.")

    while True:
        print("\nMain Menu")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_movies(movies)
        elif choice == "2":
            print_movies(movies)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
