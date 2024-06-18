a, b, c = input("Expression: ").split()


if b == '+':
    z = int(a) + int(c)
    print(f"{z:.1f}")
elif b == '-':
    z = int(a) - int(c)
    print(f"{z:.1f}")
elif b == '*':
    z = int(a) * int(c)
    print(f"{z:.1f}")
elif b == '/':
    z = int(a) / int(c)
    print(f"{z:.1f}")

