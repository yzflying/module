"""
并行：同时做某些事，可以互不干扰的同一时刻做几件事。
并发：也是同时做某些事，但是某个时间随片只能做一件事。

进程：是系统进行资源分配和调度的基本单位，是一个或多个线程的集合，在操作系统中，每个进程在内存中相对独立的，进程间不可以随便的共享数据。
线程：是操作系统能够进行调度的最小单位，每个进程至少有一个线程，同一个进程内的线程可以共享进程的资源，每一个线程拥有自己独立的堆栈。

线程的状态：
1.就绪Ready：线程能够运行，但在等待被调度。可能线程刚刚创建启动，或刚刚从阻塞中恢复，或者被其它线程抢占.(线程被创建；阻塞线程条件满足；运行线程时间随片用完；)
2.运行Running：线程正在运行.(就绪线程被调度；)
3.阻塞Blocked：线程等待外部事件发生而无法运行，如I/O操作.(运行线程等待资源)
4.终止Terminated：线程完成，或退出，或被取消.(运行线程完成或取消)

GIL全局解释器锁:
哪怕是在多CPU的情况下，即使每个线程恰好调度到了每个CPU上，有了这把大锁，同一时刻只能有一个CPU使用CPython执行一个线程的字节码，其它线程只能阻塞等待
IO密集型：由于线程阻塞，就会调度其它线程；(wait会让出时间片，让其它线程有机会被调度、sleep不会)，大量使用网络IO、磁盘IO
CPU密集型：当前线程可能会连续的获得GIL，导致其它线程几乎无法使用CPU，造成类似多核CPU单线程执行；多进程可以完全独立的进程环境中运行程序，可以充分地利用多处理器
IO密集型，使用多线程；CPU密集型，使用多进程，绕开GIL
协程：IO密集型的任务另外一种选择就是协程，协程其实是运行在单个线程中的，避免了多线程模型中的线程上下文切换，减少了很大的开销
"""


"""
进程：Process、Pool类
"""


from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()


# 示例进程池：创建一个容纳一定数目进程的池，池中的进程结束后自动候补新的进程执行。
# 候补进程会重复利用结束进程的进程ID
# 示例4：多进程文件拷贝


import multiprocessing
import os, time, random
rpath = r'E:\DESKTOP\scrapy_test\quanzhan\123'   #为文件夹路径，非具体文件
wpath = r'E:\DESKTOP\django_tests\new'


def copyfile(path1, path2):   #path1,path2入参为路径+文件名，俩入参
    fr = open(path1, 'rb')
    fw = open(path2, 'wb')
    cotent = fr.read()
    fw.write(cotent)
    fr.close()
    fw.close()


def main():
    filelist = os.listdir(rpath)  # 读取rpath路径下的所有文件的文件名,list类型
    po = multiprocessing.Pool(2)     #创建一个容量为2的进程池po
    for filename in filelist:
        po.apply_async(copyfile, args=(os.path.join(rpath, filename), os.path.join(wpath, filename),)) #往进程池添加进程或候补进程
    print('.....starting.....')
    po.close()                       #关闭进程池，不在接收新的候补进程添加
    po.join()                        #主进程运行到此处会阻塞，等待进程池po运行完毕才继续执行
    print('.....ending.....')


# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数


"""
进程间通信：管道、队列、共享内存、套接字
1. 管道：指的是无名管道，本质上可以看做一种文件，只存在于内存当中，不会存盘。不同进程通过系统提供的接口来向管道中读取或者写入数据。
也就是说我们通过这样一个中间介质为进程提供交流的方式。无名管道的局限在于一般只用于有直接关联关系的父子进程
管道通信三步曲：
    创建Pipe，得到两个connection对象conn1和conn2；
    父进程持有conn1，将conn2传递给子进程；
    父子进程通过对持有的connection对象进行send和recv操作以进行数据传递和接受
我们创建的是全双工管道，也可以创建半双工管道，具体使用可以参照官网描述
"""
from multiprocessing import Process, Pipe


def pstart(pname, conn):
    conn.send("Data@subprocess")
    print(conn.recv())          # Data@parentprocess


