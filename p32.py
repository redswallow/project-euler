def check(i,j,k):
    i=str(i);j=str(j);k=str(k)
    for num in range(1,10):
        if (str(num) in i)+(str(num) in j)+(str(num) in k)!=1:
            return False
    return True

ans=[]
for i in range(10,100):
    for j in range(100,1000):
        if len(str(i*j))==4 and check(i,j,i*j): ans.append(i*j)
for i in range(2,10):
    for j in range(1000,10000):
        if len(str(i*j))==4 and check(i,j,i*j): ans.append(i*j)
ans=list(set(ans))
print ans,sum(ans)
