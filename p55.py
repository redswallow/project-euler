def palindromic(n):
    for i in range(len(n)):
        if n[i]!=n[-i-1]: return False
    return True

def find_lychrel(i):
    for t in xrange(49):
        sum=i+int(str(i)[::-1]);i=sum
        if palindromic(str(sum)):return True
    return False

ans=[]
for i in xrange(1,10001):
    if not find_lychrel(i):ans.append(i)
print ans,len(ans)
