e=[2]
for i in range(33):
    e.append(1);e.append(2*(i+1));e.append(1)

total=10
a=1;b=e[total-1]
for i in range(total-2,-1,-1):
    a,b=b,e[i]*b+a
print b,a
digits=[int(ch) for ch in str(b)]
print digits,sum(digits)
