def find(level,ans,r):
    if level==0:
        print ans,int(ans)**2;raw_input();return
    for m in xrange(0,100):
        n=m**2+r;
        if n%10==level:
            print n,level,str(m)+ans,int(str(m)+ans)**2
            new_level=level-1;new_ans=str(m)+ans
            find(new_level,new_ans,n/100)
find(9,"0",10)
