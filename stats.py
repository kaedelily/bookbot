def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def character_count(get_book_text):
    text = get_book_text.lower() # Get the book text
    characters = {} # Initialize an empty dictionary to count characters
    for chr in text:
        if chr in characters: # Check if the character is already in the dictionary
            characters[chr] += 1
        else:
            characters[chr] = 1
    return characters # Return the character count dictionary