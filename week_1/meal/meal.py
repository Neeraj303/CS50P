def main():
    a = input("What time is it?" )
    a = convert(a)

    if (7.00 <= a <= 8.00):
        print("breakfast time")
    elif (12.00 <= a <= 13.00):
        print("lunch time")
    elif (18.00 <= a <= 19.00):
        print("dinner time")
    else :
        pass

def convert(time):
    c, b = time.split(":")
    b = int(b)/60
    return int(c) + b


if __name__ == "__main__":
    main()
