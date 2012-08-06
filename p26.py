def recurring_cycle(d):
    n=1 #numerator
    pool=[]
    level=0
    while n!=0:
        level+=1
        n=n*10
        if n in pool:
            return level-(pool.index(n)+1)
        else: pool.append(n)
        q=n/d;r=n%d;n=r
    return 0

result=map(recurring_cycle,range(1,1000))
print 'max=%d index=%d' %(max(result),result.index(max(result))+1)
