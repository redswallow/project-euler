#http://www.mathblog.dk/project-euler-104-fibonacci-pandigital/
def check(n):
    s=str(n)
    for num in range(1,10):
        if not (str(num) in s): return False
    return True

def top_digits(n):
# t = n * log10(phi)          + log10(1/sqrt(5))
  t = n * 0.20898764024997873 + (-0.3494850021680094)
  t = int((pow(10, t - int(t) + 8)))
  return t
 
fn, f0, f1 = 2, 1, 1
while not check(f1) or not check(top_digits(fn)):
 f0, f1 = f1, (f1+f0)%10**9
 fn += 1
print "Answer to PE104 = ", fn