if __name__ == '__main__':
    conn1, conn2 = Pipe(True)
    sub_proc = Process(target=pstart, args=('subprocess', conn2,))
    sub_proc.start()
    print(conn1.recv())        # Data@subprocess
    conn1.send("Data@parentprocess")
    sub_proc.join()


"""
2. 具名管道（FIFO）可以在任意进程间进行通信
"""
import os, time
from multiprocessing import Process

input_pipe = "./pipe.in"
output_pipe = "./pipe.out"

def consumer():
    if os.path.exists(input_pipe):
        os.remove(input_pipe)
    if os.path.exists(output_pipe):
        os.remove(output_pipe)

    os.mkfifo(output_pipe)
    os.mkfifo(input_pipe)
    in1 = os.open(input_pipe, os.O_RDONLY)        # read from pipe.in
    out1 = os.open(output_pipe, os.O_SYNC | os.O_CREAT | os.O_RDWR)
    while True:
        read_data = os.read(in1, 1024)
        print("received data from pipe.in: %s @consumer" % read_data)
        if len(read_data) == 0:
            time.sleep(1)
            continue

        if "exit" in read_data:
            break
        os.write(out1, read_data)
    os.close(in1)
    os.close(out1)

def producer():
    in2 = None
    out2 = os.open(input_pipe, os.O_SYNC | os.O_CREAT | os.O_RDWR)

    for i in range(1, 4):
        msg = "msg " + str(i)
        len_send = os.write(out2, msg)
        print("------product msg: %s by producer------" % msg)
        if in2 is None:
            in2 = os.open(output_pipe, os.O_RDONLY)        # read from pipe.out
        data = os.read(in2, 1024)
        if len(data) == 0:
            break
        print("received data from pipe.out: %s @producer" % data)
        time.sleep(1)

    os.write(out2, 'exit')
    os.close(in2)
    os.close(out2)

if __name__ == '__main__':
    pconsumer = Process(target=consumer, args=())
    pproducer = Process(target=producer, args=())
    pconsumer.start()
    time.sleep(0.5)
    pproducer.start()
    pconsumer.join()
    pproducer.join()

"""
3. 消息队列queue
简单示例见文件processandthread.py
"""

"""
4. 共享内存
共享内存是一种常用的，高效的进程之间的通信方式，为了保证共享内存的有序访问，需要对进程采取额外的同步措施
"""
from multiprocessing import Process
import mmap
import contextlib
import time

def writer():
    with contextlib.closing(mmap.mmap(-1, 1024, tagname='cnblogs', access=mmap.ACCESS_WRITE)) as mem:
        for share_data in ("Hello", "Alpha_Panda"):
            mem.seek(0)
            print('Write data:== %s == to share memory!' % share_data)
            mem.write(str.encode(share_data))
            mem.flush()
            time.sleep(0.5)

def reader():
    while True:
        invalid_byte, empty_byte = str.encode('\x00'), str.encode('')
        with contextlib.closing(mmap.mmap(-1, 1024, tagname='cnblogs', access=mmap.ACCESS_READ)) as mem:
            share_data = mem.read(1024).replace(invalid_byte, empty_byte)
            if not share_data:
                """ 当共享内存没有有效数据时结束reader """
                break
            print("Get data:== %s == from share memory!" % share_data.decode())
        time.sleep(0.5)


if __name__ == '__main__':
    p_reader = Process(target=reader, args=())
    p_writer = Process(target=writer, args=())
    p_writer.start()
    p_reader.start()
    p_writer.join()
    p_reader.join()
"""
5. socket

"""


"""
其他示例
"""

