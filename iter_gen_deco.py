#

# #迭代：
# #可迭代对象：list， str。。。
# #示例1：判断是否可迭代对象
# from collections.abc import Iterable
# print(isinstance([11, 22, 33], Iterable))       #判断list[11, 22, 33]是否可迭代对象


# #示例2：类class的可迭代对象创建
# class FBNQ(object):
#     def __init__(self, n):
#         self.n = n                #对象入参，属性
#         self.current_n = 0
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):           #有了__iter__，成为可迭代对象
#         return self               #迭代时返回所有属性值
#
#     def __next__(self):           #有了__next__，成功实现next操作，并引入所有属性值
#         if self.current_n < self.n:
#             ret = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.current_n += 1
#             return ret
#         else:
#             raise StopIteration   #之后main函数每次for循环，实际只调用__next__方法
#
#
# def main():
#     fb = FBNQ(20)
#     for num in fb:          #fb是类FBNQ的一个实例，此处是可迭代对象
#         print(num)
#
#
# if __name__ == '__main__':
#     main()


# #生成器：一种特殊的迭代器
# #示例1：列表与生成器的区别举例
# a = [x*2 for x in range(10)]  #列表，占用内存资源
# b = (x*2 for x in range(10))  #生成器，通过__next__方法生成下一个元素
# print(a)                      #打印一个列表
# for i in a:
#     print(i, end=' ')         #打印列表中的每个元素
# print(b)                      #生成器
# for i in b:
#     print(i, end=' ')         #依次打印（可迭代对象）


# #示例2：生成器创建的常用方法，yield
# #含有yield的函数不再是一个函数，而是一个生成器
# #调用next方法的时候执行到yield时，返回yield值，等待下次next调用接着从yield执行
# def create_num(n):           #含有yield，create_num为一个生成器
#     a, b = 0, 1
#     current_n = 0
#     while current_n < n:
#         yield a              #create_num生成器的返回值为a，然后暂停，等待下次next调用接着从yield执行
#         a, b = b, a + b
#         current_n += 1
#
#
# obj = create_num(10)         #obj为一个生成器，可迭代对象
# for num in obj:
#     print(num)


############yield解密############yield解密############yield解密############yield解密
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
# g = foo()                     #带yield的foo不再是一个函数，而是一个迭代对象，赋给g：此时并不执行foo函数。
# print(next(g))                #执行到yield，返回yield的值并暂停，下次接着执行。
# print("*"*20)
# print(next(g))                #打印空值res



def dec(f):                            #2.装饰函数入参为foo，返回值wrapper函数名：wrapper(2)【注意wrapper函数中的f为dec入参foo】
    n = 3
    def wrapper(*args, **kw):          #3.wrapper(2)  >>>  f(2)*3   >>>  foo(2)*3
        return f(*args, **kw)*n
    return wrapper                     #注意第二步执行dec的时候，此处返回的是wrapper函数名，不是wrapper()，因此不会去执行wrapper函数的定义部分
@dec                                   #1.该语句是把待装饰函数名foo进行装饰赋给dec函数：foo = dec（foo）,即dec(foo)(2)
def foo(n):                            #4.foo(2)*3   >>>  2*2*3   >>>  12
    return n*2
print(foo(2))

#其实就是在foo(2)的基础上进行了*n(n=3)的操作

