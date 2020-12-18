import json
from difflib import get_close_matches


def search_mandrin():
    search_term = input("enter search term: ").casefold()
    with open('eng_mandrin.json') as data:
        term_data = json.load(data)
    print(f"{search_term} - {term_data[search_term]}")


def write():
    term = input("enter term: ")
    define_term = input("enter the definition of term: ")
    with open('eng_mandrin.json') as data:
        term_data = json.load(data)
    term_data[term] = define_term
    with open('eng_mandrin.json', 'w') as data:
        json.dump(term_data, data)
    print("New word is added to your dictionary.")