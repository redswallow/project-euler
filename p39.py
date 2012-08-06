ans=[]
for i in range(1001): ans.append(0)
for i in range(1,334):
    for j in range(i,500):
        for k in range(j,999):
            if (i+j+k<=1000)and(i*i+j*j==k*k):
                ans[i+j+k]+=1

print ans,max(ans),ans.index(max(ans))
