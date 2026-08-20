def sumofDigits(num):
    if(num>0):
        d=num%10
        num=num//10
        return d + sumofDigits(num)
    else:
        return 0
num=int(input('Enter a Number: '))
res=sumofDigits(num)
print(res)