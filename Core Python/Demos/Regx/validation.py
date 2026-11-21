import re
mo="9623654901"
pat=r"[^1-6]\d{9}$"
r=re.match(pat,mo)
if r==None:
    print("Mobile Number is not valid")
else:
    print("Mobile Number is Valid")