import json
from difflib import get_close_matches


def search_french():
    search_term = input("enter search term: ").casefold()
    with open('eng_french.json'.format(1), encoding='utf-8') as data:
        term_data = json.load(data)
    if search_term in term_data:
        print(f"{search_term} - {term_data[search_term]}")
    elif len(get_close_matches(search_term, term_data.keys())) > 0:
        enq = input("Are you looking for the word '%s' ? Enter 'Y' for Yes and 'N' for No: " %
                    get_close_matches(search_term, term_data.keys())[0])
        if enq.casefold() == 'y':
            print(f"{term_data[get_close_matches(search_term, term_data.keys())[0]]}")
        elif enq.casefold() == 'n':
            print("Word not found in the Dictionary.")
            ask = input(f"Is '{search_term}' a new word? Enter 'Y' for Yes and 'N' for No: ")
            if ask.casefold() == 'y':
                print("Do you want to write the new word in the dictionary? ")
                query = input("Enter 'Y' for Yes and 'N' for No: ")
                if query.casefold() == 'y':
                    write_french()
                else:
                    print("""
                    Sorry for the inconvenience. Word will be updated.
                    Thank you for using the Dictionary.  
                    """)
            elif ask.casefold() == 'n':
                while True:
                    ask_again = input("Do you want to search again? Enter 'Y' for Yes and 'N' for No : ")
                    if ask_again.casefold() == 'y':
                        search_french()
                    elif ask_again.casefold() == 'n':
                        print("Thank you for using the Dictionary.")
                        break
                    else:
                        print("Please enter either 'Y' or 'N'.")

        else:
            print("Please enter either 'Y' or 'N'.")
    else:
        print("No word entered!")
        search_french()


def write_french():
    term = input("enter term: ")
    define_term = input("enter the definition of term: ")
    with open('eng_french.json') as data:
        term_data = json.load(data)
    term_data[term] = define_term
    with open('eng_french.json'.format(1), 'w', encoding='utf-8') as data:
        json.dump(term_data, data)
    print("New word is added to your dictionary.")


def search_german():
    search_term = input("enter search term: ").casefold()
    with open('eng-german.json'.format(1), encoding='utf-8') as data:
        term_data = json.load(data)
    if search_term in term_data:
        print(f"{search_term} - {term_data[search_term]}")
    elif len(get_close_matches(search_term, term_data.keys())) > 0:
        enq = input("Are you looking for the word '%s' ? Enter 'Y' for Yes and 'N' for No: " %
                    get_close_matches(search_term, term_data.keys())[0])
        if enq.casefold() == 'y':
            print(f"{term_data[get_close_matches(search_term, term_data.keys())[0]]}")
        elif enq.casefold() == 'n':
            print("Word not found in the Dictionary.")
            ask = input(f"Is '{search_term}' a new word? Enter 'Y' for Yes and 'N' for No: ")
            if ask.casefold() == 'y':
                print("Do you want to write the new word in the dictionary? ")
                query = input("Enter 'Y' for Yes and 'N' for No: ")
                if query.casefold() == 'y':
                    write_german()
                else:
                    print("""
                    Sorry for the inconvenience. Word will be updated.
                    Thank you for using the Dictionary.  
                    """)
            elif ask.casefold() == 'n':
                while True:
                    ask_again = input("Do you want to search again? Enter 'Y' for Yes and 'N' for No : ")
                    if ask_again.casefold() == 'y':
                        search_german()
                    elif ask_again.casefold() == 'n':
                        print("Thank you for using the Dictionary.")
                        break
                    else:
                        print("Please enter either 'Y' or 'N'.")

        else:
            print("Please enter either 'Y' or 'N'.")
    else:
        print("No word entered!")
        search_german()


def write_german():
    term = input("enter term: ")
    define_term = input("enter the definition of term: ")
    with open('eng-german.json') as data:
        term_data = json.load(data)
    term_data[term] = define_term
    with open('eng-german.json'.format(1), 'w', encoding='utf-8') as data:
        json.dump(term_data, data)
    print("New word is added to your dictionary.")


