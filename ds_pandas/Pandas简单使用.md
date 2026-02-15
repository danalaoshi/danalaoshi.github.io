---
layout: default
title: Pandas简单使用
parent: Pandas
nav_order: 2
---

# pandas简单使用

pandas三个主要的数据结构是Series，DataFrame和Index，三个结构用来对数据进行操作。  

本章主要介绍pandas三大件，让读者对pandas有个简单的了解：
- Series
- DataFrame
- Index

##  pandas.Series对象

是一个带索引数据构成的一维数组。 

Series给数组和一组索引绑定在一起，有点类似于list，但是Series的索引绑定的是显式索引。

如果想获取绑定的数据和索引内容，分别可以使用values属性和index属性。

### Series的创建

岁Series对象的创建主要分为：
- 使用数组直接创建,此时索引为默认索引
- 使用数组创建，显式指定索引
- 使用字典创建


```
# Series对象的创建
# 直接使用数组进行创建

import pandas as pd

data = pd.Series([10, 11, 12, 13,14])

print("完整Series内容是：\n", data)

print("\nSeries的值： \n\n", data.values)

print("\nSeries的索引是： \n", data.index)
```

    完整Series内容是：
     0    10
    1    11
    2    12
    3    13
    4    14
    dtype: int64
    
    Series的值： 
    
     [10 11 12 13 14]
    
    Series的索引是： 
     RangeIndex(start=0, stop=5, step=1)

```python
# 显式制定索引

data_index = pd.Series([10,11,12,13,14], index=[1,2,3,4,5])

print("data_index: \n", data_index)
```

    data_index: 
     1    10
    2    11
    3    12
    4    13
    5    14
    dtype: int64



```python
#使用字典进行创建

d = {"one":1, "two":2, "three":3, "four":4, "five":5}
d_s = pd.Series(d)
print(d_s)

```

    one      1
    two      2
    three    3
    four     4
    five     5
    dtype: int64



```python
import pandas as pd
# 对于字典，可以通过index来显式筛选内容
# 注意索引

d = {4:"four", 5:"five", 1:"one", 3:"three", 2:"two"}
d_s = pd.Series(d,  index=[2,1,3])
print(d_s)
```

    2      two
    1      one
    3    three
    dtype: object


### Series对象的简单使用

Series和Numpy的数组很像，他们的区别主要体现在索引上：
- Numpy通过隐士索引来对数据进行操作
- Series通过显式索引来将索引和数值关联

显式索引具有更强大的功能，你可以对其进行修改操作：

Series的values和indexs可以直接使用，查看。
请注意这俩的类型。




```python
import pandas as pd

data = pd.Series([10,11,12,13,14], index=[1,2,3,9,5])

print("data.values=", data.values)
print(type(data.values))

print()
print("data.indexs=", data.index)
print(type(data.index))
```

    data.values= [10 11 12 13 14]
    <class 'numpy.ndarray'>
    
    data.indexs= Int64Index([1, 2, 3, 9, 5], dtype='int64')
    <class 'pandas.core.indexes.numeric.Int64Index'>



```python
### 对于series的对象的访问，完全可以像数组那样使用

# 数据选择使用显式索引
print("第一个值是：", data[1])

# 隐式索引
print("\n 前三个值是：\n ", data[:9])
print("\n 前三个值是：\n ", data[:4])
```

    第一个值是： 10
    
     前三个值是：
      1    10
    2    11
    3    12
    9    13
    5    14
    dtype: int64
    
     前三个值是：
      1    10
    2    11
    3    12
    9    13
    dtype: int64



```python
# 对于不按顺序排列的index同样可以
# 请注意下例data[:2]是到index=2的那个位置结束，并不是从0开始的下标直到2结束

data = pd.Series([10, 11, 12, 13, 14], index=[54, 32, 2, 1, 9])
print("不连续数字作为索引也是可以的：\n", data)

print("\n data3  =", data[32])

print("\n data[:1] = \n", data[:1])
```

    不连续数字作为索引也是可以的：
     54    10
    32    11
    2     12
    1     13
    9     14
    dtype: int64
    
     data3  = 11
    
     data[:1] = 
     54    10
    dtype: int64



```python
# 对于自定义index同样可以使用切片
# ！！！注意此时切片的结束位置，结果是包含结束位置的值的!!!

d = {"one":1, "two":2, "three":3, "four":4, "five":5}
d_s = pd.Series(d)

print('d_s["four"] = ', d_s["four"])
print('d_s[":four"] = \n', d_s[:"four"])
```

    d_s["four"] =  4
    d_s[":four"] = 
     one      1
    two      2
    three    3
    four     4
    dtype: int64


对数据的选取，Series处理的并不是特别好，在对数据访问的时候，显式索引和隐士索引容易造成混淆。

