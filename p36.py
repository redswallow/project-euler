def d2b(n,k):
    binary=[];m=n
    while m>0:
        binary.append(m%k);m=m/k
    return binary

def palindromic(binary):
    for i in range(len(binary)):
        if binary[i]!=binary[-i-1]: return False
    return True

def palindromic_num(n):
    dec=d2b(n,10)
    if palindromic(dec):
        binary=d2b(n,2)
        return palindromic(binary)
    else:
        return False

ans=filter(palindromic_num,range(1,1000000))
print ans
print sum(ans)
