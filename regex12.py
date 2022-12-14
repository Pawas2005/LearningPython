# WAP to check email with proper alphabets before "@" and "." after "@"

from re import search, findall


def validate_email(email):

    if search(r"\b[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", email):
        print("Valid Email")
    else:
        print("Invalid Email")
    print(findall(r"\b[a-zA-Z0-9._%+-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", email))


validate_email(input("Enter String: "))
