import math 
lines=[];ans=[]
for line in open("p99.in","r").readlines():
    a,b=[int(num) for num in line.replace('\n','').split(',')]
    lines.append([a,b])
    ans.append(math.log10(a)*b)

print max(ans),ans.index(max(ans))
print lines[ans.index(max(ans))]
