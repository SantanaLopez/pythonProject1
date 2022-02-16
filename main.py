while True:
    print("What is your name?")
    name = input()
    if name != 'Joe':
        continue
    print("Hello Joe, what is the password. (is it a fish)")
    password = input()
    if password == 'swordfish':
        break
    else:
        print("Wrong password, Please try again")
print("Password granted")
