"""
线程：
import threading   #导入线程模块

t1 = threading.Thread(target=fun1, args=(arg1,))    #利用线程类Thread，创建一个线程t1（此时fun1未执行，t1未执行）

线程类Thread的常见属性和方法：
def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None):
target： 指定线程由 run () 方法调用的可调用对象。默认为 None, 意味着不调用任何内容。
name： 指定该线程的名称。 在默认情况下，创建一个唯一的名称。
args： target调用的实参，元组格式。默认为 ()，即不传参。
daemon： 为False表示父线程在脚本运行结束时需要等待子线程结束才能结束程序，为True则表示父线程在运行结束时，子线程无论是否还有任务未完成都会跟随父进程退出，结束程序。

start()   开始线程活动，对每一个线程对象来说它只能被调用一次，它安排对象在一个另外的单独线程中调用run()方法（而非当前所处线程）
run()     代表线程活动的方法。
join()    等待，直到线程终结。这会阻塞调用这个方法的线程（主线程），直到被调用 join() 的线程终结

其他方法：
返回当前存活的线程类 Thread 对象。返回的计数等于 enumerate() 返回的列表长度。
threading.active_count()
返回当前对应调用者的控制线程的 Thread 对象。
threading.current_thread()
以列表形式返回当前所有存活的 Thread 对象。 该列表包含守护线程，current_thread() 创建的虚拟线程对象和主线程。
threading.enumerate()
返回主 Thread 对象。一般情况下，主线程是Python解释器开始时创建的线程。
threading.main_thread()
返回当前线程的ID，非0整数
threading.get_ident()
threading.current_thread().ident
返回当前线程的name
threading.current_thread().name
"""

# 线程类Thread常见方法、锁对象使用方法示例
import threading
import time


g_num = 0                              # 定义一个全局变量g_num


def test1(num):                           # 定义一个test1函数
    global g_num                      # g_num为全局变量
    mutex.acquire()                 # 上锁操作，如果之前没上锁，则上锁成功，如果之前上锁了，则程序阻塞在此处
    for i in range(num):
        g_num += 1
    mutex.release()                 # 释放锁（上锁与释放锁期间，其他进程不得使用g_num）
    print('...test1...%d...' % g_num)


def test2(num):                          # 定义一个test2函数
    global g_num                      # g_num为全局变量
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print('...test2...%d...' % g_num)


mutex = threading.Lock()             #创建一个互斥锁mutex，默认没有上锁


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))  #定义一个线程t1（不开启），指向test1函数名（注意此刻只是指定函数名，并没有调用执行sing函数）
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()                          #开启执行线程t1，调用函数（调用的test1执行完成则线程结束）
    t2.start()                          #开启执行线程t1，调用函数（不必等调用test1的线程t1执行完成即开启线程t2）
    # time.sleep(3)          #等待前面俩子线程执行完毕
    t1.join()     # (等待，直到线程终结)程序执行到本语句，会暂停，等待t1线程执行完毕，再继续执行后面语句
    print(threading.enumerate())        #主线程继续执行，调用函数print打印当前存在的线程信息
    print('...main_test...%d...' % g_num)
#如果没有延迟函数，三个线程随机执行
#main函数没执行完毕，main线程就不会结束（main线程最后结束）


# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数


# 线程类Thread常见方法run\start区别示例1
import threading


class myThread(threading.Thread):      # 重新定义一个线程类，继承threading.Thread类
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        currentTreadname = threading.currentThread()
        print("running in ", currentTreadname)


# if __name__ == '__main__':
#     # 定义一个线程任务实例thread，线程名称为"mythrd"
#     thread = myThread(1, "mythrd", 1)
#     # running in  <_MainThread(MainThread, started 10196)>
#     # 执行'thread.run()'语句的是主线程，主线程不会开辟一个新线程，而是在主线程中直接调用线程thread(此时是主线程在工作)，run()方法可多次执行
#     thread.run()
#     # running in  <myThread(mythrd, started 8904)>
#     # 执行'thread.start()'语句的是主线程，主线程会启动一个新线程，新线程thread运行(此时是thread线程在工作)，要启动新线性只能用start()执行，且只能执行一次
#     thread.start()


# 线程类Thread常见方法run\start区别示例2
import threading
import time


def add(x, y):
    for _ in range(3):
        time.sleep(0.5)
        print("x+y={}".format(x + y))


class MyThread(threading.Thread):     #定义一个线程类，重新实现start和run方法
    def start(self):
        print('start~~~~~~~~~~')
        super().start()

    def run(self):
        print('run~~~~~~~~~~~~')
        print(threading.currentThread())
        super().run()  # 调用父类的start()和run()方法


