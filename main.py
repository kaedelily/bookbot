def get_book_text(book):
     with open(book) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    book_text = get_book_text(/books/frankenstein.txt) # type: ignore
    print(book_text)

main()