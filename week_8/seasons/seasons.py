from datetime import date
import sys
import re
import inflect

def main():

    try:
        # Takes input from User
        birth_day = input("Birth Date: ")
        #birth_day = sys.argv[1]
        total_min = get_minutes(birth_day)
        str_total_minutes = inflect.engine().number_to_words(total_min).replace("and ", "")
        print(f"{str_total_minutes[0].upper()}" + f"{str_total_minutes[1:]} minutes")

    except ValueError:
        print("Invalid date")
        sys.exit(1)




def get_minutes(birth_day):
    today = date.today()
    birth_day = date.fromisoformat(birth_day)
    total_days = abs(today - birth_day).days
    total_minutes = total_days * 24 * 60
    return total_minutes


if __name__ == "__main__":
    main()


#!!!!!!!!!! I did not check the hints and wrote this code which took me alot of time!!!!!!#
# def get_minutes(birth_day):
#     today = date.today() # this is not an instance of str class, it is different object

#     # Checking if the given format matches xxxx-xx-xx using re
#     if matches := re.search(r"^(\d{4})\-([0-1][0-9])\-(\d{2})$", birth_day):
#         birth_year  = matches.group(1) # assigning year
#         birth_month = matches.group(2) # assigning month
#         birth_date  = matches.group(3) # assigning date

#             # To check whether the given year, month, date are valid or not
#         if birth_day == date(int(birth_year), int(birth_month), int(birth_date)).isoformat(): #isoformat method gives an str as output
#             total_days = abs(today - date.fromisoformat(birth_day)).days #fromisoformat method to convert birth_day to same object for abs to work
#             total_minutes = total_days * 24 * 60
#             return total_minutes

#         else:
#             raise ValueError

#     else:
#         raise ValueError



