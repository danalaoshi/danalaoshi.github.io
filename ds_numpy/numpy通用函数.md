---
layout: default
title: Numpy通用函数
parent: Numpy
nav_order: 4
---
# Numpy通用函数(ufunc)

通用函数就是能同时对元素内所有元素逐个进行运算的函数。

numpy专注于大量数据运算，python本身也能够对大量数据进行计算，但是速度相对缓慢，为了解决这个问题，numpy对数据运算进行优化，使计算变得迅速简洁。

numpy进行快速数据运算的关键在于向量化。

numpy支持运算符操作，运算符看作是运算类函数的简写。

从运算符参与运算数据的角度分类，通用函数分为两类：
- 一元通用函数(unary ufunc): 对单个输入进行操作
- 二元通用函数(binary ufunc): 对两个输入进行操作

从功能上分类，通用函数分为算术计算函数，双曲三角函数，位运算类，比较运算符，弧度角度转换类等。

更加复杂的通用函数放在scipy.special模块下，如果需要，可以查阅相关文档。



## 通用函数-算数操作类
常见的算数运算操作符号和对应的函数名称如下：
- +：np.add
- -: np.subtract
- -: np.negative
- *: np.multiply
- /: np.divide
- //: np.floor_divide
- **: np.power
- %: np.mod
- absolute(abs):绝对值，比较特殊，可以处理复数，当求复数的绝对值的时候，结果是复数的幅度


