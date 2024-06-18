class Student(): # new datatype
    # classes comes with certain methods or functions inside of them
    def __init__(self, name, house): # instance method, want to intialize content of an oject in a class or fucntion inside of an class
        self.name = name
        self.house = house

    #self reference to current object or access to object
    def __str__(self):  #special method which allows to show your result as str
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    #Getter
    @property
    def house(self):
        return self._house
    
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Jamuna", "Satluj", "Jhelum", "Ravi"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    #student.house = "Chenab" # due to this we can change the value of house
    # Properties, its an attribute which have more defense mechanism
    # decorators are functions which modify the behaviour of other functions
    print(student)



def get_student():
    #student = Student() # creating object from Student class, or instantiation/instances of a class
    #student.name = input("What is your name? ") # defining "name" attributes or instance variables
    #student.house = input("What is your house? ") # name and house are variables called inside of an object whose type is student
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # this is an constructor call, it creates student object
    return student


if __name__ == "__main__": # double underscore (__) is called dunder.
    main()