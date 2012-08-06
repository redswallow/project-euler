def divisors(n):
    l=[]
    for i in range(1,n):
        if n%i==0:l.append(i)
    return l

def abundant(n):
    return sum(divisors(n))>n

ans=[]
'''
abundant_num=filter(abundant,range(1,28123))
#print abundant_num
file=open("p23.data","w")
for l in abundant_num:
    file.write(str(l)+'\n')
'''

file=open("p23.data","r")
abundant_num=[int(line.replace('\n','')) for line in file.readlines()]
#print abundant_num

l=[]
for i in range(1,28123*2):
    l.append(i)
for i in range(len(abundant_num)):
    for j in range(len(abundant_num)):
        l[abundant_num[i]+abundant_num[j]]=0
for i in range(1,28123):
    if l[i]!=0:
        ans.append(i)
print ans,sum(ans)
