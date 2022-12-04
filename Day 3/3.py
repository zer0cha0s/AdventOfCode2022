total = 0
for line in open('./Day 3/input.txt'):
    x = line.strip()
    a,b = x[:len(x)//2], x[len(x)//2:]
    print (a,b)
    for c in a:
        if c in b:
            print(x,a,b,c)
            if 'a'<=c<='z':
                total += ord(c)-ord('a') + 1
            else:
                total += ord(c)-ord('A') + 1 + 26
            break
print('Total 1 : ' + str(total))


#---------Part 2
total2 = 0
data = [i.strip('\n') for i in open('./Day 3/input.txt')]
new_data = [' ,'.join(data[i:i+3]) for i in range(0, len(data), 3)]
for i in new_data:
    #print(i)
    a,b,c = i.split(',')
    #print('A: '+ a + ' B: '+ b + ' C: ' + c)
    for d in a:
        if d in b and d in c:
            #print(d,a,b,c)
            if 'a'<=d<='z':
                total2 += ord(d)-ord('a') + 1
            else:
                total2 += ord(d)-ord('A') + 1 + 26
            break
print('Total 2 : ' + str(total2))
