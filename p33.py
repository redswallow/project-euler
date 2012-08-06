ans=[]
for b in range(1,10):
    for a in range(1,10):
        for c in range(1,10):
            if a<c  and (a*10+b)*c==(b*10+c)*a:
                ans.append([a*10+b,b*10+c])
print ans
