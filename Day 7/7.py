from collections import defaultdict
#Input file
file = open('./Day 7/input.txt').read()
lines = [x for x in file.split('\n')]

path = []
SIZE = defaultdict(int)
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls' or words[0] == 'dir':
        continue
    else:
        size = int(words[0])
        for i in range(1, len(path)+1):
            SIZE['/'.join(path[:i])] += size
            #print(path,words)

# 70000000-30000000(total space - unused space)
max_used = 40000000 
used_space = SIZE['/']
space_needed = used_space - max_used

part1 = 0
part2 = 30000000
for key,value in SIZE.items():
    if value <= 100000:
        part1 += value
    if value>=space_needed:
        part2 = min(part2, value)
print('Part 1: ' + str(part1))
print('Part 2: ' + str(part2))