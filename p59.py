data=[int(str) for str in open("p59.in","r").read().strip().split(',')]
key1=data[::3];key2=data[1::3];key3=data[2::3]

plaintext=""
for i in xrange(len(data)):
    if i%3==0:
        plaintext+=chr(103^data[i])
    elif i%3==1:
        plaintext+=chr(111^data[i])
    else:
        plaintext+=chr(100^data[i])

print plaintext
ans=[ord(ch) for ch in plaintext]
print sum(ans)
