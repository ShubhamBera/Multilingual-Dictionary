from itertools import count
import re
from eng_to_eng import write_bengali, write_hindi, write_english
from eng_to_french import write_mandarin, write_italian, write_french, write_german
import Search_dict
from random import random


def make_account():
    name = input("Enter your username: ")
    if name == '':
        print("Please enter a Username.")
        make_account()
    else:
        try:
            username = name + '@.com' + random(1, 9999)
            print("Your Login_ID has been created and is", username, ".")
            password = input('Enter your password: ')
            while len(password) < 4:
                print("Password should be greater than 4.")
                password = input('Enter your password: ')
            else:
                file = open("Login.txt", "r")
                for line in file:
                    if username in line:
                        print("invalid")
                        exit()
                file = open("Login.txt", "a")
                file.write(username)
                file.write(",")
                file.write(password)
                file.write("\n")
                file.close()
        except TypeError:
            print("Please use @.com and any integer between 1 and 9999 in your username.")


def login():
    attempts = 0
    while attempts < 3:
        user_ID = input("Enter your login_ID : ")
        Password = input("Enter your password: ".format(password='*'))
        logged_in = True
        with open('Login.txt', 'r') as file:
            for line in file:
                username, password = line.split(',')
                if username == user_ID:
                    logged_in = password == Password
                    break

        if not logged_in:
            print("Login successful.")
            print("""
                -> To write in dictionary Enter 'W'. 
                -> To Log Out Enter 'logout' 
                """)
            choice = input("Enter the option: ").casefold()
            if choice == 'w':
                print("""
                            Which dictionary you want to write in :
                            For English to English press 'E'
                            For English to Hindi press 'H'
                            For English to French press 'F'
                            For English to German press 'G'
                            For English to Chinese press 'C'
                            For English to Bengali press 'B'
                            For English to Italian press 'I'
                            """)
                ask = input("Enter your option:").casefold()
                if ask == 'e':
                    write_english()
                    exit(0)
                elif ask == 'f':
                    write_french()
                    exit(0)
                elif ask == 'g':
                    write_german()
                    exit(0)
                elif ask == 'c':
                    write_mandarin()
                    exit(0)
                elif ask == 'h':
                    write_hindi()
                    exit(0)
                elif ask == 'i':
                    write_italian()
                    exit(0)
                elif ask == 'b':
                    write_bengali()
                    exit(0)
            elif choice == 'logout':
                login()
        else:
            attempts += 1
            print("Invalid login_ID.")
            if attempts == 3:
                print("You have reached maximum attepts to login.")
                ask = input("Do you have an account\n"
                            "If yes Enter 'y': ").casefold()
                if ask == 'y':
                    print("Try again.")
                    login()
                else:
                    print("""
                    You need to crate an account to write in dictionary.
                    """)
                    ask_again = input("Do you want to create an account to proceed to write in dictionary ?\n"
                                      "if yes Enter 'y")
                    if ask_again == 'y':
                        make_account()
                    else:
                        print("Do you want to keep searching.")
                        ask_search = input("If yes Enter 'y': ")
                        if ask_search == 'y':
                            Search_dict.search_dict()
                        else:
                            print("Thank you for using the dictionary.")
                            exit()
