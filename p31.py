#init
total=200;ans=[]
for i in range(total+1):ans.append(0)
ans[0]=1
currency=[200,100,50,20,10,5,2,1]

for i in currency:
    for j in range(total-i+1):
        ans[i+j]+=ans[j]

print ans