def search_mandrin():
    search_term = input("enter search term: ").casefold()
    with open('eng_mandrin.json'.format(1), encoding='utf-8') as data:
        term_data = json.load(data)
    if search_term in term_data:
        print(f"{search_term} - {term_data[search_term]}")
    elif len(get_close_matches(search_term, term_data.keys())) > 0:
        enq = input("Are you looking for the word '%s' ? Enter 'Y' for Yes and 'N' for No: " %
                    get_close_matches(search_term, term_data.keys())[0])
        if enq.casefold() == 'y':
            print(f"{term_data[get_close_matches(search_term, term_data.keys())[0]]}")
        elif enq.casefold() == 'n':
            print("Word not found in the Dictionary.")
            ask = input(f"Is '{search_term}' a new word? Enter 'Y' for Yes and 'N' for No: ")
            if ask.casefold() == 'y':
                print("Do you want to write the new word in the dictionary? ")
                query = input("Enter 'Y' for Yes and 'N' for No: ")
                if query.casefold() == 'y':
                    write_mandarin()
                else:
                    print("""
                    Sorry for the inconvenience. Word will be updated.
                    Thank you for using the Dictionary.  
                    """)
            elif ask.casefold() == 'n':
                while True:
                    ask_again = input("Do you want to search again? Enter 'Y' for Yes and 'N' for No : ")
                    if ask_again.casefold() == 'y':
                        search_mandrin()
                    elif ask_again.casefold() == 'n':
                        print("Thank you for using the Dictionary.")
                        break
                    else:
                        print("Please enter either 'Y' or 'N'.")

        else:
            print("Please enter either 'Y' or 'N'.")


def write_mandarin():
    term = input("enter term: ")
    define_term = input("enter the definition of term: ")
    with open('eng_mandrin.json') as data:
        term_data = json.load(data)
    term_data[term] = define_term
    with open('eng_mandrin.json'.format(1), 'w', encoding='utf-8') as data:
        json.dump(term_data, data)
    print("New word is added to your dictionary.")


def search_italian():
    search_term = input("enter search term: ").casefold()
    with open('eng_ita.json'.format(1), encoding='utf-8') as data:
        term_data = json.load(data)
    if search_term in term_data:
        print(f"{search_term} - {term_data[search_term]}")
    elif len(get_close_matches(search_term, term_data.keys())) > 0:
        enq = input("Are you looking for the word '%s' ? Enter 'Y' for Yes and 'N' for No: " %
                    get_close_matches(search_term, term_data.keys())[0])
        if enq.casefold() == 'y':
            print(f"{term_data[get_close_matches(search_term, term_data.keys())[0]]}")
        elif enq.casefold() == 'n':
            print("Word not found in the Dictionary.")
            ask = input(f"Is '{search_term}' a new word? Enter 'Y' for Yes and 'N' for No: ")
            if ask.casefold() == 'y':
                print("Do you want to write the new word in the dictionary? ")
                query = input("Enter 'Y' for Yes and 'N' for No: ")
                if query.casefold() == 'y':
                    write_italian()
                else:
                    print("""
                    Sorry for the inconvenience. Word will be updated.
                    Thank you for using the Dictionary.  
                    """)
            elif ask.casefold() == 'n':
                while True:
                    ask_again = input("Do you want to search again? Enter 'Y' for Yes and 'N' for No : ")
                    if ask_again.casefold() == 'y':
                        search_italian()
                    elif ask_again.casefold() == 'n':
                        print("Thank you for using the Dictionary.")
                        break
                    else:
                        print("Please enter either 'Y' or 'N'.")

        else:
            print("Please enter either 'Y' or 'N'.")


def write_italian():
    term = input("enter term: ")
    define_term = input("enter the definition of term: ")
    with open('eng_ita.json') as data:
        term_data = json.load(data)
    term_data[term] = define_term
    with open('eng_ita.json'.format(1), 'w', encoding='utf-8') as data:
        json.dump(term_data, data)
    print("New word is added to your dictionary.")




