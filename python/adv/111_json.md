# JSON

    - 在线工具
        - https://www.sojson.com/
        - http://www.w3school.com.cn/json/
        - http://www.runoob.com/json/json-tutorial.html
    - JSON(JavaScriptObjectNotation)
    - 轻量级的数据交换格式，基于ECMAScript的自己
    - json格式是一个键值对形式的数据集，
        - Key：字符串
        - Value: 字符串，数字，列表，json格式
        - json有大括号包裹
        - 键值对之间用逗号隔开
        
        
            student={
                "name": "wangdapeng",
                "age": 18,
                "mobile":"13260446055“
                }
                
    - json和python格式的对应
        - 字符串：字符串
        - 数字：数字
        - 队列：list
        - 对象：dict
        - 布尔值：布尔值
    - Python for json
        - 有json包
        - josn.dumps():负责对数据编码
        - json.loads():负责对数据解码 
        - 案例01
        - json.dump 和 json.load，从文件读取
