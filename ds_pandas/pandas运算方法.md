---
layout: default
title: Pandas运算方法
parent: Pandas
nav_order: 3
---
# Pandas运算方法

Pandas基于Numpy，相应的运算也是基于Numpy的运算，只不过多了一些Pandas的内容，比如:  
- Pandas的运算结果保留索引和列标签
- 使用通用函数的时候回自动对齐索引

## 对通用函数保留索引和列标签

pandas的数据在运算的时候，对于通用函数来讲，索引和标签会自动保留。

```python
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(100, size=(3,5)), columns=["A", "B", "C", "D", "E"])

print("df=\n", df)

#如果对df使用通用函数，成成的结果是保留索引和列标签的
df2 = np.exp(df)
print("df2 \n", df2)
```

    df=
         A   B   C   D   E
    0  77  86  86  53  98
    1  56  92  27   0  83
    2   6  66   7  54  44
    df2 
                   A             B             C             D             E
    0  2.758513e+33  2.235247e+37  2.235247e+37  1.041376e+23  3.637971e+42
    1  2.091659e+24  9.017628e+39  5.320482e+11  1.000000e+00  1.112864e+36
    2  4.034288e+02  4.607187e+28  1.096633e+03  2.830753e+23  1.285160e+19


## 自动对齐索引

在对Series或者DataFrame进行二元运算的时候， Pandas会在计算过程中对齐两边索引，这对于不完整数据的处理极其重要。

在运算工程中，对于缺失值的处理采用默认缺失值处理方法，对于我们一般是添加NaN。如果想指定缺失值的填充内容，需要：
- 采用Pandas的运算方法，而不是使用运算符直接运算，因为运算符不能传递参数
- 使用fill_value参数把填充的内容传进去

在指定fill_value的时候，需要注意点是，此时是先对参与运算的数据进行缺省值处理，然后才运算，而不是先运算，得到缺省值后再处理，这样很多因为一方是NaN而最终结果也是NaN的运算因为换了缺省值而能够正常运算。

最终结果的索引内容是两个运算索引的并集。 


```python
# Series的索引自动对齐
# 此处对于缺失值的处理采用默认方法，即对于二元运算方法
# 只要由一方没有数据，则用NaN填充，任何数据与NaN运算结果都是NaN

s1 = pd.Series({"A": 1, "B":2, "C":3, "D":4, "E":5}, name="ONE")
s2 = pd.Series({ "D":4, "E":5, "F":6, "G":7}, name="TWO")

# 采用运算符，此时缺失值只能使用默认的值
print("s1 + s2 =\n", s1 + s2)

# 想更换缺失值的处理内容，需要用到pandas的运算方法和fill—value参数
print("\n s1 + s2 =\n", s1.add(s2, fill_value=100))
```

    s1 + s2 =
     A     NaN
    B     NaN
    C     NaN
    D     8.0
    E    10.0
    F     NaN
    G     NaN
    dtype: float64
    
     s1 + s2 =
     A    101.0
    B    102.0
    C    103.0
    D      8.0
    E     10.0
    F    106.0
    G    107.0
    dtype: float64



```python
# 缺失值和索引对其的DataFramne案例

df1 = pd.DataFrame(np.random.randint(10, size=(3,3)), index=list("ABC"), columns=['I', 'II', 'III'])
print("df1 = \n", df1)


df2 = pd.DataFrame(np.random.randint(100, 200, size=(3,3)), index=list("CDE"), columns=['II', 'III', "IV"])
print("df1 = \n", df1)

# 使用操作符，index和colums保留， 缺失值采用默认方法处理
df3 = df1 + df2
print("\n df3 = \n", df3)


# 使用pandas方法，可以指定缺省值
df4 = df1.add(df2, fill_value=0)
print("\n df4 = \n", df4)
```

    df1 = 
        I  II  III
    A  9   6    7
    B  1   9    2
    C  3   1    3
    df1 = 
        I  II  III
    A  9   6    7
    B  1   9    2
    C  3   1    3
    
     df3 = 
         I     II    III  IV
    A NaN    NaN    NaN NaN
    B NaN    NaN    NaN NaN
    C NaN  180.0  138.0 NaN
    D NaN    NaN    NaN NaN
    E NaN    NaN    NaN NaN
    
     df4 = 
          I     II    III     IV
    A  9.0    6.0    7.0    NaN
    B  1.0    9.0    2.0    NaN
    C  3.0  180.0  138.0  160.0
    D  NaN  108.0  108.0  155.0
    E  NaN  182.0  145.0  114.0


## DataFrame和Series的运算

DataFrame和Series运算默认采用的是行运算，即一行一行的运算，如果想要按列运算，需要使用axis参数。


```python
# 默认是按行来进行计算
A1 = np.random.randint(10, size=(3,5))
print("A1 = \n", A1)

print("\n A1 - A1[1] = \n", A1 - A1[1])
```

    A1 = 
     [[7 6 4 8 2]
     [9 0 1 2 7]
     [5 9 1 5 0]]
    
     A1 - A1[1] = 
     [[-2  6  3  6 -5]
     [ 0  0  0  0  0]
     [-4  9  0  3 -7]]



```python
# 如果想按列运算，可以使用axis参数

df1 = pd.DataFrame(A1, columns=list("ABCDE"))
print("df1 = \n", df1)

# 默认按行计算
df2 = df1 - df1.iloc[1]
print("\n df2 = \n", df2)

# 按列运算需要使用axis参数
df3 = df1.subtract(df["B"], axis=0)
print("\n df3 = \n", df3)
```

    df1 = 
        A  B  C  D  E
    0  7  6  4  8  2
    1  9  0  1  2  7
    2  5  9  1  5  0
    
     df2 = 
        A  B  C  D  E
    0 -2  6  3  6 -5
    1  0  0  0  0  0
    2 -4  9  0  3 -7
    
     df3 = 
         A   B   C   D   E
    0 -79 -80 -82 -78 -84
    1 -83 -92 -91 -90 -85
    2 -61 -57 -65 -61 -66
