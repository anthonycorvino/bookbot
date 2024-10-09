with open("books/frankenstein.txt", "r") as f:
    book_string = f.read()

def num_words(text):
    words = 0
    book = text.split()
    for word in book:
        words += 1
    return words

def num_characters(text):
    num_chars = 0
    char_dict = {}
    lowercase_book = text.lower()
    for char in lowercase_book:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def filter_chars(char_dict):
    filtered_dict = {}
    for char, count in char_dict.items():
        if char.isalpha():
            filtered_dict[char] = count
    return filtered_dict

def sort_dict_by_num(char_dict):
    sorted_dict = {}
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def print_report(sorted_chars):
    for key, value in sorted_chars.items():
        print(f"The '{key}' character was found {value} times")



num_words = num_words(book_string)
sorted_chars = num_characters(book_string)
sorted_chars = filter_chars(sorted_chars)
sorted_chars = sort_dict_by_num(sorted_chars)
print("---- Begin report of books/frankenstein.txt ----")
print(f"{num_words} words found in the document\n")
print_report(sorted_chars)
print("---- End Report ----")

