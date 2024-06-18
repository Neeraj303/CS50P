import sys
'''
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# IndexError: list out of range
'''

'''
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
'''

'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

for arg in sys.argv[1:]:
    print("Hello, My name is", arg)
'''