为了应对这种混乱，Python为我们提供了三个索引器，用以清晰访问数据：
- loc: 只使用显式索引, label based indexing
- iloc：只使用隐士索引, positional indexing
- ix：前两种索引的混合模式，主要用在DataFrame中, 不推荐


首先我们观察一下对Series的访问的显式索引和隐士索引的使用。



```python
# Series对显式索引和隐式索引的使用

s = pd.Series([11,12,13,14,15], index=[3,5,7,9,1])
print("s = \n", s)

# Series对于单个内容的访问，采用的是显式索引
# s[1]表示的是显式索引 ”1“ 的内容
print("\n s[1]=", s[1])


# Series切片采用的是隐士所含，即默认是从下标0开始的升序索引
# s[1:3] 选中的内容是s[1] 和 s[2]
print("\n s[1:3] = \n", s[1:3])


s = pd.Series([1,2,3,4,5], index=["one", "two", "three", "four", "five"])
print("\n s=\n", s)


# 对于显式索引的切片， 是包含最后一位内容的
# 这一点跟隐士索引有很大区别
print('\n s["two": "four"]=', s["two":"four"])
```

    s = 
     3    11
    5    12
    7    13
    9    14
    1    15
    dtype: int64
    
     s[1]= 15
    
     s[1:3] = 
     5    12
    7    13
    dtype: int64
    
     s=
     one      1
    two      2
    three    3
    four     4
    five     5
    dtype: int64
    
     s["two": "four"]= two      2
    three    3
    four     4
    dtype: int64



```python
# loc索引器表示切片和取值都是显式的，不使用隐式索引。

s = pd.Series([11,12,13,14,15], index=[3,5,7,9,1])
print("s = \n", s)

print("\n s.loc[3] = ", s.loc[3])
print("\n s.loc[3:9] = \n", s.loc[3:9])
```

    s = 
     3    11
    5    12
    7    13
    9    14
    1    15
    dtype: int64
    
     s.loc[3] =  11
    
     s.loc[3:9] = 
     3    11
    5    12
    7    13
    9    14
    dtype: int64



```python
# iloc索引器表示切片和取值都是隐式的，不使用显式索引
s = pd.Series([11,12,13,14,15], index=[3,5,7,9,1])
print("s = \n", s)

print("\n s.iloc[3] = ", s.iloc[3])
print("\n s.iloc[3:9] = \n", s.iloc[3:9])
```

    s = 
     3    11
    5    12
    7    13
    9    14
    1    15
    dtype: int64
    
     s.iloc[3] =  14
    
     s.iloc[3:9] = 
     9    14
    1    15
    dtype: int64



## pandas.DataFrame对象

- DataFrame可以看做是通用的NumPy数组，也可以看做特殊的字典
- DataFrame最常见的结构可以想象成一个Excel内容，每一行都有行号，每一列都有列名的二维结构

创建DataFrame的方式比较多，常见的有：
- 通过单个Series创建
- 通过字典列表创建
- 通过Series对象字典创建
- 通过NumPy二维数组创建
- 通过Numpy结构化数组创建


```python
# 通过单个Series对象创建

import pandas as pd

s = pd.Series([1,2,3,4,5])
print("S=\n", s)

print()
df = pd.DataFrame(s, columns=['digits'])
print("df=\n", df)
```

    S=
     0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64
    
    df=
        digits
    0       1
    1       2
    2       3
    3       4
    4       5



```python
# 通过字典列表创建

dl = [{"个": i, "十":i*10, "百":i*100} for i in range(1,5)]
print("dl = ", dl)

df = pd.DataFrame(dl)
print("df = \n", df)


# 在通过字典创建的时候，如果有的值并不存在，则自动用NaN填充
# 参看下面例子
dl = [{"a":1, "b":1}, {"b":2, "c":2}, {"c":3, "d":3}]
df = pd.DataFrame(dl)
print("df = \n", df)
```

    dl =  [{'个': 1, '十': 10, '百': 100}, {'个': 2, '十': 20, '百': 200}, {'个': 3, '十': 30, '百': 300}, {'个': 4, '十': 40, '百': 400}]
    df = 
        个   十    百
    0  1  10  100
    1  2  20  200
    2  3  30  300
    3  4  40  400
    df = 
          a    b    c    d
    0  1.0  1.0  NaN  NaN
    1  NaN  2.0  2.0  NaN
    2  NaN  NaN  3.0  3.0



```python
# 通过Series对象字典创建

s1 = pd.Series([i for i in range(1,6)], index=[1,2,3,4,5])
s2 = pd.Series([i*10 for i in range(1,6)], index=[3,4,5,6,7])

df = pd.DataFrame({"个": s1, "十":s2})
print("df = \n", df)
```

    df = 
          个     十
    1  1.0   NaN
    2  2.0   NaN
    3  3.0  10.0
    4  4.0  20.0
    5  5.0  30.0
    6  NaN  40.0
    7  NaN  50.0



