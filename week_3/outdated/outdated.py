def main():
    a = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    correct_date(a)

def correct_date(a):
    while True:
        try:
            x = input("Date: ")
            if "/" in x:
                m, d, y = x.replace(" ", "").split("/")
                if int(m) <= 12 and int(d) <= 31:
                    return print(f'{y}-{int(m):02}-{int(d):02}')
            elif "," in x:
                m, d, y = x.replace(",", "").split(" ")
                if m in a and int(d) <= 31:
                    m = a.index(m) + 1
                    return print(f'{y}-{int(m):02}-{int(d):02}')
                else:
                    continue
        except:
            continue

main()
