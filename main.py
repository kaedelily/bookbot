from stats import get_num_words
from stats import character_count
from stats import sort_characters

def get_book_text(path):
     with open(path) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    import sys # Import the sys module for system-specific parameters and functions
    if len(sys.argv) != 2: # Check if the script is run with the correct number of arguments
        print("Usage: python3 main.py <path_to_book>") # Print the usage message if the number of arguments is incorrect
        sys.exit(1) # Exit the program with an error code if the usage is incorrect
    book_path = sys.argv[1] # Path to the book file > used in get_book_text function
    book_text = get_book_text(book_path) # Function to read the book text > used in count_words function
    char_num = character_count(book_text)
    char_list = sort_characters(book_text)
    print("============ BOOKBOT ============") # Print the header for the output
    print(f"Analyzing book found at {book_text}...") # Print the path of the book being analyzed
    print("----------- Word Count ----------") # Print the header for the word count section
    print(f"Found {words} total words") # Print the number of words found in the document"
    print("--------- Character Count -------") # Print the header for the character count section
    for item in char_list:
         if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}") # Print each character and its count
    print("============= END ===============") # Print the footer for the output

main()