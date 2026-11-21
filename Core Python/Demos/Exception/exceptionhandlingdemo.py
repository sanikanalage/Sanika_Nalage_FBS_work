try:
    no1=int(input('Enter a Number 1:'))
    no2=int(input('Enter a Number 2:'))
    print(no1//no2)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print("Enter Proper Integer Value")
except Exception as e:
    print(e)
else:
    print("Exception cannot occur")
finally:
    print("All task are done...")


# def add():
#     try:
#         no1=int(input('Enter number1:'))
#         no2=int(input('Enter a Number 2:'))
#         return no1//no2
#     except ZeroDivisionError as z:
#         print(z)
#     except ValueError as v:
#         print("Enter Proper Integer Value")
#     except Exception as e:
#         print(e)
#         return
#     finally:
#         print("All task are done...")

# a=add()
# print(a)
