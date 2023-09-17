#Super Reduced strings
#https://www.hackerrank.com/contests/mountblue-technologies/challenges/reduced-string

s=input()

while True:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            k=s[i]+s[i+1]
            s=s.replace(k,"")
            break
    else:
        break
if len(s)>0:        
    print(s)
else:
    print("Empty String")