"""
1.Numpy属性
ndim：维度
shape：行数和列数
size：元素个数
"""
import numpy as np    # 导入模块


array = np.array([[1, 2, 3], [2, 3, 4]])  # 列表转化为矩阵
print(array)
"""
array([[1, 2, 3],
       [2, 3, 4]])
"""
print(array.ndim)  # 维度
# 2
print(array.shape)  # 行数和列数
#  (2, 3)
print(array.size)  # 元素个数
# 6


"""
2.Numpy的创建
array
array：创建数组
dtype：指定数据类型
zeros：创建数据全为0
ones：创建数据全为1
empty：创建数据接近0
arrange：按指定范围创建数据
linspace：创建线段
"""


a = np.array([2, 23, 4])  # list 1d  #创建数组
print(a)
# [2 23 4]
a = np.array([2, 23, 4], dtype=np.int)  # 指定数据类型
print(a.dtype)
# int 64
a = np.array([2, 23, 4], dtype=np.float)  # 指定数据类型
print(a.dtype)
# float64
a = np.array([[2, 23, 4], [2, 32, 4]])  # 2d 矩阵 2行3列
print(a)
"""
[[ 2 23  4]
 [ 2 32  4]]
"""
a = np.zeros((3, 4))  # 数据全为0，3行4列
"""
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
"""
a = np.ones((3, 4), dtype=np.int)  # 数据为1，3行4列
"""
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
"""
a = np.empty((3, 4))  # 数据为empty，3行4列
"""
array([[  0.00000000e+000,   4.94065646e-324,   9.88131292e-324,
          1.48219694e-323],
       [  1.97626258e-323,   2.47032823e-323,   2.96439388e-323,
          3.45845952e-323],
       [  3.95252517e-323,   4.44659081e-323,   4.94065646e-323,
          5.43472210e-323]])
"""
a = np.arange(10, 20, 2)  # 指定范围10-19 的数据，2步长
"""
array([10, 12, 14, 16, 18])
"""
a = np.arange(12).reshape((3, 4))  # 3行4列，0到11，改变数据的形状
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
"""
a = np.linspace(1, 10, 20)  # 开始端1，结束端10，且分割成20个数据，生成线段
"""
array([  1.        ,   1.47368421,   1.94736842,   2.42105263,
         2.89473684,   3.36842105,   3.84210526,   4.31578947,
         4.78947368,   5.26315789,   5.73684211,   6.21052632,
         6.68421053,   7.15789474,   7.63157895,   8.10526316,
         8.57894737,   9.05263158,   9.52631579,  10.        ])
