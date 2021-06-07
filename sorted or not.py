def sorted_not(n,data):
    t=data.copy()
    m=data.copy()
    t.sort()
    m.sort(reverse=True)
    if(data==t or data==m):
        return True
    else:
        return False

n=int(input())
data=list(map(int,input().split()))
print(sorted_not(n,data))