# if __name__ == '__main__':
#     t = MyThread(target=add, name="MyThread", args=(6, 7))
#     # t.start()
#     t.run()
#     print("====end===")
"""
t.start()输出如下，主线程会开启新线程MyThread，新线程MyThread会依次执行start方法，然后调用run方法，去执行target函数add：
start~~~~~~~~~~
run~~~~~~~~~~~~
<MyThread(MyThread, started 6032)>
====end===
x+y=13
x+y=13
x+y=13
t.run()输出如下，主线程不会开启新线程，而是调用线程MyThread的run方法，去执行target函数add(是主线程在执行)：
run~~~~~~~~~~~~
<_MainThread(MainThread, started 8060)>
x+y=13
x+y=13
x+y=13
====end===
"""


"""
线程同步技术：解决多个线程争抢同一个资源的情况，线程协作工作。一份数据同一时刻只能有一个线程处理。
解决线程同步的几种方法：Lock、RLock、Condition、Barrier、semaphore

event对象
e = threading.Event()  #定义一个event对象

e.wait(10)          # wait与sleep的区别是：wait会主动让出时间片，其它线程可以被调度，而sleep会占用时间片不让出
# time.sleep(10)           


其他类对象：
锁对象threading.Lock()：
原始锁处于 "锁定" 或者 "非锁定" 两种状态之一。它被创建时为非锁定状态。
它有两个基本方法， acquire() 和 release() 。
当状态为非锁定时， acquire() 将状态改为 锁定 并立即返回。
当状态是锁定时， acquire() 将阻塞至其他线程调用 release() 将其改为非锁定状态，然后 acquire() 调用重置其为锁定状态并返回。
release() 只在锁定状态下调用； 它将状态改为非锁定并立即返回。
使用锁的注意事项：
1.少用锁，必要时用锁。使用了锁，多线程访问被锁的资源时，就变成了串行，要么排队执行，要么争抢执行。
2.加锁时间越短越好，不需要就立即释放锁。
3.一定要避免死锁
"""
# 一般来说加锁以后还要有一些功能实现，在释放之前还有可能抛异常，一旦抛出异常，锁是无法释放；使用 try..except..finally 语句处理异常、保证锁的释放
import threading
import time

# 10 -> 100cups
cups = []
lock = threading.Lock()   # 创建一个锁实例lock

# 计算len(cups)前加锁，对cups加一append(1)后释放锁
def worker(lock: threading.Lock, task=100):
    while True:
        if lock.acquire(False):
            count = len(cups)
            # time.sleep(0.001)
            if count >= task:
                lock.release()
                break
            print('lenth of cups:', len(cups))
            cups.append(1)
            lock.release()


# if __name__ == '__main__':
#     for x in range(10):
#         threading.Thread(target=worker, args=(lock, 100)).start()


"""
条件对象threading.Condition()：
wait() 方法释放锁，然后阻塞直到其它线程调用 notify() 方法或 notify_all() 方法唤醒它。一旦被唤醒， wait() 方法重新获取锁并返回。它也可以指定超时时间
wait()               等待直到被通知或发生超时
wait_for(predicate)  等待，直到条件计算为真
notify()             默认唤醒一个等待这个条件的线程
notify_all()         唤醒所有正在等待这个条件的线程。这个方法行为与 notify() 相似，但并不只唤醒单一线程，而是唤醒所有等待线程
总结：
Condition采用通知机制，常用于生产者消费者模型中，解决生产者消费者速度匹配的问题;
最好的方法是使用with上下文管理。
生产者wait，会阻塞等待通知，被激活。
生产者生产好消息，对消费者发通知，可以使用notidy_all() 通知所有消费者或者notify()
"""
import threading, time, random, logging


logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
c = threading.Condition()  # 创建condition实例
e = threading.Event()
data = 0


def produce(delta):
    global data             #函数内部声明data为全局变量，produce与custom共享
    for i in range(100):
        with c:
            data = random.randint(1, 100)
            # c.notify_all()
            c.notify(2)   # 唤醒2个等待的custom
        # time.sleep(delta)  # 生产者每1秒生成一条数据
        e.wait(delta)


def custom(delta):
    global data
    while True:
        with c:
            c.wait()          # 阻塞，等待notify来唤醒,避免重复取相同的值
            logging.info(data)
        # time.sleep(delta)  # 消费者每0.5秒取一次数据;但是被生产者速度限制
        e.wait(delta)


if __name__ == '__main__':
    threading.Thread(target=produce, args=(1,)).start()
    for i in range(5):
        threading.Thread(target=custom, args=(0.5,)).start()


"""
信号量对象threading.Semaphore()：
信号量对象管理一个原子性的计数器，代表 release() 方法的调用次数减去 acquire() 的调用次数再加上一个初始值。
如果需要， acquire() 方法将会阻塞直到可以返回而不会使得计数器变成负数。在没有显式给出 value 的值时，默认为1
acquire()：   如果在进入时内部计数器的值大于零，则将其减一并立即返回 True.
如果在进入时内部计数器的值为零，则将会阻塞直到被对 release() 的调用唤醒。
一旦被唤醒（并且计数器的值大于 0），则将计数器减 1 并返回 True。
每次对 release() 的调用将只唤醒一个线程。 线程被唤醒的次序是不可确定的。
release()：释放一个信号量，将内部计数器的值增加1。当计数器原先的值为0且有其它线程正在等待它再次大于0时，唤醒正在等待的线程
"""


