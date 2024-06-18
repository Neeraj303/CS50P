name = input("What's your name ? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Neville":
        print("Slytherin")
    case _: # it consider all other cases
        print("Who?")