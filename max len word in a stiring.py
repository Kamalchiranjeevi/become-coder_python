s=input()
data=s.split()
l=0
pos=0
for i in range(len(data)):
    if len(data[i])>l:
        l=len(data[i])
        pos=i
print(pos+1,data[pos],l)
        
