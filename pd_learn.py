"""
1.Pandas基本介绍
Pandas的主要两个数据结构：Series和DataFrame
Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N - 1（N为长度）的整数型索引。
"""

import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])

print(s)
"""
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
"""
"""DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）。DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典。"""
dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])  # index与columns

print(df)
"""
                   a         b         c         d
2016-01-01 -0.253065 -2.071051 -0.640515  0.613663
2016-01-02 -1.147178  1.532470  0.989255 -0.499761
2016-01-03  1.221656 -2.390171  1.862914  0.778070
2016-01-04  1.473877 -0.046419  0.610046  0.204672
2016-01-05 -1.584752 -0.700592  1.487264 -1.778293
2016-01-06  0.633675 -1.414157 -0.277066 -0.442545
"""
print(df['b'])  # 筛选b列数据

"""
2016-01-01   -2.071051
2016-01-02    1.532470
2016-01-03   -2.390171
2016-01-04   -0.046419
2016-01-05   -0.700592
2016-01-06   -1.414157
Freq: D, Name: b, dtype: float64
"""
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))  # index与columns默认是从0开始自然数
print(df1)

"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)  # 对每一列的数据类型不一样

"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""

print(df2.index)  # 看对列的序号
# Int64Index([0, 1, 2, 3], dtype='int64')
print(df2.columns)  # 看每种数据的名称
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
print(df2.values)  # 只看值，不看索引
"""
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']], dtype=object)
"""

print(df2.T)  # 翻转数据
"""                   
0                    1                    2  \
A                    1                    1                    1   
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2013-01-02 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo  

"""

print(df2.sort_values(by='B'))  # 对数据 值 排序输出

"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
print(df2.sort_index(axis=1, ascending=False))  # 对数据的 index 进行排序并输出

"""
     F      E  D    C          B    A
0  foo   test  3  1.0 2013-01-02  1.0
1  foo  train  3  1.0 2013-01-02  1.0
2  foo   test  3  1.0 2013-01-02  1.0
3  foo  train  3  1.0 2013-01-02  1.0
"""


"""2. Pandas选择数据"""
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# 建立了一个 6X4 的矩阵数据
"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""

print(df['A'])  # print(df.A) 选择A列数据
"""
2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int64
"""
print(df[0:3])  # 连续选择多行数据
"""
            A  B   C   D
2013-01-01  0  1   2   3
2013-01-02  4  5   6   7
2013-01-03  8  9  10  11
"""
print(df['20130102':'20130104'])  # 连续选择多行数据

"""
A   B   C   D
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
"""
print(df.loc['20130102'])  # 通过标签选择数据
"""
A    4
B    5
C    6
D    7
Name: 2013-01-02 00:00:00, dtype: int64
"""
print(df.loc[:, ['A', 'B']])  # 通过标签选择数据
"""
             A   B
2013-01-01   0   1
2013-01-02   4   5
2013-01-03   8   9
2013-01-04  12  13
2013-01-05  16  17
2013-01-06  20  21
"""
print(df.loc['20130102', ['A', 'B']])  # 通过标签选择数据
"""
A    4
B    5
Name: 2013-01-02 00:00:00, dtype: int64
"""
print(df.iloc[3, 1])  # 通过位置选择数据
# 13
print(df.iloc[3:5, 1:3])  # 通过位置选择数据
"""
             B   C
2013-01-04  13  14
2013-01-05  17  18
"""
print(df.iloc[[1, 3, 5], 1:3])  # 通过位置选择数据
"""
             B   C
2013-01-02   5   6
2013-01-04  13  14
2013-01-06  21  22
"""
print(df.ix[:3, ['A', 'C']])  # 通过ix混合选择数据
"""
            A   C
2013-01-01  0   2
2013-01-02  4   6
2013-01-03  8  10
"""
print(df[df.A > 8])  # 通过判断选择数据
"""
             A   B   C   D
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""


"""
3.pandas设置值
"""
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# 创建一个矩阵数据
"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""

df.iloc[2, 2] = 1111
df.loc['20130101', 'B'] = 2222  # 利用索引或者标签修改值
"""
             A     B     C   D
2013-01-01   0  2222     2   3
2013-01-02   4     5     6   7
2013-01-03   8     9  1111  11
2013-01-04  12    13    14  15
2013-01-05  16    17    18  19
2013-01-06  20    21    22  23
"""
df.B[df.A > 4] = 0  # 根据条件：对于A大于4的位置. 更改B在相应位置上的数为0
"""
                A     B     C   D
