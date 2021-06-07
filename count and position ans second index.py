def search(n,d,s):
    c=0
    if d.count(s)<2:
        return False
    for i in range(n):
        if d[i]==s:
            c+=1
        if c==2:
            return i




n=int(input())
d=list(map(int,input().split()))
s=int(input())
print(search(n,d,s))
