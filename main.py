def get_book_text(path):
     with open(path) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    import sys # Import the sys module for system-specific parameters and functions
    if len(sys.argv) != 2: # Check if the script is run with the correct number of arguments
        print("Usage: python3 main.py <path_to_book>") # Print the usage message if the number of arguments is incorrect
        sys.exit(1) # Exit the program with an error code if the usage is incorrect
    from stats import count_words # Import the count_words function from the stats.py file > used in main function
    from stats import sort_characters # Import the sort_on function from the stats.py file > used in main function
    book_path = sys.argv[1] # Path to the book file > used in get_book_text function
    book_text = get_book_text(book_path) # Function to read the book text > used in count_words function
    print(book_text)

main()