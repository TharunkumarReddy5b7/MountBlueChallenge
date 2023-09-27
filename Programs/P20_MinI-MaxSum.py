#Mini-Max Sum

li=list(map(int,input().split()))


        
li.sort()

d=sum(li[:4])
e=sum(li[1:5])
print(d,e)
