n=int(input())#1234
l=n%10        #4
temp=n//10    #123
c=0
while n:
    r=n%10
    n=n//10
    c+=1
c=c-1
temp=temp*10+r
temp=temp%10**c
temp=l*pow(10,c)+temp
print(temp)
