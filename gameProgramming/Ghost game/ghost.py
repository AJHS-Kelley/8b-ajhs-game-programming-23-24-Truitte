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
    door = input('1, 2 or 3?\n')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False
    else:
        print('No ghost!')
        score = score + 1
print('Run away!')
print('Game over! you scored',score)

    
    
