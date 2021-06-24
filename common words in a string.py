def common(s1,s2):
    a=[]
    for i in s1.split():
        for j in s2.split():
            if i==j:
                a.append(i)
    return ' '.join(a)




s1=input()
s2=input()
s=common(s1,s2)
print(s)
