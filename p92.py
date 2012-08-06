list=[]
for i in xrange(10000000):
    digits=0
    for ch in str(i):digits+=(int(ch)**2)
    list.append(digits)
loop=set([89]);flag=False;ans=1
while not flag:
    flag=True
    for i in range(len(list)):
        if list[i] in loop and i not in loop:
            flag=False;loop.add(i);ans+=1
print ans

