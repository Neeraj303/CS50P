''' Using while loop 
i = 0

while i < 3:
    print("meow")
    i+=1 # does the same job as i = i + 1

'''

'''
 Using for loop

 for _ in range(3): # _ is a placeholder for the value that is not used
    print("meow")
 
 '''

# Dictionary
'''
students = {
    "Hermoine": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor"
}

for student in students: # this would only print the key values in the dictonary
    print(student)   

'''
def main():
    print_square(3)

def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()

main()
