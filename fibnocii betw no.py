while 1:
    def gen_fib(l,u,a=0,b=0):
        if l==0:
            print(0,1)
        if l==1:
            print(1)
        c=0
        while c<u:
            c=a+b
            if c>=l and c<=u:
                print(c,end=" ")
            a=b
            b=c

    l,u=map(int,input().split())
    gen_fib(l,u)

