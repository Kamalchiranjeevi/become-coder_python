while 1:
    n,a,b=map(int,input().split())
    s=0
    l=0
    while n!=0:
        r=n%10
        n=n//10
        s=s*10+r
    while s!=0:
        r=s%10
        s=s//10
        if(r%a==0):
           r=b
           b+=1
           if(b>9):
               b=1
        l=l*10+r
    print(l)


