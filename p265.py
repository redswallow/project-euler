n=5;total=2**n
aim=set([])
ans=[]
for i in xrange(total):
    aim.add(str(bin(i))[2:])

for i in xrange(2**(total-n-2)):
    m=str(bin(i))[2:]
    binary="0"*n+"1"+"0"*(total-n-2-len(m))\
            +m+"1"+"0"*n
    digits=set([])
    for k in xrange(total):
        digits.add(binary[k:k+n])
    if len(digits)==len(aim):
        dec=0
        for i in xrange(total):
            if binary[i]==str(1):
                dec+=2**(total-i-1)
        ans.append(dec)
print sum(ans)
        