"""


"""
3.Numpy
基础运算
"""
import numpy as np


a = np.array([10, 20, 30, 40])  # array([10, 20, 30, 40])
b = np.arange(4)  # array([0, 1, 2, 3])   #创建两个一维矩阵

c = a - b  # array([10, 19, 28, 37])  #矩阵的差
c = a + b  # array([10, 21, 32, 43])  #矩阵的和
c = a * b  # array([  0,  20,  60, 120])  #矩阵的积
c = b ** 2  # array([0, 1, 4, 9])   #矩阵中各个元素的乘方

c = 10 * np.sin(a)  # 对矩阵a中各个元素x进行10*sin（x），返回矩阵
# array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])

print(b < 3)  # 对矩阵b中各个元素x进行b<x判断，返回bool型矩阵
# array([ True,  True,  True, False], dtype=bool)
a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2, 2))  # 创建两个二维矩阵
print(a)
# array([[1, 1],
#       [0, 1]])
print(b)
# array([[0, 1],
#       [2, 3]])

c_dot = np.dot(a, b)  # 同 a.dot(b)，矩阵的乘法运算（对应行乘对应列得到相应元素）
# array([[2, 4],
#       [2, 3]])
a = np.array([[10, 20, 30, 40]])  # 注意两个[]才代表1x4矩阵
b = np.array([[0], [1], [2], [3]])  # 注意每一列要用[]间隔
print(a.shape)
print(b.shape)

import numpy as np

a = np.random.random((2, 4))  # 生成一个2行4列的矩阵，元素是从0到1的随机数
print(a)
# array([[ 0.94692159,  0.20821798,  0.35339414,  0.2805278 ],
#       [ 0.04836775,  0.04023552,  0.44091941,  0.21665268]])

np.sum(a)  # 4.4043622002745959 对矩阵中所有元素进行求和
np.min(a)  # 0.23651223533671784 对矩阵中所有元素寻找最小值
np.max(a)  # 0.90438450240606416 对矩阵中所有元素寻找最大值
np.sum(a, axis=1)  # 以行为单元，对矩阵中各行元素进行求和
#  [ 1.96877324  2.43558896]
np.min(a, axis=0)  # 以列为单元，对矩阵中各列元素寻找最小值
# [ 0.23651224  0.41900661  0.36603285  0.46456022]
np.max(a, axis=1)  # 以行为单元，对矩阵中各行元素寻找最大值
# [ 0.84869417  0.9043845 ]

import numpy as np

A = np.arange(2, 14).reshape((3, 4))  # 创建一个矩阵
# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])

print(np.argmin(A))  # 0   矩阵中最小元素的索引
print(np.argmax(A))  # 11  矩阵中最大元素的索引

print(np.mean(A))  # 7.5
print(np.average(A))  # 7.5
print(A.mean())  # 7.5   矩阵中所有元素的平均值

print(A.median())  # 7.5  矩阵中所有元素的中位数

print(np.cumsum(A))  # 累加函数：生成项矩阵元素是从原矩阵首项累加到对应项元素之和
# [2 5 9 14 20 27 35 44 54 65 77 90]
print(np.diff(A))  # 累差函数：每一行中后一项与前一项之差。故矩阵计算后会少一列
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
print(np.nonzero(A))  # 将所有非零元素的行与列坐标分开，构成两个分别关于行和列的矩阵
# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))

import numpy as np

A = np.arange(14, 2, -1).reshape((3, 4))  # 重新生成一个矩阵
# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

print(np.sort(A))  # 对矩阵A的每一行进行排序
# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])

print(np.transpose(A))
print(A.T)  # 矩阵的转置，上同
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
print(np.clip(A, 5, 9))  # 对于A，最小值5、最大值9用于让函数判断矩阵中元素是否有比最小值小的或者比最大值大的元素，并将这些指定的元素转换为最小值或者最大值
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])


"""
4.Numpy索引
"""
A = np.arange(3, 15).reshape((3, 4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""

print(A[2])  # [11 12 13 14]     #A的第3行
print(A[1][1])  # 8               #A的第二行第二个元素
print(A[1, 1])  # 8              #A的第二行第二个元素，同上
print(A[1, 1:3])  # [8 9]            #A的第二行，第二到四个元素切片操作
print(A.flatten())  # 将多维的矩阵进行展开成1行的数列
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


"""
5.Numpy array合并
"""
import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

print(np.vstack((A, B)))  # vertical stack 上下合并，参数(A,B)
"""
[[1,1,1]
 [2,2,2]]
"""
print(np.hstack((A, B)))  # horizontal stack 左右合并，参数(A,B)
# [1,1,1,2,2,2]

print(A[np.newaxis, :])  # 对于单行array，通过[np.newaxis,:]转换为单行矩阵
# [[1 1 1]]
print(A[np.newaxis, :].shape)
# (1,3)
print(A[:, np.newaxis])  # 对于单行array，通过[:,np.newaxis]转换为单列矩阵
"""
[[1]
[1]
[1]]
"""
print(A[:, np.newaxis].shape)
# (3,1)

C = np.concatenate((A, B, B, A), axis=0)  #
print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""
D = np.concatenate((A, B, B, A), axis=1)  #
print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""


"""
6.Numpy array分割
"""
A = np.arange(12).reshape((3, 4))
print(A)
"""
array([[ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11]])
"""

print(np.split(A, 2, axis=1))  # 纵向分割（等量分成2份）
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
print(np.split(A, 3, axis=0))  # 横向分割（等量分成3份）
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.array_split(A, 3, axis=1))  # 纵向分割（不等量分成3份）
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2],
        [ 6],
        [10]]), array([[ 3],
        [ 7],
        [11]])]
"""
print(np.vsplit(A, 3))  # 等于 print(np.split(A, 3, axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.hsplit(A, 2))  # 等于 print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""

"""
7. copy & deep
copy
“= 的赋值方式会带有关联性”
"""
import numpy as np

a = np.arange(4)
# array([0, 1, 2, 3])
b = a
c = a
d = b  # “=”的赋值方式
d[1:3] = [22, 33]  # array([11, 22, 33,  3])  更改d的值，a、b、c也会改变
print(a)  # array([11, 22, 33,  3])
b is a  # True   确认b、c、d是与a相同

""" “copy()的赋值方式没有关联性”"""
b = a.copy()  # deep copy
print(b)  # array([11, 22, 33,  3])
a[3] = 44
print(a)  # array([11, 22, 33, 44])
print(b)  # array([11, 22, 33,  3])   a与b已经没有关联
