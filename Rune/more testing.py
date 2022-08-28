import kociemba

#kleuren
wit = 'U'
rood = 'R'
groen = 'F'
geel = 'D'
oranje = 'L'
blauw = 'B'



scramble = ('LDDLUBLDRUUBFRBFUUDRBLFRFRLRUDFDLULLBBBFLFFDDRBURBUFDR')
#UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
a = kociemba.solve(scramble)

up = a.split()
lengte = len(up)


for b in up:
    #Up
    if b == 'U':
        print('draai up 1 keer')

    elif b == 'U2':
        print('draai up 2 keer')

    elif b == "U'":
        print('draai up andere kant')

    #Right
    elif b == 'R':
        print('draai Right 1 keer')

    elif b == 'R2':
        print('draai Right 2 keer')

    elif b == "R'":
        print('draai Right andere kant')

    # Front
    elif b == 'F':
        print('draai Front 1 keer')

    elif b == 'F2':
        print('draai Front 2 keer')

    elif b == "F'":
        print('draai Front andere kant')

    # Down
    elif b == 'D':
        print('draai Down 1 keer')

    elif b == 'D2':
        print('draai Down 2 keer')

    elif b == "D'":
        print('draai Down andere kant')

    # Left
    elif b == 'L':
        print('draai Left 1 keer')

    elif b == 'L2':
        print('draai Left 2 keer')

    elif b == "L'":
        print('draai Left andere kant')

    # Back
    elif b == 'B':
        print('draai Back 1 keer')

    elif b == 'B2':
        print('draai Back 2 keer')

    elif b == "B'":
        print('draai Back andere kant')

print(a)
print(lengte)
