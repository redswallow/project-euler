import timeit,math 
class time(object): 
    def __init__(self, orig_func): 
        self.f = orig_func 
    
    def __call__(self, *args, **kwargs): 
        start = timeit.default_timer() 
        r = self.f(*args, **kwargs) 
        end = timeit.default_timer() 
        print "The running time for %s:%2f"%(self.f.__name__, end-start) 
        return r 
