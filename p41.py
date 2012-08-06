import itertools
def isprime(n):
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

ans=[]
digits=list(xrange(1,8))
nums=list(itertools.permutations(digits))
for num in nums:
    n=0
    for digit in num:
        n=n*10+digit
    if isprime(n): ans.append(n)
print max(ans)
