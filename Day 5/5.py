#         [C] [B] [H]                
# [W]     [D] [J] [Q] [B]            
# [P] [F] [Z] [F] [B] [L]            
# [G] [Z] [N] [P] [J] [S] [V]        
# [Z] [C] [H] [Z] [G] [T] [Z]     [C]
# [V] [B] [M] [M] [C] [Q] [C] [G] [H]
# [S] [V] [L] [D] [F] [F] [G] [L] [F]
# [B] [J] [V] [L] [V] [G] [L] [N] [J]
#  1   2   3   4   5   6   7   8   9 

#Input file
X = [l.strip() for l in open('./Day 5/input.txt')]

#Stacks from input file 
stacks=[
[''],
['W','P','G','Z','V','S','B'],
['F','Z','C','B','V','J'],
['C','D','Z','N','H','M','L','V'],
['B','J','F','P','Z','M','D','L'],
['H','Q','B','J','G','C','F','V'],
['B','L','S','T','Q','F','G'],
['V','Z','C','G','L'],
['G','L','N'],
['C','H','F','J'],
]

#split input to get quantity to move, the source location and destination.
for x in X:
    commands = x.split()
    qty = int(commands[1])
    source = int(commands[3])
    dest = int(commands[5])
    move = stacks[source][:qty]
    #move.reverse()  #For part 1
    stacks[source] = stacks[source][qty:]
    stacks[dest] = move + stacks[dest]
    #print(qty,source_,dest_)

print(''.join([s[0] for s in stacks if len(s)>0]))
print(stacks)