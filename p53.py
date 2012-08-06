def c(n):
    s=1
    for r in xrange(1,n):
        s=s*(n-r+1)/r
        if s>1000000:
            ans.append(s)

ans=[]
for i in xrange(1,101):
    c(i)
print len(ans)
