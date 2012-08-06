def prime(n):
    return [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]

def isprime(n):
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def check(n):
    for i in range(1000):
        if i*i*2>n:return False
        elif isprime(n-i*i*2):
            return True

prime_list=prime(4000)
for i in range(1,1000000):
    n=i*2+1
    if not isprime(n) and not check(n):
        print n
        break
