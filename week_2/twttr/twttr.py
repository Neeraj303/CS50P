def main():
    a = input("Input: ")
    shorter_text(a)


def shorter_text(a):
    for i in range(len(a)):
        if i == 0:
            print("Output: ", end="")
        if a[i] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            print(a[i], end="")
    print()


main()

