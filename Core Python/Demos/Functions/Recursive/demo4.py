def DSO(num):
    if num>0:
        d=num%10
        num=num//10
        print(d)
        DSO(num)
num=int(input('Enter a Number:'))
DSO(num)