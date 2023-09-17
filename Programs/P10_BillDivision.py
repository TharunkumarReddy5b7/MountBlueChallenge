#BillDivision
#https://www.hackerrank.com/contests/mountblue-technologies/challenges/bon-appetit

n,n1=list(map(int,input().split()))
arr=list(map(int,input().split()))
ans=int(input())

s=sum(arr)-arr[n1]

ans1=s//2

if ans1==ans:
    print("Bon Appetit")
else:
    print(ans-ans1)