#Beautiful Binary String

'''A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example

We promptly judged antique ivory buckles for the next prize

The string contains all letters in the English alphabet, so return pangram.'''


#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    a="abcdefghijklmnopqrstuvwxyz"
    z=""
    
    for i in s:
        if i!=" " and i.lower() not in z:
            z+=i.lower()
    if ''.join(sorted(z))==a:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
