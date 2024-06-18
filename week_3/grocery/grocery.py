def main():
    shop_list()


def shop_list():
    a = []
    b = {}
    while True:
        try:
            a.append(input().upper())
        except EOFError:
            print()
            a.sort()
            for i in range(len(a)):
                count = 0
                if a[i] not in b.keys():
                    for j in range(i,len(a)):
                        if a[j] == a[i]:
                            count+=1
                    b[a[i]] = count
                    print(f'{count} {a[i]}')
            break


main()
