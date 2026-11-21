# try:
#     no1=int(input('Enter a Number 1:'))
#     no2=int(input('Enter a Number 2:'))
#     if no2==0:
#         raise Exception("No2 cannot be 0")
#     else:
#         print(no1//no2)
# except Exception as e:
#     print(e)

from myexception import MyException
try:
    no1=int(input('Enter a Number 1:'))
    no2=int(input('Enter a Number 2:'))
    if no2==0:
        raise MyException()
    else:
        print(no1//no2)
except MyException as m:
    print("MYEXCEPTION")
    print(m)
except Exception as e:
    print(e)
