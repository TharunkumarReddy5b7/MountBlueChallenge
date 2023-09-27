#Grading Students

n=int(input())

for i in range(n):
    m=int(input())
    if m<38:
        print(m)
    else:
        if m==100:
            print(100)
        for i in range(m+1,101):
            if i%5==0:
                d=i-m
                if d<3:
                    print(i)
                    break
                else:
                    print(m)
                    break