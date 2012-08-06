ans=[]
for a in range(2,100):
    for b in range(1,100):
        digital_sum=0
        for ch in list(str(a**b)):
            digital_sum+=int(ch)
        ans.append(digital_sum)
print max(ans)
