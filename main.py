from stats import get_num_words
from stats import character_count
from stats import sort_characters

def get_book_text(path):
     with open(path) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    words = get_num_words(book_text)
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