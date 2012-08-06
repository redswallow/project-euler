import math
def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def gcd(a,b):
    """gcd(a,b) returns the greatest common divisor of the integers a and b."""
    if a == 0:
	return b
    return abs(gcd(b % a, a))

def factor(n):
    """factor(n) - Find a prime factor of n using a variety of methods."""
    if (isprime(n)): return n
    for fact in prime_list:
        if n%fact == 0: return fact
    return factorPR(n)  # Needs work - no guarantee that a prime factor will be returned

def factors(n):
    """factors(n) - Return a sorted list of the prime factors of n."""
    if (isprime(n)):
        return [n]
    fact = factor(n)
    if (fact == 1): return [1]
    facts = factors(n/fact) + factors(fact)
    facts.sort()
    return facts

def factorPR(n):
    """factorPR(n) - Find a factor of n using the Pollard Rho method.
    Note: This method will occasionally fail."""
    for slow in [2,3,4,6]:
        numsteps=2*math.floor(math.sqrt(math.sqrt(n))); fast=slow; i=1
        while i<numsteps:
            slow = (slow*slow + 1) % n
            i = i + 1
            fast = (fast*fast + 1) % n
            fast = (fast*fast + 1) % n
            g = gcd(fast-slow,n)
            if (g != 1):
                if (g == n):
                    break
                else:
                    return g
    return 1

def n_div_euler(n):
    euler=n;flag=False
    for i in set(factors(n)):
        euler=euler*(1-float(1)/i);flag=True
    if not flag:euler-=1
    #print n,euler,float(n)/euler
    return float(n)/euler

def prime(n):
    return [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]

prime_list=set(prime(1000))
total=1000000
max=0,0
for i in xrange(2,total):
    n=n_div_euler(i)
    if n>max[0]:max=n,i
print max
