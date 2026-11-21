from threading import Thread
import time

def fun1(str1):
    for i in str1:
        print(i, end=" ",flush=True)
        time.sleep(1)

def fun2(str2):
    for i in str2:
        print(i, end=" ",flush=True)
        time.sleep(1)

t1=Thread(name="Threa1", target=fun1, args=("11111111",))
t2=Thread(name="Thread2",target=fun2, args=("22222222",))
t1.start()
t1.join(5)
t2.start()