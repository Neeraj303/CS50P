''' CS50P Lecture 0'''
''' Practising with Str'''

name = input("What is your name ? ").strip().title()

first_name, last_name = name.split(" ")

# remove the space between the name
#name = name.strip() # this is an method
#name = name.capitalize() # this is an method, only the first word
#name = name.title() # this is an method, to all words

#print("Hello,",name)
#print("Hello,",name, sep="??", end="!!")
# position parameter and name parameters (optional to add)
# sep is the separator
# end is the end of the string

print(f"Hello, {first_name}")
