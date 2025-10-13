
from collections import OrderedDict

a = {"banana":3,"apple":2,"pear":1,"orange":4}
print(a)
# dict sorted by key, 每个 (k,v)中按 k排序
b = OrderedDict(sorted(a.items(),key = lambda t:t[0]))
print(b)

# dict sorted by value
# 每个 (k,v)中按 v排序
c = OrderedDict(sorted(a.items(),key = lambda t:t[1]))
print(c)

# 按k的长度排序
d =  OrderedDict(sorted(a.items(),key = lambda t:len(t[0])))
del d['apple']
print(d)

d["apple"] = 2
print(d)