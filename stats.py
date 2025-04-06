def count_book_words (book_string):
    number_of_words = len(book_string.split())
    print(f"Found {number_of_words} total words")


def count_ind_letters (book_string) :
    letter_count = {}
    for char in book_string.lower():
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def sort_book_dict (book_dict):
    
    def sort_on(dict):
        return dict["count"]
    
    letter_list = []

    for letter, count in book_dict.items():
        dictionary = {}
        dictionary.update({"letterName" : letter,  "count": count})
        letter_list.append(dictionary)

    letter_list.sort(reverse=True, key=sort_on)
    
    for letter in letter_list:
        if letter['letterName'].isalpha():
            print(f"{letter['letterName']}: {letter['count']}")
    

    # sorted_books = dict(sorted(book_dict.items(), key=lambda x:x[1], reverse=True))
    # return sorted_books