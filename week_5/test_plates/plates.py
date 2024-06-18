import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(n):
    def plate_letter(n):
        count = 0
        for i in range(len(n)):
            if n[i].isalpha():
                count+=1
        return (count >= 2)

    def plate_length(n):
        return (6 >= len(n) >= 2)

    def plate_number(n):
        if n.isalpha():
            return True
        for i in range(len(n)):
            if n[i] == '0' and n[i].isnumeric():
                return False
            elif n[i] != '0' and n[i].isnumeric():
                for j in range(i, len(n)):
                    if n[j].isalpha():
                        return False
                return True

    def plate_punc(n): # lesson learned both none and false are different type, None != False, but works same with if statement

        return not any(char in string.punctuation or char == " " for char in n)


    return (plate_punc(n) and plate_number(n) and plate_letter(n) and plate_length(n))


if __name__ == "__main__":
    main()
