from eng_to_eng import search, write_english, search_hindi, write_hindi, search_bengali, write_bengali
from eng_to_french import search_french, search_german, search_mandrin, write_mandarin, write_german, write_french, \
    search_italian, write_italian
from Search_dict import search_dict
from Login import login, make_account


print("'*****ENGLISH WORD DICTIONARY*****'")
print("""
In this dictionary you can:
1.Search Term
2.Write Term
""")


while True:
    response = input("Enter to 'Search' or to 'Write' : ")
    if response.casefold() == "search":
        search_dict()
    elif response.casefold() == "write":
        print("""
        To write in dictionary you need to login.
        """)
        sign = input("Do you have an account \n"
                     "If Yes Press 'Y' if No press 'N': ").casefold()
        if sign == 'y':
            print("Then Login to write words in the dictionary.")
            login()
        if sign == 'n':
            ask_sign = input("Do you want to create a account\n"
                             "If Yes Press 'Y': ").casefold()
            if ask_sign == 'y':
                make_account()
                print("Account created")
            else:
                print("""
                To write in dictionary user need to login.
                But user can search the dictionary.  
                """)
                reuse = input("Do you want to search:\n"
                              "If Yes Press 'Y': ").casefold()
                if reuse == 'y':
                    search_dict()
                else:
                    print("thank you for using the dictionary.")
                    exit(0)

    else:
        if response == '':
            print("Thank you for using the dictionary.")
            exit(0)
            break
