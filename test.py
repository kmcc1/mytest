from multiprocessing import Process
import time,os


#
# # 操作共享内存
# def man():
#     print(os.getpid())
#     time.sleep(100)
kwargs={'song':'凉凉'}
kw = ""
for k,w in kwargs.items():
    kw += "%s = %s,"%(k,w)
total = "self.func(args,%s)"%kw
print(total)
#
# m = Process(target=man)
#
# print(os.getpid())
# m.start()
#
# m.join()

