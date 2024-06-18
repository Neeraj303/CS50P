import random

while True:
    n = input("Level: ")
    try:
        if int(n) > 0:
            break
    except ValueError:
        continue

a = random.randint(1, int(n))


while True:
    m = input("Guess: ")
    try:
        if int(m) < int(a):
            print("Too small!")
            continue
        elif int(m) > int(a):
            print("Too large!")
            continue
        else:
            print("Just Right!")
            break
    except ValueError:
        continue

