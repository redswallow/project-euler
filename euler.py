import math
#Euclidean algorithm
def gcd(a,b):
    if a<b:a,b=b,a
    while b:
        a,b=b,a%b
    return a

#Extended Euclidean algorithm
def extended_gcd(a,b):
    x=0;lastx=1;y=1;lasty=0
    while b:
        quotient=a/b
        a,b=b,a%b
        x,lastx=lastx-quotient*x,x
        y,lasty=lasty-quotient*y,y
    return lastx,lasty

#Binary GCD: Stein's algorithm
def gcd_stein(a,b):
    if a==0:return b
    if b==0:return a
    if a&1==0 and b&1==0:
        return gcd_stein(a>>1,b>>1)<<1
    elif a&1==0:
        return gcd_stein(a>>1,b)
    elif b&1==0:
        return gcd_stein(a,b>>1)
    else:
        return gcd_stein(abs(a-b)>>1,min(a,b))

#least common multiple
def lcd(a,b):
    return a*b/gcd_stein(a,b)

#Check whether n is a prime
def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

#Find a prime factor of n using a variety of methods
def factor(n):
    if (isprime(n)): return n
    for fact in [2,3,5,7,11,13,17,19,23,29]:
        if n%fact == 0: return fact
    return factorPR(n)  # Needs work - no guarantee that a prime factor will be returned

#factors(n) - Return a sorted list of the prime factors of n
def factors(n):
    if (isprime(n)):
        return [n]
    fact = factor(n)
    if (fact == 1): return [1]
    facts = factors(n/fact) + factors(fact)
    facts.sort()
    return facts

#Find a factor of n using the Pollard Rho method
def factorPR(n):
    for slow in [2,3,4,6]:
        numsteps=2*math.floor(math.sqrt(math.sqrt(n))); fast=slow; i=1
        while i<numsteps:
            slow = (slow*slow + 1) % n
            i = i + 1
            fast = (fast*fast + 1) % n
            fast = (fast*fast + 1) % n
            g = gcd(abs(fast-slow),n)
            if (g != 1):
                if (g == n):
                    break
                else:
                    return g
    return 1

if __name__ == '__main__':
    #print gcd(123456,987654)
    #print extended_gcd(12,7),lcd(12,18)
    print factors(37*37)
