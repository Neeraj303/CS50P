import sys


names = []
while True:
    try:
        n = input("Name: ")
        names.append(n)
    except:
        break

if len(names) == 1:
    print()
    print("Adieu, adieu, to", names[0] )
elif len(names) == 2:
    print()
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    print()
    print("Adieu, adieu, to ", end="")
    for name in names[0:-1]:
        print(name, end=", ")
    print(f'and {names[-1]}')


