file = open('./Day 10/input.txt').read()
lines = [x for x in file.split('\n')]

image = [['?' for _ in range(40)] for _ in range(6)]
p1 = 0
c = 0
x = 1

def increase_cycle(t, x):
    global p1
    global image
    t1 = t-1
    image[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
    if t in [20, 60, 100, 140, 180, 220]:
        p1 += x*t

for line in lines:
    words = line.split()
    if words[0] == 'noop':
        c += 1
        increase_cycle(c,x)
    elif words[0] == 'addx':
        c += 1
        increase_cycle(c,x)
        c += 1
        increase_cycle(c,x)
        x += int(words[1])
print(p1)
for r in range(6):
    print(''.join(image[r]))