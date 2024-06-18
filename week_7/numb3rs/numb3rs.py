import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if values := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        a = 1
        if 0 <= int(values.group(1)) <= 255:
            for i in range(2, 5):
                a = numeric_range(values.group(i))*a
            return a == True
        else:
            return False
    else:
        return False


def numeric_range(num):
    try:
        if (int(num) <= 255 and int(num) >= 0):
            return True
        else:
            return False
    except ValueError:
        return False



if __name__ == "__main__":
    main()
