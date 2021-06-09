def max_len_ones(n,data):
    a=0
    c=0
    if n==0:
        return 0
    for i in range(n):
        if data[i]==1:
            c+=1
        else:
            if a<c:
                a=c
            c=0
    return max(c,a)
        
        
       

n=int(input())
data=list(map(int,input().split()))
print(max_len_ones(n,data))

