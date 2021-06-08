def max_len_sorted_list(n,data):
    a=0
    c=1
    for i in range(n-1):
        if data[i]<data[i+1]:
            c+=1
        else:
            if a<c:
                a=c
            c=1
    if a<c:
        return c
    return a
        
        
       

n=int(input())
data=list(map(int,input().split()))
print(max_len_sorted_list(n,data))

