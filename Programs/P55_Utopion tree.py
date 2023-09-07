#utopian tree



import math
import os
import random
import re
import sys



def utopianTree(n):
    h=1
    for i in range(1,n+1):
        if(i%2==0):
            h+=1
        else:
            h=h*2
            
    return h
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
