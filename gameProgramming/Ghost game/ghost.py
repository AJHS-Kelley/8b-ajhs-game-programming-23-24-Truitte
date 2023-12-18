# Ghost game Coded by Truitte Moreland
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('Three doors ahead...')
    print('A ghost is behind one.')
    print('Which door do you open?')
    door =