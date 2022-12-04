X = [l.strip() for l in open('./Day 2/input.txt')]
score = 0
for x in X:
    op,me = x.split()
    #print(me,op)
    score += {'X': 1,'Y': 2, 'Z': 3}[me]
    score += {('A', 'X'): 3,('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0,('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6,('C', 'Y'): 0, ('C', 'Z'): 3,
        }[(op, me)]
 
print('Part 1: ' + str(score))

score = 0
#--------------------Part 2
for x in X:
    op,me = x.split()
    #print(me,op)
    score += {'X': 0,'Y': 3, 'Z': 6}[me]
    score += {('A', 'X'): 3,('A', 'Y'): 1, ('A', 'Z'): 2,
        ('B', 'X'): 1,('B', 'Y'): 2, ('B', 'Z'): 3,
        ('C', 'X'): 2,('C', 'Y'): 3, ('C', 'Z'): 1,
        }[(op, me)]
 
print('Part 2: ' + str(score))