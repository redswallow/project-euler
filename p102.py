#vendor product
def vendor_product(xa,xb,ya,yb,xp,yp):
    return (xp-int(xa))*(int(yb)-int(ya))-(yp-int(ya))*(int(xb)-int(xa))>0

#input
lines=open("p102.in","r").readlines();
data=[line.strip().replace(',',' ').split() for line in lines]
print data
#init
(xp,yp)=0,0
ans=0

for num in data:
    for n in num: n=int(n)
    bool1=vendor_product(num[0],num[1],num[2],num[3],xp,yp)
    bool2=vendor_product(num[2],num[3],num[4],num[5],xp,yp)
    bool3=vendor_product(num[4],num[5],num[0],num[1],xp,yp)
    if bool1==True and bool2==True and bool3==True:ans+=1
    if bool1==False and bool2==False and bool3==False:ans+=1

print ans
