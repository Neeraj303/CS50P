## False con give True in the below code but None would give Fasle
# a = None
# print(isinstance(a, int))

#import re

# link = input("HTML: ").strip()

# if url := re.search(r".+https?://(?:www.)?youtube.com/embed/(\w+).*", link, re.IGNORECASE):
#     print("Valid")
#     if url := re.search(r".+/embed/(\w+).*", link, re.IGNORECASE):
#         print(f"{url.group(1)}")

#check
# else:
#     print("Invalid")

#!!!!!!!!!!!!!! to check how to add to f -string in python!!!!!!#
# a = "5"
# b = "4"

# # if a == 5 or b == 4:
# # print(f"{a+b}")
# print(f"{a}" + ":00 " f"{b}")

#!!!!!!!! to compare list with a vairable!!!!!!#
# import re

# a = "how.are"

# if match := re.search(r"([\w]+\.+)", a):
#     print(match)

import sys


print(type(sys.argv[1:4]))