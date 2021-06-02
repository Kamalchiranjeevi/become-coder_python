def fib(a,b,d,num):
    if d>num:
        return
    if d==1:
        print(a,end=" ")
        d+=1
    if d==2:
        print(b,end=" ")
        d+=1
    if d<=num:
        print(a+b,end=" ")
    fib(b,a+b,d+1,num)

num=int(input())
fib(0,1,1,num)
