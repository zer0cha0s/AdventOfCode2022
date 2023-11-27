#Input file
data = open('./Day 6/input.txt').read()
#print(data)

part1= []
part2= []
#Part 1
for x in range(4, len(data)):
    if len(set(data[x-4:x])) == 4:
        part1.append(x)
print('Part 1 : ' + str(part1[0]))

#Part 2
for x in range(14, len(data)):
    if len(set(data[x-14:x])) == 14:
        part2.append(x)
print('Part 2 : ' + str(part2[0]))
