#input
lines = open("p67.in","r").readlines()
data=[line.split() for line in lines]
data.reverse()
length=len(data)

for i in range(1,len(data)):
    for j in range(len(data[i])): 
        data[i][j]=int(data[i][j])+int(max(data[i-1][j],data[i-1][j+1]))

print data[-1]
