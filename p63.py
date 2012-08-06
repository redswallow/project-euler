import math
ans=0
for a in range(1,10):
    loga=math.log10(a)
    #log10(9)*n < n-1 => n=22
    for b in range(1,22):
        if loga*b>=b-1 and loga*b<b:
            ans+=1
print ans
