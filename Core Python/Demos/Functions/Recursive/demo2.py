def SOS(n):
    if(n>0):            
        return n + SOS(n-1)
    else:
        return 0
n=5
res=SOS(n)
print(res)