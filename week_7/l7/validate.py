# email = input("Enter your email: ").strip()


# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

import re

email = input("Enter your email: ").strip()

# if re.search(r"^[^@]+@[^@]+\.edu$", email): # r indicates the raw string, \ is escape character
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#if re.search(r"^\w+@\w+\.(edu|ac\.in)$", email): #\w is the word character, alpha numeric, word and underscore, nut no space and .
# if re.search(r"^\w+@\w+\.(?:edu|ac\.in)$", email): #?: no capturing version
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# re.match(patern, string, flag = 0) # no ^ symbol, automatically start matching from the start of the symbol
# re.fullmatch(pattern, string, flag = 0) no ^, $ symbol