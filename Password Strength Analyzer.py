while True:

    p = input("Enter Password: ")
    special = "!@#$%^&*()_=+-"
    count = 8
    upper = False
    lower = False
    digit = False
    symbol = False
        
    if len(p) < 8:
        print("Password is Short")
        count -= 1

    if any(ch.isspace() for ch in p):
        print("Password shouldn't include spaces")
        count -= 1

    if p.lower() in ["password", "password123", "admin123", "12345678", "qwerty123"]:
        print("This password is too common and weak")
        count -= 1

    for i in p:
        if i.isupper():
            upper = True

        elif i.islower():
            lower = True

        elif i.isdigit():
            digit = True

        elif i in special:
            symbol = True

    if upper == False:
        print("Missing uppercase letter")
        count -= 1

    if lower == False:
        print("Missing lowercase letter")
        count -= 1

    if digit == False:
        print("Missing digit")
        count -= 1

    if symbol == False:
        print("Missing special character")
        count -= 1

    print("Password Score:", count, "/ 8")

    if count < 4:
        print("WEAK PASSWORD")

    elif count < 6:
        print("MODERATE PASSWORD")

    else:
        print("STRONG PASSWORD")