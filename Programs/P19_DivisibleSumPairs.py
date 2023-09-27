#Divisile Sum Pairs

n=list(map(int,input().split()))
li=list(map(int,input().split()))

s=0

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if (li[i]+li[j])%n[1]==0:
            s=s+1
print(s)
        
