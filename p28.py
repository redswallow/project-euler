def spiral_diag(n):
    #init
    ans=1;increment=0;m=1
    while increment+2<n:
        increment+=2
        for i in range(4):
            m+=increment;ans+=m
    print ans

spiral_diag(1001)
