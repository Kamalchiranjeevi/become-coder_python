def second_max(n,data):
    s=max(data)
    for i in data:
        if i==s:
            data.remove(s)
    p=max(data)
    return p


n=int(input())
data=list(map(int,input().split()))
print(second_max(n,data))
