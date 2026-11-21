# def login():
#     print('Log in done ')
# login()

# # def login():
    # print('time started')
    # print('Logger added')
    # print('Before Login')
# #     print('Log in done ')
# #     print('Timer Stopped')
# #     print('Logger Removed')
# #     print('After Login')
# # login()

# def logout():
#     print('Log out is Done')
# logout()

# def adminlogin():
#     print('Admin Log in done ')
# adminlogin()

# def adminlogin():
#     print('time started')
#     print('Logger added')
#     print('Before Login')
#     print('Admin Log in done ')
#     print('Timer Stopped')
#     print('Logger Removed')
#     print('After Login')
# adminlogin()


#1.We can store function in variable
# def demo():
#     print('I am in demo')
# a=10
# x=demo
# print("Type of Demo=",type(demo))
# print("Type of x=",type(x))
# demo()
# x()

#2.Pass the function as an argument to another function
# def fun1():
#     print('I am from function1')
# # fun1()
# def demofun(a):
#     print('I am from demo function')
#     a()
# demofun(fun1)

#3.return inner function from outer function...
# def outer():
#     print('Outer is called')
#     def innerFunction():
#         print('Inner function is called')
#     return innerFunction
# a=outer()
# a()

#4.closur
# def outer():
#     print('Outer is called')
#     var='Virat'
#     def innerFunction():
#         print('Inner function is called',var)
#     return innerFunction
# a=outer()
# a()

#Decoretor
def demo(fun):
    print('Decoretor is called')
    def wrapper():
        print('time started')
        print('Logger added')
        print('Before Login')
        fun()
        print('after calling your function all task will be performed here..')
    return wrapper

@demo
def login():
    print('\nLogin is done\n ')

@demo
def logout():
    print('\nLogout is done\n ')

login()
logout()
