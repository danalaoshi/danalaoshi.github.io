#
# - `issubclass`:检测一个类是否是另一个类的子类
# - `isinstance`:检测一个对象是否是一个类的实例
# - `hasattr`:检测一个对象是否由成员xxx
# - `getattr`: get attribute
# - `setattr`: set attribute
# - `delattr`: delete attribute
# - `dir`: 获取对象的成员列表

class A():
    pass

class B(A):

    def __init__(self):
        self.name = "刘大拿"
        self.tel = '131 191 44223'
        self.qq_group = "9990960"

    def say(self):
        print("Hello ......")


# 第一个参数是判断的类名, 第二个参数是可能的父类组成的tuple`
print("B是A的子类: ", issubclass(B, (A, )))

b = B()
print('b是B的实例:', isinstance(b, B))

# 第二个参数字符串形式的属性名称
print("B是否具有属性say:", hasattr(b, "say"))

# 利用字符串得到某个具体的函数或者功能
# 这个在系统级别的代码中常用
say = getattr(b, "say")
# 注意这个调动方式, say必须要求有一个参数,但此时这个函数代表的是b实例的函数say,此种方式调用照样默认传入b作为第一个参数
say()

# 给实例或者类设置内容
b = B()
# 给实例b设置一个属性age
setattr(b, "age", 18)
print(b.age)

def sayage(self, age):
    print("AGE.......", age)

# 同样可以把函数设置给b,但此时这个函数不作为b的实例函数, 调用的时候也不默认把自身当做第一个参数传入
setattr(b, "sayage", sayage)
b.sayage(b, 23)

#  显示类,实例所有可用内容,属性
print(dir(b))

print(dir(B))