# with open('students.csv') as file:
#     for line in file:
#         name, dept = line.rstrip().split(',') # split gives an list
#         print(f'{name} belongs to {dept}')

# What if you wanted to sort
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         students.append(f'{name} is in {house}')

# for student in sorted(students):
#     print(student)

######  different way to sort same as above code  #################
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         # student = {}
#         # student['name'] = name
#         # student['house'] = house
#         student = {'name': name, 'house': house} # sue to cut the 3 line above
#         students.append(student)

# def get_name(student):
#     return student['name']


# for student in sorted(students, key=get_name): # key is the named parameter key
#     print(f"{student['name']} is in {student['house']}")

######## similar to above one we use lambda  #######################
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house}
#         students.append(student)

# for student in sorted(students, key=lambda student: student['name']): # lambda is anynomous function
#     print(f"{student['name']} is in {student['house']}")



####### Now we input names and city they currently are in ###################
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(',')
#         student = {'name': name, 'city': city}
#         students.append(student)

# for student in sorted(students, key=lambda student: student['name']): # lambda is anynomous function
#     print(f"{student['name']} is in {student['city']}")

############### Import csv to work with the code #######################
# import csv # its an module

# students = []

# with open("students.csv") as file:
#     #reader = csv.reader(file) # loading each line of text as list of columns
#     reader = csv.DictReader(file) # iterate over top to bottom loading each line of text as dictionary of column # even if you cahnge the header this code would work like Jodhpur,Arjun
#     for row in reader:
#         #students.append({'name': row[0], 'city': row[1]})
#         students.append({'name': row['name'], 'city': row['city']})

# for student in sorted(students, key=lambda student: student['name']): # lambda is anynomous function
#     print(f"{student['name']} is in {student['city']}")


################                         ############################
# import csv

# name = input('What is your name? ')   
# city = input('Which city do you belong to? ')

# with open('students.csv', 'a', newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, city])

#####################SAME CODE AS ABOVE ###########################
# import csv

# name = input('What is your name? ')
# city = input('Which city do you belong to? ') 

# with open('students.csv', 'a', newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=['name', 'city'])
#     writer.writerow({'name': name, 'city': city})

import csv 

with open('file_doesnot_exist.csv') as file:
    writer = csv.writer(file)