def get_book_text(path):
     with open(path) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    book_text = get_book_text("books_frankenstein_txt") 
    print(book_text)

main()