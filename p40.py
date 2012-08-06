ans=1
total=7;level=1;lens=0;n=0
for i in range(1,1000000):
    n+=1;
    lens+=len(str(n))
    if lens>=level:
        print n,str(n)[level-lens-1],level,lens
        ans*=int(str(n)[level-lens-1])
        level*=10
        total-=1
    if total==0:break
print ans
