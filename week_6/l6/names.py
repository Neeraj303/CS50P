# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print(f'hello, {name}')

### 2 #####

# name = input('what is your name? ')

# with open("names.txt", "a") as file:
#     file.write(f'{name}\n')
#file = open("names.txt", "a") # open returns file handle, w-write, a-append\
#file.close()

#### 3 #####
# with open("names.txt", "r") as file:
#     lines = file.readlines() # return this as an list

# for line in lines:
#     print('hello,', line.rstrip()) #rstirp used to remove the end of each line '/n' or white spaces whereas strip() removes from both the front and the end
    
# same code as above
# with open("names.txt", 'r') as file:
#     for line in file:
#         print('hello,', line.rstrip())


# how to sort the names and then print the names
# names = []

# with open('./names.txt') as file: # in general open always read file till the time you assign it to write the file
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print('hello,' , name )

# same as above code
names = []

with open('./names.txt') as file: # in general open always read file till the time you assign it to write the file
    for line in sorted(file, reverse=True):
        print(f'hello, {line.rstrip()}')

