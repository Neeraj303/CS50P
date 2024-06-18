import sys

def main():

    count = 0

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 2:
        code_file = sys.argv[1]

        if code_file.endswith(".py"):
            count = lines_in_file(code_file)
            print(count)
        else:
            sys.exit("Not a Python file")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def lines_in_file(code_file):
    count = 0
    with open(f'{code_file}') as file:
        for line in file:
            if line.lstrip().startswith("#") | line.isspace():
                pass
            else:
                count+=1
        return count


if __name__ == "__main__":
    main()



