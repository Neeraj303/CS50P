# import random

# class Hat: # class method
#     def __init__(self):
#         self.houses = ["Jamuna", "Ravi"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))
#     ...



# hat = Hat()
# hat.sort("Neeraj")


import random

class Hat():

    houses = ["Jamuna", "Ravi", "Satluj", "Jhelum"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Neeraj")