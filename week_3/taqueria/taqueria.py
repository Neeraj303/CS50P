def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total_amount(menu)


def total_amount(menu):
    total = 0
    while True:
        try:
            y = input("Item: ").lower().title()
            if y in menu.keys():
                total = total + menu[y]
                print(f"Total: ${total:.2f}")
            else:
                pass
        except EOFError:
            break

main()






