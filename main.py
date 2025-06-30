from stats import get_num_words
from stats import character_count

def get_book_text(path):
     with open(path) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    words = get_num_words(book_text)
    char_num = character_count(book_text)
    print(char_num)

main()