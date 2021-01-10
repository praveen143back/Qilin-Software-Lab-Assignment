import re

passwords = input("Please Enter The Multiple Passwords Seperated By Comma: ")
passwords = passwords.split(",")

password_res= []
for i in passwords:

    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        password_res.append(i)

print((" ").join(password_res))