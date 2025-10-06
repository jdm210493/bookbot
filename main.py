# python
import sys
from stats import count_words, count_chars, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]

def get_book_text(filepath): # open the file at 'filepath' and ensure it closes automatically
     with open(filepath) as f: # read the entire file into a single string
        return f.read()

def main(path):
    text = get_book_text(path) # get the book text by reading the file

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    num_words = count_words(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    chars = count_chars(text) # Calls the count_chars function to count how many times each character appears in book_content.
    sorted_chars = sorted_list(chars) # Passes the character count dictionary to sorted_list, which returns a sorted list of dictionaries

    print("--------- Character Count -------")
 
    for item in sorted_chars: #  loops through the sorted list and prints each character and its count in the format: character: count
       print (f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main(path)
