import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if url := re.search(r"<.*https?://(?:www.)?youtube.com/embed/(\w+).*", s, re.IGNORECASE):
        if url := re.search(r".+/embed/(\w+).*", s, re.IGNORECASE):
            return ("https://youtu.be/" + f"{url.group(1)}")
    else:
        return None




...


if __name__ == "__main__":
    main()
