
# python
from stats import count_words

def get_book_text(filepath):
    #open the file at 'filepath' and ensure it closes automatically
     with open(filepath) as f:
        # read the entire file into a single string
        book_content = f.read()
        # give the text back to the caller
        return book_content

def main():
    # relative path to the book file from this script
    path = "books/frankenstein.txt"
    # get the book text by reading the file
    book_content = get_book_text(path)
    num_words = count_words(book_content)
    print(f"{num_words} words found in the document")  

# run the program when this file is executed
main()
