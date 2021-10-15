import re
fname=input('Enter file name:\n')
fhandler=open(fname)
for x in fhandler:
    x=x.rstrip()
    mail=re.findall('^F.+ (\S+@\S+)', x)
    print(mail)