# #process进程：运行起来的程序就是进程，每个子进程占用独立的资源，有自己的内存来存储变量数据（会造成资源的浪费）
# # #示例1：创建两个进程p1和p2
# import multiprocessing
# import time
#
#
# def test1():                           #定义一个test1函数
#     while True:
#         print('1.......')
#         time.sleep(1)
#
#
# def test2():                          #定义一个test2函数
#     while True:
#         print('2.......')
#         time.sleep(1)
#
#
# def main():
#     p1 = multiprocessing.Process(target=test1)  #定义一个进程p1（不开启），指向test1函数名（注意此刻只是指定函数名，并没有调用执行sing函数）
#     p2 = multiprocessing.Process(target=test2)
#     p1.start()                          #开启执行进程p1，调用函数（调用的test1执行完成则线程结束）
#     p2.start()                          #开启执行进程p1，调用函数（不必等调用test1的进程p1执行完成即开启进程p2）
#
#
# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数


# #示例2：创建两个进程p1和p2，通过queue队列实现进程间通信
# import multiprocessing
# # get put full empty,队列Queue的操作函数
#
# def download_from_web(q):                           #从网页下载数据
#     data = [11, 22, 33, 44]
#     for temp in data:
#         q.put(temp)
#         print('downloading and saving to Queue,%d' % temp)
#
#
# def analysis_data(q):                          #分析数据
#     waitting_analysis_data = list()
#     while True:
#         data = q.get()
#         waitting_analysis_data.append(data)
#         if q.empty():
#             break
#     print(waitting_analysis_data)
#
#
# def main():
#     q = multiprocessing.Queue()            #创建一个队列q，用于两个进程通信的中转
#     p1 = multiprocessing.Process(target=download_from_web, args=(q,))  #定义一个进程p1（不开启），指向函数名（注意此刻只是指定函数名，并没有调用执行函数）
#     p2 = multiprocessing.Process(target=analysis_data, args=(q,))
#     p1.start()                          #开启执行进程p1，调用函数（调用的test1执行完成则线程结束）
#     p2.start()                          #开启执行进程p1，调用函数（不必等调用test1的进程p1执行完成即开启进程p2）
#
#
# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数


# #示例3：进程池：创建一个容纳一定数目进程的池，池中的进程结束后自动候补新的进程执行。
# #候补进程会重复利用结束进程的进程ID
# import multiprocessing
# import os, time, random
#
#
# def worker(msg):
#     t_start = time.time()
#     print('%s starting to %d'% (msg, os.getpid()))
#     time.sleep(random.random()*2)
#     t_stop = time.time()
#     print(msg, 'over,it takes %0.2f time' % (t_stop - t_start))
#
# def main():
#     po = multiprocessing.Pool(3)     #创建一个容量为3的进程池po
#     for i in range(10):
#         po.apply_async(worker, (i,)) #往进程池添加进程或候补进程
#     print('.....starting.....')
#     po.close()                       #关闭进程池，不在接收新的候补进程添加
#     po.join()                        #主进程运行到此处会阻塞，等待进程池po运行完毕才继续执行
#     print('.....ending.....')
#
#
# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数

# #示例4：进程池：创建一个容纳一定数目进程的池，池中的进程结束后自动候补新的进程执行。
# #候补进程会重复利用结束进程的进程ID
# #示例4：多进程文件拷贝
# import multiprocessing
# import os, time, random
# rpath = r'E:\DESKTOP\scrapy_test\quanzhan\123'   #为文件夹路径，非具体文件
# wpath = r'E:\DESKTOP\django_tests\new'
#
#
# def copyfile(path1, path2):   #path1,path2入参为路径+文件名，俩入参
#     fr = open(path1, 'rb')
#     fw = open(path2, 'wb')
#     cotent = fr.read()
#     fw.write(cotent)
#     fr.close()
#     fw.close()
#
# def main():
#     filelist = os.listdir(rpath)  # 读取rpath路径下的所有文件的文件名,list类型
#     po = multiprocessing.Pool(2)     #创建一个容量为2的进程池po
#     for filename in filelist:
#         po.apply_async(copyfile, args=(os.path.join(rpath, filename), os.path.join(wpath, filename),)) #往进程池添加进程或候补进程
#     print('.....starting.....')
#     po.close()                       #关闭进程池，不在接收新的候补进程添加
#     po.join()                        #主进程运行到此处会阻塞，等待进程池po运行完毕才继续执行
#     print('.....ending.....')
#
#
# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数
