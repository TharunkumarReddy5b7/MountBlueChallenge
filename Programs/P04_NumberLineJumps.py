#NumberLineJumps
n=input().split(" ")

x1=int(n[0])
v1=int(n[1])
x2=int(n[2])
v2=int(n[3])


if x2>x1 and v2>=v1:
    print("NO")
else:
    if (x1-x2)%(v2-v1)==0:
        print("YES")
    else:
        print("NO")