import sys
from stats import count_words, count_chars, sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():

        # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # the path to the book file

    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars = count_chars(book_text)
    sorted_list = sorted_chars(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()