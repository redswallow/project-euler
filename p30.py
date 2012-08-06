def fifth_power(n):
    digits=[];m=n
    while m>0:
        digits.append(m%10);m=m/10
    digits=[digit**5 for digit in digits]
    return sum(digits)==n

ans=filter(fifth_power,range(2,1000000))
print sum(ans)
