def isprime(n):
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

primes=[]
for i in xrange(1001, 10000, 2):
    if isprime(i):
        primes.append(i)

for p in primes:
    for q in primes:
        if p<q and set(str(p)) == set(str(q)):
            r=p*2-q
            if r in primes and set(str(p)) == set(str(r)):
                print p, q, r
