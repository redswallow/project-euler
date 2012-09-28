import euler
def func(n):
    factors=euler.factors(n)
    set_factors=set(factors)
    result=1
    for factor in set_factors:
        #print factor,factors.count(factor)
        result=result*(factors.count(factor)+1)
    return result

n=4
while (func(n*n)+1)/2<=1000:
    n+=1
    print n
