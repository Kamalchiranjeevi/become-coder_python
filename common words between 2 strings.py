def fun(s1,s2):
    a=[]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                a.append(s1[i])
    return(''.join(a))

s1=input()
s2=input()
s=fun(s1,s2)
print(s)
