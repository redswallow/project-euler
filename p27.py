def prime(n):
    return [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]

def expression(a,b):
    n=2
    while (n*n+a*n+b in prime_list_large): n+=1
    return [n,a*b]

prime_list=prime(1000)
prime_list_large=prime(10000)
ans=[0,0]
for b in prime_list:
    for a in range(-999,1000):
        if a+b+1 in prime_list:
            temp=expression(a,b)
            if temp[0]>ans[0]:ans=temp
print ans

