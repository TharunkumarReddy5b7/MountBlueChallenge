#Drawing Book

n=int(input())
n1=int(input())

li=[]
li2=[]
li3=[]
for i in range(0,n+1):
    k=i,i+1
    li.append(k)
#print(li)
for i in range(len(li)):
    if i%2==0:
        li2.append(li[i])
#print(li2)
for i in li2:
    if n1 in i:
        li3.append(li2.index(i))
k2=li2[::-1]
for i in k2:
    if n1 in i:
        li3.append(k2.index(i))
    
print(min(li3))