2013-01-01   0  2222     2   3
2013-01-02   4     5     6   7
2013-01-03   8     0  1111  11
2013-01-04  12     0    14  15
2013-01-05  16     0    18  19
2013-01-06  20     0    22  23 
"""
df['F'] = np.nan  # 对整列做批处理修改数据
"""
             A     B     C   D   F
2013-01-01   0  2222     2   3 NaN
2013-01-02   4     5     6   7 NaN
2013-01-03   8     0  1111  11 NaN
2013-01-04  12     0    14  15 NaN
2013-01-05  16     0    18  19 NaN
2013-01-06  20     0    22  23 NaN
"""
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))  # 添加数据：加上 Series 序列（但是长度必须对齐）
"""
             A     B     C   D   F  E
2013-01-01   0  2222     2   3 NaN  1
2013-01-02   4     5     6   7 NaN  2
2013-01-03   8     0  1111  11 NaN  3
2013-01-04  12     0    14  15 NaN  4
2013-01-05  16     0    18  19 NaN  5
2013-01-06  20     0    22  23 NaN  6
"""


"""
4.Pandas处理丢失数据
"""
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan  # 更改两处元素为空
"""
             A     B     C   D
2013-01-01   0   NaN   2.0   3
2013-01-02   4   5.0   NaN   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
"""

df.dropna(
    axis=0,  # 0: 对行进行操作; 1: 对列进行操作
    how='any'  # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
)
"""          #直接去掉有 NaN 的行或列
             A     B     C   D
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
"""
df.fillna(value=0)  # 将 NaN 的值用其他值代替
"""
             A     B     C   D
2013-01-01   0   0.0   2.0   3
2013-01-02   4   5.0   0.0   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
"""
df.isnull()  # 判断是否有缺失数据 NaN, 为 True 表示缺失数据
"""
                A      B      C      D
