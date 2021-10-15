f=input('Enter a file name:\n')
try:
    fhandler=open(f)
except:
    print(f.upper(), 'really??')
    quit()

import re

set=list()
for x in fhandler:
    num=re.findall('[0-9]+' , x)
    for m in num:
        set.append(int(m))

print(sum(set))
