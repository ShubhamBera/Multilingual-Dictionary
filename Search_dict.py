from eng_to_eng import search_bengali, search_hindi, search
from eng_to_french import search_italian, search_mandrin, search_german, search_french


def search_dict():
    print("""
            Which dictionary you want to access :
            For English to English press 'E'
            For English to Hindi press 'H'
            For English to French press 'F'
            For English to German press 'G'
            For English to Chinese press 'C'
            For English to Bengali press 'B'
            For English to Italian press 'I'
            """)
    ask = input("Enter your option: ").casefold()
    while ask == "e" or "f" or "g" or "c" or "h" or "b" or "i":
        if ask == 'e':
            search()
            exit(0)
        elif ask == 'f':
            search_french()
            exit(0)
        elif ask == 'g':
            search_german()
            exit(0)
        elif ask == 'c':
            search_mandrin()
            exit(0)
        elif ask == 'h':
            search_hindi()
            exit(0)
        elif ask == 'i':
            search_italian()
            exit(0)
        elif ask == 'b':
            search_bengali()
            exit(0)
        else:
            print("please enter the correct response.")
            break
