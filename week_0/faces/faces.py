def main():
    s = input("What is the input? ")
    convert(s)

def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    print(s)

main()

