amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    a = int(input("Insert Coin: "))
    #change_owed = a - amount_due

    if a in (25, 10, 5):
        amount_due = amount_due - a

    if amount_due <= 0:
        print(f"Change Owed: {-1*amount_due}")
    else:
        print(f"Amount Due: {amount_due}")

