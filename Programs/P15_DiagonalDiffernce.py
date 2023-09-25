#Diagonal Difference

n=int(input())
d=0
m=-1
a=[]
b=[]
for i in range(n):
    k=list(map(int,input().split()))
    a.append(k[d])
    d=d+1
    b.append(k[m])
    m=m-1
print(abs(sum(a)-sum(b)))
    
    