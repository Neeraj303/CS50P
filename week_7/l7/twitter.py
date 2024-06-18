import re

url = input("What is your twitter url? ").strip()

#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/")
#re.sub(pattern, repl, string, count=0, flags=0)
#username = re.sub(r"^(https|http)://twitter\.com/", "", url)
#username = re.sub(r"^(https?://twitter\.com/", "", url) # does the same work as above
username = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

print(f"Username: {username.group(1)}")
