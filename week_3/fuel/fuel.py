def main():
    y = fuel_gauge()
    if y <= 1:
        print("E")
    elif y >= 99:
        print("F")
    else:
        print(f"{y}%")

def fuel_gauge():
    while True:
        try:
            x, y = (input("Fraction: ")).split("/")
            if int(x) > int(y):
                continue
            return round((int(x)/int(y)) * 100)
        except (ValueError, ZeroDivisionError):
            pass


main()


