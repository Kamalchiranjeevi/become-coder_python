def issorted(n,data):
    a=0
    d=0
    for i in range(n-1):
        if data[i]>data[i+1]:
            d+=1
        if data[i]<data[i+1]:
            a+=1
    if d==n-1 or a==n-1:
        return True
    else:
        return False

n=int(input())
data=list(map(int,input().split()))
print(issorted(n,data))