```python
# 通过Numpy二维数组创建
import numpy as np

df = pd.DataFrame(np.zeros([5,3]), 
                  columns=["A", "B", "C"], 
                 index=["one", "two", "three", "four", "five"])
print("df=\n",df)

```

    df=
              A    B    C
    one    0.0  0.0  0.0
    two    0.0  0.0  0.0
    three  0.0  0.0  0.0
    four   0.0  0.0  0.0
    five   0.0  0.0  0.0



```python
import pandas as pd
import numpy as np
# 通过Numpy结构化数组

d = np.zeros(3, dtype=[("A", "i8"), ("B", "f8")])
print("d = \n", d)

print()
df = pd.DataFrame(d)
print("df=\n", df)
```

    d = 
     [(0, 0.) (0, 0.) (0, 0.)]
    
    df=
        A    B
    0  0  0.0
    1  0  0.0
    2  0  0.0


对于DataFrame数据的使用方式，我们以前说过，可以把DataFrame看做是具有行列号和首部标题行的Excel表格，而去除掉列号和首部标题行后，DataFrame就可以看做是一个二维数组。

对于DataFrame的数据选择，可以采用字典形式的访问，此时访问的是一列值，也可以采用切片等，下面详细进行介绍：



```python
dl = [{"个": i, "十":i*10, "百":i*100} for i in range(1,5)]


df = pd.DataFrame(dl)
print("df = \n", df)


```

    df = 
        个   十    百
    0  1  10  100
    1  2  20  200
    2  3  30  300
    3  4  40  400



```python
# 使用字典的方式访问

print("df['百'] =\n",  df['百'] )

```

    df['百'] =
     0    100
    1    200
    2    300
    3    400
    Name: 百, dtype: int64


如果选取的键的名字跟上例中的df的属性名称或者函数不冲突，可以直接采用圆点符号进行访问：

```python
# 上面访问方式等价于下面访问方式
# 但下面访问方式并非通用，可能会引起冲突
print("df.百=\n", df.百)
```

    df.百=
     0    100
    1    200
    2    300
    3    400
    Name: 百, dtype: int64


DataFrame可以看做是一个增强版的二维数组，此时他的全部值可以用DataFrame.values来表示：



```python
# values属性的使用
print("df.values = \n", df.values)
```

    df.values = 
     [[  1  10 100]
     [  2  20 200]
     [  3  30 300]
     [  4  40 400]]


对于DataFrame的访问，推荐时候用loc，iloc或者ix三个所引器进行访问，避免引起混淆：



```python
# 使用loc进行显示访问
print('df.loc[:2, :"十"]=\n', df.loc[:2, :"十"])

```

    df.loc[:2, :"十"]=
        个   十
    0  1  10
    1  2  20
    2  3  30



```python
# 时候iloc进行隐式访问
print('df.iloc[:2, :2] = \n', df.iloc[:2, :2])
```

    df.iloc[:2, :2] = 
        个   十
    0  1  10
    1  2  20



```python
# 或者使用ix进行混合访问
# indexing的初衷是避免访问混淆，但ix显然并没有达到这一点，所以，ix索引器不推荐使用
# 使用ix访问，可能会引起警告错误

print(df.ix[:2, :"十"])
```

       个   十
    0  1  10
    1  2  20
    2  3  30


    /Users/augs/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:5: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      """


## pandas.Index对象

Pandas的Index对象是一个独立的对象，用来表示数据的索引，可以把它看做不可变的数组(tuple)或者有序的集合。

当作为不可变数组的时候，除了数组的一些读操作外，还具有一些NumPy数组的属性。

Index作为有序集合操作主要是为了进行一些基于集合的操作，比如集合的交差并补操作。



```python
# Idnex作为不可变数组

idx = pd.Index([2,4,6,8,10])
print("idx = ", idx)
print("idx[1:4] = ", idx[1:4])
print("idx.size=", idx.size)
print("idx.shape=", idx.shape)
print("idx.ndim", idx.ndim)
print("idx.dtype=", idx.dtype)
```

    idx =  Int64Index([2, 4, 6, 8, 10], dtype='int64')
    idx[1:4] =  Int64Index([4, 6, 8], dtype='int64')
    idx.size= 5
    idx.shape= (5,)
    idx.ndim 1
    idx.dtype= int64



```python
# Index作为有序集合

idx_1 = pd.Index([1,3,5,6,7,])
idx_2 = pd.Index([2,4,6,7,8,9])

print("交集： idx_1 & idx_2 = ", idx_1 & idx_2)
print("并集： idx_1 | idx_2 = ", idx_1 | idx_2)
print("异或： idx_1 ^ idx_2 = ", idx_1 ^ idx_2)
```

    交集： idx_1 & idx_2 =  Int64Index([6, 7], dtype='int64')
    并集： idx_1 | idx_2 =  Int64Index([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')
    异或： idx_1 ^ idx_2 =  Int64Index([1, 2, 3, 4, 5, 8, 9], dtype='int64')
