X = [l.strip() for l in open('./Day 1/input.txt')]
I = []
for elfs in ('\n'.join(X)).split('\n\n'):
    i = 0
    for x in elfs.split('\n'):
        i += int(x)
    I.append(i)
print(sorted(I))
#--------------Part 2
last_3_items = slice(-3, None)
top3 = list(sorted(I))[last_3_items]
print(top3)
q = 0
for i in top3:
    q += i
print(q)