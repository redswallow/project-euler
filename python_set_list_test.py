from runningtime import time
def pentagonal(x):
    return x*(3*x-1)/2

@time
def list_test():
    p=[pentagonal(n) for n in xrange(2,2400)]
    for i in xrange(10000):
        if i in p: pass

@time
def set_test():
    p=set(pentagonal(n) for n in xrange(2,2400))
    for i in xrange(10000): 
        if i in p: pass

list_test()
set_test()
