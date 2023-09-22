#PlusMinus
n=input()
arr = list(map(int, input().split()))


l=len(arr)
a=0
b=0
c=0
for i in arr:
    if i>0:
        a=a+1
    elif i<0:
        b=b+1
    else:
        c=c+1
        
d=a/l
e=b/l
f=c/l
print("{:.6f}".format(d))
print("{:.6f}".format(e))
print("{:.6f}".format(f))
    
        
    
