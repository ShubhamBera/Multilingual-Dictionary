def make_account():
    filename = "username"
    with open(filename, "w") as f:
        f.write(input("Enter a username: "))

    filename = "password"
    with open(filename, "w")  as f:
        f.write(input("Enter a password: "))


print("Account created.")


def login():
    username = input("Enter your UserId: ")
    password = input("Enter your password: ")
    check()


def check(username=None, password=None):
    if username == open("username").read() and password == open("password").read():
        print("Successful Login.")
    else:
        print("Incorrect")