2013-01-01  False   True  False  False
2013-01-02  False  False   True  False
2013-01-03  False  False  False  False
2013-01-04  False  False  False  False
2013-01-05  False  False  False  False
2013-01-06  False  False  False  False
"""
np.any(df.isnull()) == True  # 检测在数据中是否存在 NaN, 如果存在就返回 True
# True


"""
5.Pandas导入导出
"""
import pandas as pd  # 加载模块

# 读取csv
data = pd.read_csv('student.csv')
# 打印出data
print(data)

data.to_pickle('student.pickle')  # 将资料存取成pickle


"""
6.Pandas合并\concat
"""

import pandas as pd
import numpy as np

# 定义资料集
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

# concat纵向合并
res = pd.concat([df1, df2, df3], axis=0)  # axis=0是预设值
# 打印结果
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0

# 承上一个例子，并将index_ignore设定为True
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # ignore_index (重置 index)
# 打印结果
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  2.0  2.0  2.0  2.0
# 7  2.0  2.0  2.0  2.0
# 8  2.0  2.0  2.0  2.0

import pandas as pd
import numpy as np

# 定义资料集
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# 纵向"外"合并df1与df2
# 函数默认join='outer'。此方式是依照column来做纵向合并，有相同的column上下合并在一起，其他独自的column个自成列，原本没有值的位置皆以NaN填充。
res = pd.concat([df1, df2], axis=0, join='outer')
print(res)
#     a    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0

# 承上一个例子
# 纵向"内"合并df1与df2
# 只有相同的column合并在一起，其他的会被抛弃
res = pd.concat([df1, df2], axis=0, join='inner')
# 打印结果
print(res)
#     b    c    d
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0

# 重置index并打印结果
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
print(res)
#     b    c    d
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
# 5  1.0  1.0  1.0

import pandas as pd
import numpy as np

# 定义资料集
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

# 依照`df1.index`进行横向合并
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])  # join_axes (依照 axes 合并)
# 打印结果
print(res)
#     a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0

# 移除join_axes，并打印结果
res = pd.concat([df1, df2], axis=1)
print(res)
#     a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0

# append只有纵向合并，没有横向合并。
import pandas as pd
import numpy as np

# 定义资料集
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 将df2合并到df1的下面，以及重置index，并打印出结果
res = df1.append(df2, ignore_index=True)
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0

# 合并多个df，将df2与df3合并至df1的下面，以及重置index，并打印出结果
res = df1.append([df2, df3], ignore_index=True)
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  1.0  1.0  1.0  1.0
# 7  1.0  1.0  1.0  1.0
# 8  1.0  1.0  1.0  1.0

# 合并series，将s1合并至df1，以及重置index，并打印出结果
res = df1.append(s1, ignore_index=True)
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  2.0  3.0  4.0


"""
7.Pandas合并merge
pandas中的merge和concat类似, 但主要是用于两组有key
column的数据, 统一索引的数据.通常也被用在Database的处理当中。
"""
# 依据一组KEY合并
import pandas as pd

# 定义资料集并打印出
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#    A   B  key
# 0  A0  B0  K0
# 1  A1  B1  K1
# 2  A2  B2  K2
# 3  A3  B3  K3

print(right)
#    C   D key
# 0  C0  D0  K0
# 1  C1  D1  K1
# 2  C2  D2  K2
# 3  C3  D3  K3

# 依据key column合并，并打印出
res = pd.merge(left, right, on='key')
print(res)
A
B
key
C
D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2
# 3  A3  B3  K3  C3  D3

# 依据二组KEY合并
import pandas as pd

# 定义资料集并打印出
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#    A   B key1 key2
# 0  A0  B0   K0   K0
# 1  A1  B1   K0   K1
# 2  A2  B2   K1   K0
# 3  A3  B3   K2   K1
print(right)
#    C   D key1 key2
# 0  C0  D0   K0   K0
# 1  C1  D1   K1   K0
# 2  C2  D2   K1   K0
# 3  C3  D3   K2   K0
# 合并时有4种方法how = ['left', 'right', 'outer', 'inner']，预设值how='inner'
# 依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)
#    A   B   key1  key2  C  D
# 0  A0  B0   K0   K0  C0  D0
# 1  A2  B2   K1   K0  C1  D1
# 2  A2  B2   K1   K0  C2  D2

res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)
#     A    B key1 key2    C    D
# 0   A0   B0   K0   K0   C0   D0
# 1   A1   B1   K0   K1  NaN  NaN
# 2   A2   B2   K1   K0   C1   D1
# 3   A2   B2   K1   K0   C2   D2
# 4   A3   B3   K2   K1  NaN  NaN
# 5  NaN  NaN   K2   K0   C3   D3

res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)
#    A   B key1 key2    C    D
# 0  A0  B0   K0   K0   C0   D0
# 1  A1  B1   K0   K1  NaN  NaN
# 2  A2  B2   K1   K0   C1   D1
# 3  A2  B2   K1   K0   C2   D2
# 4  A3  B3   K2   K1  NaN  NaN

res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(res)
#     A    B key1 key2   C   D
# 0   A0   B0   K0   K0  C0  D0
# 1   A2   B2   K1   K0  C1  D1
# 2   A2   B2   K1   K0  C2  D2
# 3  NaN  NaN   K2   K0  C3  D3

###indicator=True会将合并的记录放在新的一列
import pandas as pd

# 定义资料集并打印出
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
#   col1 col_left
# 0     0        a
# 1     1        b
print(df2)
#   col1  col_right
# 0     1          2
# 1     2          2
# 2     2          2

# 依据col1进行合并，并启用indicator=True，最后打印出
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
#   col1 col_left  col_right      _merge
# 0   0.0        a        NaN   left_only
# 1   1.0        b        2.0        both
# 2   2.0      NaN        2.0  right_only
# 3   2.0      NaN        2.0  right_only

# 自定indicator column的名称，并打印出
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)
#   col1 col_left  col_right indicator_column
# 0   0.0        a        NaN        left_only
# 1   1.0        b        2.0             both
# 2   2.0      NaN        2.0       right_only
# 3   2.0      NaN        2.0       right_only

# 依据index合并
import pandas as pd

# 定义资料集并打印出
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left)
#     A   B
# K0  A0  B0
# K1  A1  B1
# K2  A2  B2
print(right)
#     C   D
# K0  C0  D0
# K2  C2  D2
# K3  C3  D3

# 依据左右资料集的index进行合并，how='outer',并打印出
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
#      A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C2   D2
# K3  NaN  NaN   C3   D3

# 依据左右资料集的index进行合并，how='inner',并打印出
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
#     A   B   C   D
# K0  A0  B0  C0  D0
# K2  A2  B2  C2  D2

# 解决overlapping的问题
import pandas as pd

# 定义资料集
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

# 使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
#    age_boy   k  age_girl
# 0        1  K0         4
# 1        1  K0         5


"""
8.Pandas plot出图
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 随机生成1000个数据
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# 为了方便观看效果, 我们累加这个数据
data.cumsum()
# pandas 数据可以直接观看其可视化形式
data.plot()
plt.show()

data = pd.DataFrame(
    np.random.randn(1000, 4),
    index=np.arange(1000),
    columns=list("ABCD")
)
# 生成一个1000*4 的DataFrame，并对他们累加
data.cumsum()
data.plot()
plt.show()

# 分别给scatter的x，y两个属性指定数据
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class1')
# 再画一个在同一个ax上面，选择不一样的数据列，不同的 color 和 label
# 将之下这个 data 画在上一个 ax 上面
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class2', ax=ax)
plt.show()
