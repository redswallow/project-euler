def check(i,j):
    i=str(i);j=str(j)
    for num in range(1,10):
        if (str(num)in i)+(str(num)in j)!=1:
            return False
    return True

ans=[]
for i in range(9000,10000):
    if (check(i,i*2)):
        ans.append(i*100000+i*2)
print ans
