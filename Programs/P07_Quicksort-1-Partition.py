#QuickSort-1-Partition
#https://www.hackerrank.com/contests/mountblue-technologies/challenges/quicksort1
n=int(input())
li=list(map(int,input().split()))
l=[]
m=[li[0]]
r=[]
d=li[0]


for i in range(1,len(li)):
    if li[i]<d:
        l.append(li[i])
    else:
        r.append(li[i])
        
k=l+m+r
print(*k)

