def triangle(n):
  return n*(n+1)/2
def pentagonal(n):
    return n*(3*n-1)/2
def hexagonal(n):
    return n*(2*n-1)

t=map(triangle,range(1,100000))
p=map(pentagonal,range(1,100000))
h=map(hexagonal,range(1,100000))
ans=[]
for i in t:
    if i in p and i in h:ans.append(i)
print ans
