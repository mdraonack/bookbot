def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def get_number_of_words(path_to_book):
    return len(get_book_text(path_to_book).split())

def get_character_count(path_to_book):
    string_dict = {}
    book = get_book_text(path_to_book).lower()
    for char in book:
        if char not in string_dict:
            string_dict[char] = 1
        else:
            string_dict[char] += 1
    return string_dict

def sort_on(items):
    return items["num"]

def get_list_of_dict(path_to_book):
    expected = []
    for key, value in get_character_count(path_to_book).items():
        if not key.isalpha():
            continue
        else:
            expected.append({"char": key, "num": value})

    expected.sort(reverse=True, key= sort_on)
    return expected

def get_report(path_to_book):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_number_of_words(path_to_book)} total words")
    print(f"----------- Character Count -------")
    for item in get_list_of_dict(path_to_book):
        print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")