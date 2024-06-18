import random

def main():
    n = get_level()

    i, j, score = 0, 0, 0
    while i < 10:
        x, y = generate_integer(n)
        j=0
        while j < 3:
            try:
                m = int(input(f'{x} + {y} = '))
                if m == x+y:
                    score+=1
                    break
                else:
                    print("EEE")
                    j+=1
            except ValueError:
                    print("EEE")
                    j+=1
        i+=1
        if j == 3:
            print(f'{x} + {y} = {x+y}')
    print(f'Score: {score}')



def get_level():
    while True:
        try:
            m = int(input("Level: "))
            if 1 <= m <= 3:
                return m
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()
