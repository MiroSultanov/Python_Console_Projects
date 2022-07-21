import re
password = input()
flag = 0
while True:
    if len(password) < 8:
        flag = -1
        print("Not a Valid Password")
        break
    elif not re.search("[a-z]", password):
        flag = -1
        print("Not a Valid Password")
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        print("Not a Valid Password")
        break
    elif not re.search("[0-9]", password):
        flag = -1
        print("Not a Valid Password")
        break
    elif not re.search("[_@$]", password):
        flag = -1
        print("Not a Valid Password")
        break
    elif re.search("\s", password):
        flag = -1
        print("Not a Valid Password")
        break
    else:
        flag = 0
        print("Valid Password")
        break