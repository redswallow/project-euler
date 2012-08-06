import itertools
def gen_data_list(n):
    data_list=[]
    for i in range(1,1000):
        if isdivide(i,n):data_list.append(i)
    return data_list

def isdivide(n,x):
    return n % x == 0

def check(n):
    digits=[];
    for i in range(0,10):
        digits.append(0)
    for i in n:
        digits[int(i)]+=1
        if digits[int(i)]>1:return 10
    for i in range(0,10):
        if digits[i]==0:
            return i

def search(level,string,match):
    if level==-1: 
        i=check(string)
        if i!=10: 
            ans.append(int(str(i)+string))
        return
    for i in data[level]:
        if level==6:
            new_string=str(i);
            while len(new_string)<3:new_string="0"+new_string
            search(level-1,new_string,i/10)
        elif i%100==match:
            new_match=i/10
            new_string=str(i/100)+string
            while len(new_string)<3:new_string="0"+new_string
            search(level-1,new_string,new_match)

data=map(gen_data_list,[2,3,5,7,11,13,17])
ans=[]
search(6,"","")
print ans,sum(ans)
