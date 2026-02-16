---
layout: default
title: JSON
parent: Python编程
nav_order: 27
---

# JSON

- 在线工具
    - https://www.sojson.com/
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html

- JSON (JavaScript Object Notation)
- 轻量级的数据交换格式，基于 ECMAScript 的子集
- JSON 格式是一个键值对形式的数据集：
    - Key：字符串
    - Value：字符串、数字、列表、JSON 格式
    - JSON 用大括号包裹
    - 键值对之间用逗号隔开

示例：

```json
{
    "name": "wangdapeng",
    "age": 18,
    "mobile": "13260446055"
}
```

- JSON 和 Python 格式的对应关系：
    - 字符串：字符串
    - 数字：数字
    - 队列：list
    - 对象：dict
    - 布尔值：布尔值
- Python for JSON
    - 有 json 包
    - `json.dumps()`: 负责对数据编码
    - `json.loads()`: 负责对数据解码
    - 案例01

```python
'''
student={
    "name": "wangdapeng",
    "age": 18,
    "mobile":"13260446055"
}
'''

import json

# 此时student是一个dict格式内容，不是json
student={
    "name": "luidana",
    "age": 18,
    "mobile":"15578875040"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)
```

- `json.dump` 和 `json.load`，从文件读取

```python
import json

data = {"name":"hahah", "age":12}
with open("t.json", 'w') as f:
    json.dump(data, f)

with open("t.json", 'r') as f:
    d = json.load(f)
    print(d)
```

