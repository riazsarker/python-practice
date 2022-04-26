
import random


def swg(comp,mine):
    if (comp==mine):
        return True
    if (comp=='s' and mine == 'g'):
        return True
    elif (comp=='w' and mine == 's'):
        return True
    elif (comp=='g' and mine == 'w'):
        return True
    else:
        return False


choice = ('s','w','g')
comp = random.randint(0,2)
comp =choice[comp]
mine = input('Choose either s,w or g')

win=swg(comp,mine)
print(f'You choose {mine} and the computer choose {comp}')

if win is None:
    print('Match Drawn')

if win:
    print("win")

else:
    print('you lose')
    
    