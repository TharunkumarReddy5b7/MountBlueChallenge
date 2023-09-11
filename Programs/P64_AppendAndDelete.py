#P64-Append and Delete
'''You have two strings of lowercase English letters. You can perform two types of operations on the first string:

Append a lowercase English letter to the end of the string.
Delete the last character of the string. Performing this operation on an empty string results in an empty string.'''


import math
import os
import random
import re
import sys


def appendAndDelete(s, t, k):
    if k>=len(s)+len(t):
        return 'Yes'
    else:
        d=min(len(s),len(t))
        
        
        for i in range(0,d):
            if s[i]!=t[i]:
                d=i
                break
        k-=len(s)-d
        k-=len(t)-d
        if(k>=0 and k%2==0):
            return 'Yes'
        else:
            return 'No'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
