# python
def get_book_text(filepath):
    #open the file at 'filepath' and ensure it closes automatically
     with open(filepath) as f:
        # read the entire file into a single string
        contents = f.read()
        # give the text back to the caller
        return contents

def main():
    # relative path to the book file from this script
    path = "books/frankenstein.txt"
    # get the book text by reading the file
    contents = get_book_text(path)
    # display the full contents
    print(contents)

# run the program when this file is executed
main()
