#1st Program
#Sales By Match

#There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.


n=int(input())
li=list(map(int,input().split(" ")))

s=list(set(li))

m=0
for i in s:
    m=m+li.count(i)//2
    
print(m)
    
