---
layout: default
title: Numpy数据类型
parent: Numpy
nav_order: 2
---
# Numpy数据类型
- numpy的数据类型和c语言中的数据类型实现并不一样
- 可以理解对基础数据类型的优化和升级
- 一切为了快速处理大型/大量数据为宗旨

## numpy基础数据类型
- bool_: 布尔值，用一个字节存储
- int_： 默认整型，通常是int64/int32
- intc:  整型，通常是int32/int64
- intp:  用作索引的整型，通常是int32/int64
- int8/16/32/64: 整型
- uint8/16/32/64： 无符号整型
- float_: float64的简写
- float16: 半精度浮点型， 1bit符号， 5bits指数，10bits尾数
- float32: 单精度浮点型， 1bit符号，8bits指数，23bits尾数
- float64: 双精度浮点型， 1bit符号，11bits指数，52bits尾数
- complex_: complex128
- complex64: 复数，两个32位浮点数表示
- complex128: 复数， 由两个64位浮点数表示

## numpy的数据类型表示
- 'b': 字节型， np.dtype('b')
- 'i': 有符号整型， np.dtype('i4')就是一个 np.int32类型
- ’u': 无符号整型， np.dtype('u8')就是一个np.uint64
- 'f': 浮点型， np.dtype('f8')
- 'c': 复数浮点型
- ’S': 'a': 字符串， np.dtype('S6')
- 'U': Unicode编码字符串， n'p.dtype('U') 就是np.str_类型
- ‘V': 原生数据， 比如空或者void， np.dtype('V')就是np.void

其中如果出现<则表示低字节序(little endian), 同理>则表示高字节序
