import dbm
help(dbm
# 文件
- 长久保存信息的一种数据信息集合
- 常用操作
    - 打开关闭（文件一旦打开，需要关闭操作）
    - 读写内容
    - 查找
# open函数
- open函数负责打开文件，带有很多参数
- 第一个参数： 必须有，文件的路径和名称
- mode：表明文件用什么方式打开
    - r:以只读方式打开
    - w：写方式打开，会覆盖以前的内容
    - x：创建方式打开，如文件已经存在，报错
    - a：append方式，以追加的方式对文件内容进行写入
    - b： binary方式，二进制方式写入
    - t： 文本方式打开
    - +： 可读写


```python
# 打开文件，用写的方式
# r表示后面字符串内容不需要转义
# f称之为文件句柄
f = open(r"test01.txt", 'w')
# 文件打开后必须关闭
f.close()

# 此案例说明，以写方式打开文件，默认是如果没有文件，则创建
```

# with语句
- with语句使用的技术是一种成为上下文管理协议的技术(ContextManagementProtocal)
- 自动判断文件的 作用域， 自动关闭不在使用的打开的文件句柄


```python
# with语句案例

with open(r"test01.txt", 'r') as f:
    pass
    # 下面语句块开始对文件f进行操作
    # 在本模块中不需要在使用close关闭文件f
```


```python
# with案例

with open(r'test01.txt', 'r') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件知道结束
    while strline:
        print(strline)
        strline = f.readline()
```

    假若他日相逢

    我将何以贺你

    以沉默

    以眼泪



```python
# list能用打开的文件作为参数，把文件内每一行内容作为一个元素

with open(r'test01.txt', 'r') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)
```

    假若他日相逢

    我将何以贺你

    以沉默

    以眼泪



```python
# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有制定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符

with open(r'test01.txt', 'r') as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)

# 作业：
# 使用read读取文件，每次读取一个，使用循环读完
# 尽量保持格式
```

    1
    假


# seek（offset， from)
- 移动文件的读取位置，也叫读取指针
- from的取值范围：
    - 0： 从文件头开始偏移
    - 1：从文件当前位置开始偏移
    - 2： 从文件末尾开始偏移
- 移动的单位是字节(byte)
- 一个汉子由若干个字节构成
- 返回文件只针对 当前位置


```python
# seek案例
# 打开文件后，从第5个字节出开始读取

# 打开读写指针在0处， 即文件的开头
with open(r'test01.txt', 'r') as f:
    # seek移动单位是字节
    f.seek(6, 0)
    strChar = f.read()
    print(strChar)
```

    他日相逢
    我将何以贺你
    以沉默
    以眼泪



```python
# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟

# 让程序暂停，可以使用time下的sleep函数
import time

with open(r'test01.txt', 'r') as f:
    # read参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        # sleep参数单位是秒
        time.sleep(1)
        strChar = f.read(3)
# 作业：
# 解释以下运行结果，为什么不是每行三个字符
```

    假若他
    日相逢

    我将
    何以贺
    你
    以
    沉默

    以眼泪



```python
# tell函数： 用来显示文件读写指针的当前位置
with open(r'test01.txt', 'r') as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()

# 以下结果说明：
# tell的返回数字的单位是byte
# read是以字符为单位
```

    9
    假若他
    18
    日相逢
    25

    我将
    34
    何以贺
    41
    你
    以
    48
    沉默

    57
    以眼泪


# 文件的写操作-write
- write(str): 把字符串写入文件
- writeline(str): 把字符串按行写入文件
- 区别：
    - write函数参数只能是字符串
    - writerline参数可以是字符串，也可以是字符序列


```python
# write 案例
# 1. 向文件追加一句诗

# a代表追加方式打开
with open(r'test01.txt', 'a') as f:
    # 注意字符串内含有换行符
    f.write("生活不仅有眼前的苟且， \n 还有远方的苟且")

```


```python
# 可以直接写入行， 用writelines
# writelines表示写入很多行，参数可以是list格式

# a代表追加方式打开
with open(r'test01.txt', 'a') as f:
    # 注意字符串内含有换行符
    f.writelines("生活不仅有眼前的苟且")
    f.writelines("还有远方的枸杞")

```


```python
l = ["I", "love", "wangxiaojing"]

# a代表追加方式打开
with open(r'test01.txt', 'w') as f:
    # 注意字符串内含有换行符
    f.writelines(l)

```

# 持久化 - pickle
- 序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
- 反序列化： 序列号的逆过程
- pickle： python提供的序列化模块
- pickle.dump:序列化
- pickle.load:反序列化


```python
# 序列化案例
import pickle

age = 19

with open(r'test01.txt', 'wb') as f:
    pickle.dump(age, f)
```


```python
# 反序列化案例

import pickle

with open(r'test01.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)
```

    19



```python
# 序列化案例
import pickle

a = [19, 'liudana', "i love wangxiaojing", [185, 76]]

with open(r'test01.txt', 'wb') as f:
    pickle.dump(a, f)
```


```python

with open(r'test01.txt', 'rb') as f:
    a  = pickle.load(f)
    print(a)
```

    [19, 'liudana', 'i love wangxiaojing', [185, 76]]


# 持久化-shelve
- 持久化工具
- 类似字典，用kv对保存数据，存取方式跟字典也类似
- open, close


```python
# 使用shelve创建文件并使用
import shelve

# 打开文件
# shv相当于一个字典
shv = shelve.open(r'shv.db')

shv['one'] = 1
shv['two'] = 2
shv['three'] = 3

shv.close()

# 通过以上案例发现，shelve自动创建的不仅仅是一个shv.db文件，还包括其他格式文件
```


```python
# shelve读取案例
shv = shelve.open(r'shv.db')

try:
    print(shv['one'])
    print(shv['threee'])
except Exception as e:
    print("烦死了")
finally:
    shv.close()
```

    1
    烦死了


# shelve特性
- 不支持多个应用并行写入
    - 为了解决这个问题，open的时候可以使用flag=r
- 写回问题
    - shelv恶魔人情况下不会等待持久化对象进行任何修改
    - 解决方法： 强制写回：writeback=True


```python
# shelve 之只读打开
import shelve

shv = shelve.open(r'shv.db', flag='r')

try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()


```

    1



```python
import shelve



shv = shelve.open(r'shv.db')
try:
    shv['one'] = {"eins":1, "zwei":2, "drei":3}
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()


```

    {'eins': 1, 'zwei': 2, 'drei': 3}



```python
# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] =100
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
```

    {'eins': 1, 'zwei': 2, 'drei': 3}
    {'eins': 1, 'zwei': 2, 'drei': 3}



```python
# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db', writeback=True)
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] =100
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
```

    {'eins': 1, 'zwei': 2, 'drei': 3}
    {'eins': 100, 'zwei': 2, 'drei': 3}



```python
# shelve 使用with管理上下文环境

with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] =1000



with shelve.open(r'shv.db') as shv:
    print(shv['one'])
```

    {'eins': 100, 'zwei': 2, 'drei': 3}
    {'eins': 1000, 'zwei': 2, 'drei': 3}



```python

```
)