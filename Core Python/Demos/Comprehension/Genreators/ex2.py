# def demo():
#     for i in range(10,100):
#         yield i
# g=demo()
# print(next(g))
# print('Next Value')
# print(next(g))
# print('Next Value')
# print(next(g))
# print('Next Value')
# print(next(g))
# print('Next Value')
# print(next(g))

# list=[i for i in range(100,201)]
# print(list)

list=(i for i in range(100,201))
# print(list)
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
# print(type(next(list)))
# print(type(list))