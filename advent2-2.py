f= open('test.txt', 'r')

hor = 0
vert = 0
vert1 = 0

for line in f:
    x= line.split()
    if x[0] == 'forward':
        hor += int(x[1])
        vert1 += int(x[1]) * vert
    if x[0] == 'up':
        vert -= int(x[1])
    if x[0] == 'down':
        vert += int(x[1])

print(f'hor = {hor} aim = {vert} vert = {vert1} total = {hor*vert1}')
