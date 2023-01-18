import threading
def thread_funct1():
    for i in range(1,10000):
        print(i,"  thread çalışıyor")
def thread_fucnt2():
    for k in range(1,10000):
        print(k,"************")
thr = threading.Thread(target=thread_funct1())
thr2=threading.Thread(target=thread_fucnt2())
thr.start()
thr2.start()