#JumpingOnTheClouds
n=int(input())
z=input().split(" ")

s1=""
for i in z:
    s1=s1+i

s=s1.split("1")
c=0
for i in range(len(s)):
    d=(len(s[i])//2)
    if i==len(s)-1:
        c=c+d
    else:
        c=c+d+1
print(c)
