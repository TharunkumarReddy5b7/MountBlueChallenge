#Subarray Division
n=int(input())
li=list(map(int,input().split()))
k=list(map(int,input().split()))
m=k[1]
d=k[0]
s=0
if len(li)>1:
    for i in range(len(li)):
        p=sum(li[i:i+m])
        if p==d:
            s=s+1
else:
    if sum(li)==d:
        s=len(li)
        
print(s)