```python
# 运算符举例
# 需要注意的是逐个元素运算

a = np.arange(20).reshape([4,5])
print("a = \n", a)

print("a+3 = \n", a + 3)
print("a//5 = \n", a  // 3)
print("a**2 = \n", a ** 2)
print("-a = \n",  -a)
print("a % 3 = \n", a % 3)
```

    a = 
     [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    a+3 = 
     [[ 3  4  5  6  7]
     [ 8  9 10 11 12]
     [13 14 15 16 17]
     [18 19 20 21 22]]
    a//5 = 
     [[0 0 0 1 1]
     [1 2 2 2 3]
     [3 3 4 4 4]
     [5 5 5 6 6]]
    a**2 = 
     [[  0   1   4   9  16]
     [ 25  36  49  64  81]
     [100 121 144 169 196]
     [225 256 289 324 361]]
    -a = 
     [[  0  -1  -2  -3  -4]
     [ -5  -6  -7  -8  -9]
     [-10 -11 -12 -13 -14]
     [-15 -16 -17 -18 -19]]
    a % 3 = 
     [[0 1 2 0 1]
     [2 0 1 2 0]
     [1 2 0 1 2]
     [0 1 2 0 1]]


absolute函数用来求绝对值，abs是缩写形式。

** 需要注意的是，对复数求绝对值的时候，得到的是复数的幅度值


```python
# abs举例

a = np.arange(-10,0).reshape([2,5])
print("a = \n", a)

print("abs(a) = \n", abs(a))

a = np.array([1-2j, 3-4j, 5-6j, 7-9j])
print("abs(a) = ", abs(a))
```

    a = 
     [[-10  -9  -8  -7  -6]
     [ -5  -4  -3  -2  -1]]
    abs(a) = 
     [[10  9  8  7  6]
     [ 5  4  3  2  1]]
    abs(a) =  [ 2.23606798  5.          7.81024968 11.40175425]


三角函数分为正三角函数和反三角函数。 

进行反三角函数的求值的时候，可能这里会得到一个值错误警告，但是不会报错。


```python
# 三角函数举例

theta = np.linspace(0, np.pi, 5)
print("theta = ", theta)

# 三角函数
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

# 反三角函数
print("arcsin(theta) = ", np.arcsin(theta))
print("arccos(theta) = ", np.arccos(theta))
print("arctan(theta) = ", np.arctan(theta))

```

    theta =  [0.         0.78539816 1.57079633 2.35619449 3.14159265]
    sin(theta) =  [0.00000000e+00 7.07106781e-01 1.00000000e+00 7.07106781e-01
     1.22464680e-16]
    cos(theta) =  [ 1.00000000e+00  7.07106781e-01  6.12323400e-17 -7.07106781e-01
     -1.00000000e+00]
    tan(theta) =  [ 0.00000000e+00  1.00000000e+00  1.63312394e+16 -1.00000000e+00
     -1.22464680e-16]
    arcsin(theta) =  [0.         0.90333911        nan        nan        nan]
    arccos(theta) =  [1.57079633 0.66745722        nan        nan        nan]
    arctan(theta) =  [0.         0.66577375 1.00388482 1.16942282 1.26262726]


    C:\Users\augs\Anaconda3\lib\site-packages\ipykernel_launcher.py:12: RuntimeWarning: invalid value encountered in arcsin
      if sys.path[0] == '':
    C:\Users\augs\Anaconda3\lib\site-packages\ipykernel_launcher.py:13: RuntimeWarning: invalid value encountered in arccos
      del sys.path[0]


指数和对数函数常用的是以e, 2, 10为底的运算，同样对于非常小的值输入，numpy也给出了精度好的运算方式。



```python
a = np.array([1,2,3])
print("a = ",a)
print("e^a = ",np.exp(a))
print("2^a = ",np.exp2(a))

# 直接使用power函数进行操作
print("3^a = ",np.power(3, a))

print("ln(a) = ", np.log(a))
print("log2(a) = ", np.log2(a))
print("log10(a) = ", np.log10(a))
```

    a =  [1 2 3]
    e^a =  [ 2.71828183  7.3890561  20.08553692]
    2^a =  [2. 4. 8.]
    3^a =  [ 3  9 27]
    ln(a) =  [0.         0.69314718 1.09861229]
    log2(a) =  [0.        1.        1.5849625]
    log10(a) =  [0.         0.30103    0.47712125]


以下特殊的版本，对非常小的输入值，能保持比较好的精度。


```python
a = np.array([0, 0.001, 0.01, 0.1])
print("exp(a) - 1 = ", np.expm1(a))
print("log(1+x) = ", np.log1p(a))
```

    exp(a) - 1 =  [0.         0.0010005  0.01005017 0.10517092]
    log(1+x) =  [0.         0.0009995  0.00995033 0.09531018]



```python
# 对exp和expm1在极小数值上的比较
print("expm1 = ", np.expm1(1e-10))
print("exp-1 = ",  np.exp(1e-10) - 1)

# log1p和log(1+x)的比较
print("log1p = ", np.log1p(1e-99))
print("log(1+x) = ", np.log(1 + 1e-99))
```

    expm1 =  1.00000000005e-10
    exp-1 =  1.000000082740371e-10
    log1p =  1e-99
    log(1+x) =  0.0


## 通用函数-比较类操作

此类比较操作也是逐个元素操作，最后的结果是一个包含布尔值的数组，数组的shape，size等同原数组一致。

此类操作包含：
- ==: np.equal
- !=: no.not_equal
- <: np.less
- <=: np.less_equal
- \>: np.greater
- \>=: np.greater_equal


```python
# 比较类操作案例
a = np.random.randint(100, size=(2,5))
print("a = \n", a)

print("a < 50 : \n", a < 50)
print("a == 50 : \n", a == 50)
```

    a = 
     [[67 14 95 28 51]
     [80  5 65 41  0]]
    a < 50 : 
     [[False  True False  True False]
     [False  True False  True  True]]
    a == 50 : 
     [[False False False False False]
     [False False False False False]]



```python
# 常用的np关于比较运算的操作
# count_nonzero用来统计非零的值个数
a = np.random.randint(100, size=(2,5))
print("a = \n", a)

print()

# count_nonzero用来统计非零的值个数
# 统计小于50的数字的个数
print("小于50的格式总共 {}个".format(np.count_nonzero(a < 50)))

#或者
print()

# 布尔值也可以作为数字运算，所以可以直接求和
# 统计大于50的数字的个数
print("大于50的格式总共 {}个".format(np.sum(a > 50)))

```

    a = 
     [[52  3 57  5 50]
     [47 31 46 77 69]]
    
    小于50的格式总共 5个
    
    大于50的格式总共 4个



```python
# 如果检测结果是否包含真值或者全部是否都是某个值
# 可以用any或者all
a = np.array([1,2,3,4,5,6])
print("a = ", a)

print("a中包含大于10的数字吗：", np.any(a > 10))
print("a中包含大于5的数字吗：", np.any(a > 5))
print("a中的数组都大于0吗：", np.all(a > 0))
 


```

    a =  [1 2 3 4 5 6]
    a中包含大于10的数字吗： False
    a中包含大于5的数字吗： True
    a中的数组都大于0吗： True


## 通用函数-按位运算

numpy提供了可以对数组进行布尔运算的操作夫，此类操作符称为逐位运算符(bitwise logic operator)。

逐个运算符包括以下几个：
- &： np.bitwise_and
- |: np.bitwise_or
- ^: np.bitwise_xor
- ~: np.bitwise_not



```python
a = np.arange(20).reshape([4,5])
print("a = \n", a)

print()
print("a中能被3整除或者7整除的数字保留：")
print((a % 3 == 0) | (a % 7 == 0))
```

    a = 
     [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    
    a中能被3整除或者7整除的数字保留：
    [[ True False False  True False]
     [False  True  True False  True]
     [False False  True False  True]
     [ True False False  True False]]


## 将布尔值作为掩码操作

通过组合使用比较类运算，可以快速提取出符合条件的数值，此类操作称为掩码操作。


```python
a = np.random.randint(100, size=(3,5))
print("a = \n", a)
print()

# 掩码可以快速提取数据，比如，提取出小于50的数据
a1 = a[a<50]
print("a1 = ", a1)

print("a1.shape = ", a1.shape)
```

    a = 
     [[45 22 92  1 14]
     [17 90 96  8 61]
     [21 87 69 44 47]]
    
    a1 =  [45 22  1 14 17  8 21 44 47]
    a1.shape =  (9,)


## 通用函数-特性

numpy是为了大量数据运算而生，所以根据大量数据计算的特殊情况，有一些特殊的属性，本节我们做一个简单介绍。

### 指定输出

大量数据运算的临时结果一般放在内存变量中，但有时候可能需要保存中间结果，即把中间结果写入指定位置，此时就需要用到指定输出功能。

所有通用函数都可以带参数out，out即是需要将结果写入的位置。




```python
a = np.arange(10)
b = np.empty(10)

# 此时把中间结果存入b，最终结果存入c
# 此处中间结果和最终结果一致
c = np.multiply(a, 2, out=b)
print("a = ", a)
print("b = ", b)
print("c = ", c)
```

    a =  [0 1 2 3 4 5 6 7 8 9]
    b =  [ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18.]
    c =  [ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18.]


out也可以直接作用于数组的视图，可以直接更改数组内容。

下面的结果，跟直接对b赋值是由区别的：

```
>>> b[::2] = 2 ** a 
```
上面代码会计算结果，将结果放入临时数组作为中间变量保存，最后作为结果复制给b[::2]，但是如果使用out
则把结果直接写入b中，减少资源使用。

虽然就下面案例来讲，并没有节省多少资源，但如果数据量特别大的时候，效果非常明显，有时甚至是必要手段。



```python
# out也可以是一个数组的视图，这样可以直接更改数组内容
a = np.arange(5)
b = np.zeros(10)

np.power(2, a, out=b[::2])

print("a = ", a)
print("b = ", b)

```

    a =  [0 1 2 3 4]
    b =  [ 1.  0.  2.  0.  4.  0.  8.  0. 16.  0.]


### 外积

数组的外积，就是数组对应逐个元素相乘，即获得两个数组所有元素对的乘积，假定数组a1， a2，每个数组10个元素，总共获得的外积应该有 10 x 10 = 100 个元素。


```python
# 外积计算
a = np.arange(1,6)
b = np.arange(10, 15)
print("a = \n", a)

print()
print("b = \n", b)
print()
c = np.multiply.outer(a, b)
print("c = \n", c)
```

    a = 
     [1 2 3 4 5]
    
    b = 
     [10 11 12 13 14]
    
    c = 
     [[10 11 12 13 14]
     [20 22 24 26 28]
     [30 33 36 39 42]
     [40 44 48 52 56]
     [50 55 60 65 70]]
