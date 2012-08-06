def d(n):
    s=0
    for i in range(1,n):
        if n%i==0:s+=i
    return s

def amicable_pair(n):
    m=d(n)
    if n==d(m) and n!=m:
        return True
    else:return False

l=10000
result=filter(amicable_pair,range(1,l))
print result
print sum(result)
