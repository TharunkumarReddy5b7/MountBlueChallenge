#Migration Birds


n=int(input())
li=list(map(int,input().split()))

f=set(li)
m=0
s=0
for i in f:
    d=li.count(i)
    if d>s:
        s=d
        m=i
    elif d==s:
        if m>i:
            m=i
print(m)




