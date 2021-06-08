def bouncy(n,data):
    l=0
    h=0
    if data[0]>data[1]:
        h+=1
    else:
        l+=1
    for i in range(1,n-1):
        if h==1 and data[i]<data[i+1]:
            l=1
            h=0
        elif l==1 and data[i]>data[i+1]:
            h=1
            l=0
        else:
            return False
    return True
       
        
            
    

n=int(input())
data=list(map(int,input().split()))
print(bouncy(n,data))

