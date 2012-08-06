data=open("p22.in","r").read().replace('\"', '').split(',')
data.sort()
values=[]
sum=0
for name in data:
    value=0
    for char in name:
        value+=(ord(char)-64)
    values.append(value)
    sum+=(data.index(name)+1)*value
print sum
