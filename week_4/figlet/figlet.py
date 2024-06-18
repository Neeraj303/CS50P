import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts() #gives the list of available fonts

if len(sys.argv) == 1:
    n = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print(f'Output: {figlet.renderText(n)}')
elif len(sys.argv) == 3 and (sys.argv[1] in ['-f', '--font']) and (sys.argv[2] in fonts):
    n = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(f'Output: \n{figlet.renderText(n)}')
else:
    sys.exit("Invalid usage")


