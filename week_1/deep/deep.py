a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

match a.lower().replace(" ", ""):
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
