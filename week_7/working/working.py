## This is going to be the most dirty code i have written
## Please dont bang your head trying understanding it.

import re
import sys


def main():
    try:
        print(convert(input("Hours: ").strip()))
    except ValueError:
        print("ValueError")
        sys.exit(1)


def convert(s):
        if match := re.search(r"^([0-9]*:?[0-9]*)\ ([A-Z]+)\ (\-?[a-z]*)\ ([0-9]*:?[0-9]*)\ ([A-Z]+)$", s):
            start, am, connector, end, pm = match.groups()
            if connector != "to":
                raise ValueError

            if am == "AM":
                if ":" in start:
                    hour_start, minute_start = start.split(":")
                    if int(minute_start) >= 60 or int(hour_start) > 12:
                        raise ValueError
                    elif int(hour_start) == 12:
                        hour_start = int(hour_start) - 12
                        start = f"{int(hour_start):02d}:{minute_start}"
                    else:
                        start = f"{int(hour_start):02d}:{minute_start}"
                else:
                    if int(start) > 12:
                        raise ValueError
                    elif int(start) == 12:
                        start = int(start) - 12
                        start = f"{int(start):02d}" + ":00"
                    else:
                        start = f"{int(start):02d}" + ":00"

            elif am == "PM":
                if ":" in start:
                    hour_start, minute_start = start.split(":")
                    if int(minute_start) >= 60 or int(hour_start) > 12:
                        raise ValueError
                    elif int(hour_start) == 12:
                        start = f"{hour_start:02d}:{minute_start}"
                    elif int(hour_start) < 12:
                        hour_start = int(hour_start) + 12
                        start = f"{hour_start:02d}:{minute_start}"
                else:
                    if int(start) > 12:
                        raise ValueError
                    elif int(start) == 12:
                        start = int(start)
                        start = f"{int(start):02d}:00"
                    else:
                        start = int(start) + 12
                        start = f"{int(start):02d}:00"

            if pm == "AM":
                if ":" in end:
                    hour_end, minute_end = end.split(":")
                    if int(hour_end) > 12 or int(minute_end) >= 60:
                        raise ValueError
                    elif int(hour_end) == 12:
                        hour_end = int(hour_end) - 12
                        end = f"{int(hour_end):02d}:{minute_end}"
                    else:
                        end = f"{int(hour_end):02d}:{minute_end}"
                else:
                    if int(end) > 12:
                        raise ValueError
                    elif int(end) == 12:
                        end = int(end) - 12
                        end = f"{int(end):02d}:00"
                    else:
                        end = f"{int(end):02d}:00"

            elif pm == "PM":
                if ":" in end:
                    hour_end, minute_end = end.split(":")
                    if int(hour_end) > 12 or int(minute_end) >= 60:
                        raise ValueError
                    elif int(hour_end) == 12:
                        hour_end = int(hour_end)
                        end = f"{hour_end:02d}:{minute_end}"
                    else:
                        hour_end = int(hour_end) + 12
                        end = f"{hour_end:02d}:{minute_end}"
                else:
                    if int(end) > 12:
                        raise ValueError
                    elif int(end) == 12:
                        end = int(end)
                        end = f"{int(end):02d}:00"
                    else:
                        end = int(end) + 12
                        end = f"{int(end):02d}:00"


            return f"{start}" + " to " + f"{end}"
        else:
            raise ValueError


if __name__ == "__main__":
    main()
