from math import sqrt

def primeList(n):
    sieve = [True for j in range(2, n+1)]  #creates sieve with all True
    for j in range(2, int(sqrt(n))+1):  #only have to test up to sqrt of n
        i = j-2   #shift index back by 2, to look in sieve list
        if sieve[i]:
            for k in range(j*j, n+1, j):  #start at j squared and go up by multiples of j to set to False
                sieve[k-2] = False
    ret = [j for j in range(2, n+1) if sieve[j-2]]  #ret set to list of primes
    return ret

lst = primeList(10000)

def truncLtoR(num):
    numString = str(num)
    numList = []
    for i in range(len(numString)):
        numList.append(int(numString[i:]))
    return numList

def truncRtoL(num):
    numString = str(num)
    numList = [int(numString)]
    for i in range(1,len(numString)):
        numList.append(int(numString[:-i]))
    return numList

listLtoR = []
listRtoL = []

for x in lst:
    test1 = truncLtoR(x)
    if all(number in lst for number in test1):
        listLtoR.append(x)

for x in lst:
    test1 = truncRtoL(x)
    if all(number in lst for number in test1):
        listRtoL.append(x)

def intersect(a,b):
    return list(set(a) & set(b))

result = intersect(listLtoR, listRtoL)
solution = [x for x in result if x > 10]
print solution
##this only got us the first 10 primes
## let's find the 11th result

def isPrime(n):
    for x in range(2,int(sqrt(n)+1)):
        if n % x == 0:
            return False
    else:
        return True

def trunc(x):
    numString = str(x)
    numListL = []
    numListR = []
    numListBoth = []
    for i in range(len(numString)):
        numListL.append(int(numString[i:]))
    for i in range(1,len(numString)):
        numListR.append(int(numString[:-i]))
    numListBoth = numListL + numListR
    if all(isPrime(x) for x in numListBoth):
        return True
    else:
        return False

listLtoR4 = [x for x in listLtoR if x >= 1000]
listRtoL4 = [x for x in listRtoL if x >= 1000]

list5L = []
list5R = []

for x in listLtoR4:
    for y in listRtoL:
        numString = str(y) + str(x)
        number = int(numString)
        if isPrime(number):
            list5L.append(number)

for x in listRtoL4:
    for y in listLtoR:
        numString = str(x) + str(y)
        number = int(numString)
        if isPrime(number):
            list5R.append(number)

list5 = list5L + list5R

for i in list5:
    if trunc(i):
        if not i in solution:
            solution.append(i)

summation = 0
for i in solution:
    summation += i

print summation

