import csv
import sys
from tabulate import tabulate

def main():
    check_argument()

def check_argument():
    if len(sys.argv) == 3:
        check_file(sys.argv[1])
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_file(file_path):
    try:
        with open(f"{file_path}") as input_file:
            reader = csv.DictReader(input_file)
            with open(f'{sys.argv[2]}', 'w', newline="") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    lastname, firstname = row['name'].split(", ")
                    housename = row['house']
                    writer.writerow({'first': firstname, 'last': lastname, 'house': housename})
    except FileNotFoundError:
        sys.exit(f"Could not read {file_path}")


if __name__ == "__main__":
    main()

