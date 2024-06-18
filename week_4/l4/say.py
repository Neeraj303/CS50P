# About packages
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.meow("hello, " +  sys.argv[1])

# we import the code in other file named "saying.py"

import sys
from saying import hello

if len(sys.argv) == 2:
    hello(sys.argv[1]) 