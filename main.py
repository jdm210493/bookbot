
# python
from stats import count_words, count_chars, sorted_list

def get_book_text(filepath): # open the file at 'filepath' and ensure it closes automatically
     with open(filepath) as f: # read the entire file into a single string
        book_content = f.read() # give the text back to the caller
        return book_content

def main():
    path = "books/frankenstein.txt" # relative path to the book file from this script
    book_content = get_book_text(path) # get the book text by reading the file

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    num_words = count_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    chars = count_chars(book_content) # Calls the count_chars function to count how many times each character appears in book_content.
    sorted_chars = sorted_list(chars) # Passes the character count dictionary to sorted_list, which returns a sorted list of dictionaries

    print("--------- Character Count -------")
    for item in sorted_chars: #  loops through the sorted list and prints each character and its count in the format: character: count
        print (f"{item['char']}: {item['num']}")

    print("============= END ===============")

# run the program when this file is executed
main()
