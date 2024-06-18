import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # re.findall return list of matches
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))
    #return len(re.findall(r"\w*um\w*", s, re.IGNORECASE)) # this matches if "um" is part of any word
    #return len(re.findall(r"\ {1}um\ {1}", s, re.IGNORECASE))  # this matches if we have have space at both sides of "um"


if __name__ == "__main__":
    main()
