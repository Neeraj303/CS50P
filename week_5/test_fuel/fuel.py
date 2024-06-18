def main():
     while True:
          try:
               n = input("Fraction: ")
               if isinstance(convert(n), int):
                    print(gauge(convert(n)))
                    break
          except (ValueError, ZeroDivisionError):
               continue

def convert(fraction):
     num, den = fraction.split("/")
     if (int(den) == 0):
          raise ZeroDivisionError
     elif (int(num) > int(den)) or (not isinstance(int(num), int)) or (not isinstance(int(den), int)):
          raise ValueError
     else:
          return round(int(num)/int(den)*100)


def gauge(percentage):
     if percentage <= 1:
          return f"E"
     elif percentage >= 99:
          return f"F"
     else:
          return f"{percentage}%"

if __name__ == "__main__":
     main()
