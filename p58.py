def isprime(n):
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

#init
num=49;inc=6;total=13;prime=8
while (prime*10>=total):
    inc+=2
    for i in range(4):
        num+=inc
        if isprime(num):prime+=1
        total+=1
        print [prime,total]
        if (prime*10<total):
            print inc+1
            break