# 锁对象threading.Lock()
import threading

class Foo:
    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        printThird()


# 条件对象threading.Condition()
import threading


class Foo:
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.res(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.res(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.res(2, printThird)

    def res(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t)  # 参数是函数对象，返回值是bool类型
            func()
            self.t += 1
            self.c.notify_all()


# 信号量对象threading.Semaphore()
import threading

class Foo:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        printThird()

# queue1：直接使用多线程专用的阻塞队列，对于队列为空时，get方法就会自动阻塞，直到put使之非空才会释放进程
import queue

class Foo:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()


# queue2：对于定容队列来说，如果队列满了，put方法也是阻塞
import queue

class Foo:
    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.put(0)
        printSecond()
        self.q2.get()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.put(0)
        printThird()


"""
其他示例
"""
#processing and  threading
#threading部分
# # 示例1：创建两个线程t1和t2，并执行
# import threading
# import time
# import random
#
#
# def sing():                           #定义一个sing函数
#     for i in range(5):
#         print('...正在唱歌...')
#         time.sleep(random.random()*2)                 #延迟
#
#
# def dance():                          #定义一个dance函数
#     for i in range(5):
#         print('...正在跳舞...')
#         time.sleep(1)                 #延迟1s
#
#
# def main():
#     t1 = threading.Thread(target=sing)  #定义一个线程t1，指向sing函数名（注意此刻只是指定函数名，并没有调用执行sing函数）
#     t2 = threading.Thread(target=dance)
#     t1.start()                          #开始执行线程t1，调用sing函数
#     t2.start()
# #分别start开始两个并行线程，main函数等待两个线程结束后，函数运行完成
#
# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数


# #示例2：多线程与主线程执行顺序
# import threading
# import time
#
#
# def test1():                           #定义一个sing函数
#     for i in range(5):
#         print('...test1...%d...'%i)
#         time.sleep(1)
#
#
# def test2():                          #定义一个dance函数
#     for i in range(5):
#         print('...test2...%d...'%i)
#
# def main():
#     t1 = threading.Thread(target=test1)  #定义一个线程t1（不开启），指向test1函数名（注意此刻只是指定函数名，并没有调用执行sing函数）
#     t2 = threading.Thread(target=test2)
#     t1.start()                          #开启执行线程t1，调用函数（调用的test1执行完成则线程结束）
#     t2.start()                          #开启执行线程t1，调用函数（不必等调用test1的线程t1执行完成即开启线程t2）
#     # time.sleep(10)
#     print(threading.enumerate())        #主线程继续执行，调用函数print打印当前存在的线程信息
# #如果没有延迟函数，三个线程随机执行
# #main函数没执行完毕，main线程就不会结束（main线程最后结束）
#
# if __name__ == '__main__':              #函数执行起点
#     main()                              #调用main函数


# #示例3：定义的线程指向一个类class
# import threading
# import time
#
#
# class MyThread(threading.Thread):       #定义一个线程类，继承threading模块的Thread
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             self.login()                #调用login方法
#     def login(self):
#         print('...login...')
#
#
# if __name__ == '__main__':              #函数执行起点
#     t = MyThread()                      #定义一个线程，指向MyThread类
#     t.start()                           #执行线程t(线程类 是执行run函数)


# #示例4：线程共享全局变量资源竞争的问题（多个线程对全局变量进行操作，乱）-----互斥锁
import threading
import time

g_num = 0                              #定义一个全局变量g_num
def test1(num):                           #定义一个test1函数
    global g_num                      #g_num为全局变量
    mutex.acquire()                 #上锁操作，如果之前没上锁，则上锁成功，如果之前上锁了，则程序阻塞在此处
    for i in range(num):
        g_num += 1
    mutex.release()                 #释放锁（上锁与释放锁期间，其他进程不得使用g_num）
    print('...test1...%d...' % g_num)


def test2(num):                          #定义一个test2函数
    global g_num                      #g_num为全局变量
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print('...test2...%d...' % g_num)


mutex = threading.Lock()             #创建一个互斥锁mutex，默认没有上锁


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))  #定义一个线程t1（不开启），指向test1函数名（注意此刻只是指定函数名，并没有调用执行sing函数）
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()                          #开启执行线程t1，调用函数（调用的test1执行完成则线程结束）
    t2.start()                          #开启执行线程t1，调用函数（不必等调用test1的线程t1执行完成即开启线程t2）
    time.sleep(5)          #等待前面俩子线程执行完毕
    print(threading.enumerate())        #主线程继续执行，调用函数print打印当前存在的线程信息
    print('...main_test...%d...'%g_num)
#如果没有延迟函数，三个线程随机执行
#main函数没执行完毕，main线程就不会结束（main线程最后结束）


if __name__ == '__main__':              #函数执行起点
    main()                              #调用main函数
