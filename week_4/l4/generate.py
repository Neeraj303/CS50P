'''
import random # importing the random module
import random

number = random.randint(1, 10) # gives random betqeen the number, both 1 and 10 are included
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)
'''

import statistics

print(statistics.mean([100, 90]))
