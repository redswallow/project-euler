def triangle(n):
    return n*(n+1)/2

data=open("p42.in","r").read().replace("\"","").split(",")
triangle_num=map(triangle,range(1,200))
ans=0

for word in data:
    word_value=0
    for letter in word:
        word_value+=ord(letter)-ord('A')+1
    if word_value in triangle_num:
        ans+=1
print ans
