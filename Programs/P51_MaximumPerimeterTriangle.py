#Maximum perimeter Triangle

'''input
5
1 1 1 3 3
output
1 3 3'''

#!/bin/python3

import math
import os
import random
import re
import sys


def maximumPerimeterTriangle(sticks):
    sticks.sort()
    max=[-1]
    for i in range(len(sticks)-2):
        if(sticks[i]+sticks[i+1]>sticks[i+2]):
            max=[]
            max.append(sticks[i])
            max.append(sticks[i+1])
            max.append(sticks[i+2])
    
    return max
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
