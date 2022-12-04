count = 0
X = [l.strip() for l in open('./Day 4/input.txt')]
for x in X:
    a,b = x.split(',')
    print('A: ' + a + ' B: ' + b)
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)

    if a1>=b1 and a2<=b2:
        count+=1
    elif b1>=a1 and b2<=a2:
        count+=1
print(count)

#-------------Part 2
count1 = 0
X = [l.strip() for l in open('./Day 4/input.txt')]
for x in X:
    a,b = x.split(',')
    print('A: ' + a + ' B: ' + b)
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)

    if a1>=b1 and a1<=b2:
        count1+=1
    elif a2>=b1 and a2<=b2:
        count1+=1
    elif b1>=a1 and b1<=a2:
        count1+=1
    elif b2>=a1 and b2<=a2:
        count1+=1
print(count1)