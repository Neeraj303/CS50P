def main():
    n = input("Input: ")
    print(shorten(n))

def shorten(word):
    b = ""
    for i in range(len(word)):
        if word[i] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            b = b + word[i]
    return b

if __name__ == "__main__":
    main()
