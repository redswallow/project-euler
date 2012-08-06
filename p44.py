def is_pentagonal(x):
    n=float((24*x+1)**0.5+1)/6
    return n==int(n)

def pentagonal(x):
    return x*(3*x-1)/2

p=set(pentagonal(n) for n in range(2,2400))
for pj in p:
    for pk in p:
        if pj-pk in p and pj+pk in p:
            print pj-pk
