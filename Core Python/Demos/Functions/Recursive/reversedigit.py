


def reverseDigit(num, rev):
    if(num > 0):
        d = num % 10
        rev = rev * 10 + d
        num=num//10
        return reverseDigit(num , rev)
    return rev

num = int(input("Enter a number: "))
res = reverseDigit(num, 0)
print(res)