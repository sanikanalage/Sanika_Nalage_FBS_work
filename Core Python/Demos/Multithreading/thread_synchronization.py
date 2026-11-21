from threading import Thread,Lock

def deposite(amt):

    lock.acquire()
    with open('balance.txt','r') as fp:
        bal=int(fp.read())
    bal=bal+amt
    with open('balance.txt','w') as fp:
        fp.write(str(bal))
    lock.release()

def withdraw(amt):
    
    lock.acquire()
    with open('balance.txt','r') as fp:
        bal=int(fp.read())
    bal=bal-amt
    with open('balance.txt','w') as fp:
        fp.write(str(bal))
    lock.release()

global lock
lock=Lock()

t1=Thread(name="Thread1", target=deposite, args=(20000,))
t2=Thread(name="Thread2", target=withdraw, args=(10000,))
t1.start()
t2.start()
