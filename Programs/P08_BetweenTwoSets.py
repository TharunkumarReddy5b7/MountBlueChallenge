#Between Two Sets
#https://www.hackerrank.com/contests/mountblue-technologies/challenges/between-two-sets/problem



import math
import os
import random
import re
import sys


def getTotalX(a, b):
    a.sort()
    b.sort()
    c=min(a)
    d=max(b)
    s=0
    for i in range(c,d+1):
        d=0
        for j in a:
            if i%j!=0:
                break
        else:
            d=d+1
        if d>0:
            for k in b:
                if k%i!=0:
                    break
            else:
                s=s+1
    return s
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
