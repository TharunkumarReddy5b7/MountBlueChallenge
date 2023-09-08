#Breaking the records
n=int(input())

li=list(map(int,input().split(" ")))

max=li[0]
min=li[0]
ma=0
mi=0
for i in li:
    if i>max:
        max=i
        ma+=1
    if i<min:
        min=i
        mi+=1

print("{} {}".format(ma,mi))
        
    
