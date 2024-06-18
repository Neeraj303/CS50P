def main():
    a = input("camelCase: ")
    a = snake_case(a).lower()
    print(a)

def snake_case(a):
    i = 0
    while i in range(len(a)):
        if a[i].isupper():
            a = a[:i] + '_' + a[i:]
            i+=2
            continue
        i+=1

    return a

main()




