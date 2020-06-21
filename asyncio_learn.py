"""
asyncio 往往是构建 IO 密集型首选
异步IO是一种单进程、单线程的设计：它使用协同多任务处理机制，是以协程为核心的一种编程模型
异步IO模型异步IO采用消息循环的模式，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程

消息模型是如何解决同步IO必须等待IO操作这一问题的呢？
当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。
当IO操作完成后，将收到一条“IO完成”的消息，处理该消息时就可以直接获取IO操作结果。
在“发出IO请求”到收到“IO完成”的这段时间里，同步IO模型下，主线程只能挂起，
但异步IO模型下，主线程并没有休息，而是在消息循环中继续处理其他消息。这样，在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。
对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力


asyncio.gather() 类似join，会阻塞参数协程
await asyncio.gather(task1, task2) # 指定了多个任务或协程，那么它会等待所有的任务或协程task1, task2运行结束
"""

import asyncio, threading, time


async def hello():     # 创建协程函数
    print("Hello World", threading.currentThread())
    await asyncio.sleep(1)       #等待，await后需要是可等待对象，比如协程async, 任务task 和 Future
    await asyncio.create_task(count())
    print("Again")


async def count():
    print("One")

# 总耗时1s，因为三个任务(后续又创建了两个count任务)，在asyncio.sleep(1)阻塞，会继续其他任务，其他任务也阻塞则一起等待
if __name__ =="__main__":
    start_time = time.time()
    tasks = [hello(), hello(), count()]
    loop = asyncio.get_event_loop()       # 创建消息处理循环模型loop
    loop.run_until_complete(asyncio.wait(tasks))
    # asyncio.run(count())      # 运行协程
    loop.close()
    end_time = time.time()
    print("执行时间:%s" % (end_time - start_time) + "秒")







