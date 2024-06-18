import sys
import requests
import json

def main():
    if len(sys.argv) == 1:
        print("Missing command-line argument")
    else:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
#    print(json.dumps(response.json(), indent=2))
    for i, j in o["bpi"]["USD"].items():
        if i == "rate":
            print(f'${n*float(j.replace(",", "")):,.4f}')

main()






