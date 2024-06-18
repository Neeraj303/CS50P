def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if char(s) and fly(s) and letters(s) and length(s):
        return True
    else:
        return False

def char(s):
    for i in range(len(s)):
        if s[i] in (".", " ", ",", "?", ";", ":"):
            return False
    return True

def fly(s):
    for i in range(len(s)):
        if s[i] in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return s[i:].isnumeric()
        elif s[i] == "0":
            return False
    else:
        return True

def letters(s):
    return s[0:2].isalpha()

def length(s):
    return (2 <= len(s) <= 6)

main()
