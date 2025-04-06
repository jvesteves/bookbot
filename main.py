from stats import count_book_words, count_ind_letters,sort_book_dict
import sys


def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print(f"Analyzing book found at {sys.argv[1]}")
        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        count_book_words(get_book_text(sys.argv[1]))
        print("--------- Character Count -------")
        print(sort_book_dict(count_ind_letters(get_book_text(sys.argv[1]))))
        print("============= END ===============")
    

main()

