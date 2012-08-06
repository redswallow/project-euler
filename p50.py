def prime(n):
    return [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]

def isprime(n):
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

prime_list=prime(4000)[3:]
s=0;k=0
ans=[]
for prime in prime_list:
    s+=prime;k+=1
    if s<1000000 and isprime(s):
        ans.append([s,k])
print ans,max(ans[0])
