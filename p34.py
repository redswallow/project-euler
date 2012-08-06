def fact(n):
    return reduce(lambda x,y:x*y,range(1,n+1)) 
def curious_num(n):
    digits=[];m=n
    while m>0:
        digits.append(m%10);m=m/10
    digits=[fact_list[digit] for digit in digits]
    return sum(digits)==n

fact_list=[1]+map(fact,range(1,10))
ans=filter(curious_num,range(3,2177280))
print ans
print sum(ans)
