import math
a=3;b=2;ans=0
for i in range(2,1001):
    a,b=2*b+a,a+b
    if int(math.log10(a))>int(math.log10(b)):
        #print a,b
        ans+=1
print ans
