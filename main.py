from stats import word_count, char_count, sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    return text.replace('\n', ' ').replace('\r', '').replace('  ', ' ')


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    characters = char_count(book_text)
    sorted_chars = sorted_list(characters)

    print ("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()