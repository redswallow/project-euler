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
    for fact in [2,3,5,7,11,13,17,19,23,29]:
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


total=4;n=2*3*5*7;k=0
while k!=total:
    n+=1
    if len(set(factors(n)))==total:k+=1
    else:k=0
print n-total+1
