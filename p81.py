data=[];ans=[]
for line in open("p81.in","r").readlines():
    data.append([int(num) for num in line.replace("\n","").split(",")])
    ans.append([int(num) for num in line.replace("\n","").split(",")])

w=len(data);l=w*2-1

for level in range(l):
    if level<w:
        i=level;j=0
    else:
        i=w-1;j=level-w+1
    while i>=0 and i<w and j>=0 and j<w:
        if i-1>=0:ans[i][j]=data[i][j]+ans[i-1][j]
        if j-1>=0:ans[i][j]=data[i][j]+ans[i][j-1]
        if i-1>=0 and j-1>=0:
            ans[i][j]=min(data[i][j]+ans[i-1][j],data[i][j]+ans[i][j-1])
        i-=1;j+=1;

for line in ans:
    print line
