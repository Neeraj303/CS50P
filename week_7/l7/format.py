# name = input("What is your name? ").strip() #remove the backspace at the front and the end

# if "," in name:
#     last, first = name.split(", ?") # ? 0 or 1 ergular expression usage. Split built into string does not allow this so we need to import re
#     name = f"{first} {last}"
# print(f"Hello, {name}")   

#!!!!!!!!!2nd Part!!!!!!!!!!#
# import re

# name = input("What is your name? ").strip()

# matches  = re.search(r"^(\w+), ?(\w+)",  name)

# if matches:
#     #last, first = matches.groups()
#     last = matches.group(1)
#     first = matches.group(2)
#     name = f"{first} {last}"
# print(f"Hello, {name}")

#!!!!!!!!!3rd Part!!!!!!!#
# to combine assignment and boolean statement
import re
name = input("What is your name? ")

if matches := re.search(r"^(\w+), ?(\w+)",  name): # walrus operator
    name = matches.group(2) + " " + matches.group(1)
    print(type(matches.group(2)))

print(f"Hello, {name}")

#!!!!! Imp Point about re.match class (type(matches))!!!!!#
''' They are not iterable
    you can not use len() function on them'''


