from functools import reduce
data=[1,2,3,4,5,6,7,8,9,10]
res=reduce(lambda num1,num2:num1+num2,data)
print(res)