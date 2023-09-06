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

print(pangrams('We promptly judged antique ivory buckles for the next prize'))
