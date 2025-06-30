def get_book_text(path):
     with open(path) as f: # Open the book file: used in main function in line 2
            return f.read() # Read the content of the book file: replaces the previous get_book_text function

def main():
    book_text = get_book_text("books/frankenstein.txt") 
    words = get_words(book_text)
    print(words + " words found in the document")


def get_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

main()