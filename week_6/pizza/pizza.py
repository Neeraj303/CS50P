import sys
from tabulate import tabulate
import csv

def main():
    file_path = check_argument()
    print(tabulate(tabular_data(file_path), headers="firstrow", tablefmt = "grid"))

def check_argument():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        if not (sys.argv[1]).endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            return sys.argv[1]
    else:
        sys.exit("Too many command line arguments")

def tabular_data(file_path):
    data = []
    with open(f"{file_path}") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    main()
