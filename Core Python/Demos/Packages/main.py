#1.Direct import
# import FirstbitSolution.demo1
# FirstbitSolution.demo1.add(10,20)

#2.from packagename.modulename import member
# from FirstbitSolution.demo1 import add
# add(10,30)

#3.from packagename.modulename import multiple member
# from FirstbitSolution.demo1 import add,sub
# add(10,20)
# sub(20,10)

#4.from packagename.modulename import all things
# from FirstbitSolution.demo1 import *
# add(10,20)
# sub(20,10)
# mul(5,10)
# div(20,5)

#5.By using alice
import FirstbitSolution.demo1 as f
f.add(10,5)
f.sub(30,5)

