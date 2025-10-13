import re

def fun_1():
    s = "I love wangxiaojing"

    #匹配是否跟wangxiaojing表白过
    rst = re.match("wangxiaojing love", "wangxiaojing love me")

    r = rst.group()
    print(type(r))
    print(r)


def fun_2():
    #匹配任意一个字符
    rst = re.match(".", "9")
    print(rst.group())

    rst = re.match(".", "B")
    print(rst.group())

    rst = re.match("w", "Wang")
    # 匹配为空
    #print(rst.group())


    rst = re.match("[wW]", "wang")
    print(rst.group())

    rst = re.match("[0123456789]", "89years")
    print(rst.group())

    # 匹配两位数字或者一位数字
    rst = re.match("[0123456789]{1,2}", "89years")
    print(rst.group())

    # 匹配至少一位数字
    rst = re.match("[0123456789]+", "809years")
    print(rst.group())


def fun_3():
    '''匹配字符'''
    rst = re.match("[i]+", "i love wangxiaojing")
    print(rst.group())

    rst = re.match("\w+", "i love 3th wangxiaojing")
    print(rst.group())


def fun_4():
    dir = "C:\\a\\b\\c.txt"
    print("DIR={0}".format(dir))

    rst = re.match("C:\\\\a", dir)
    print(rst.group())

    rst = re.match(r"C:\\a", dir)
    print(rst.group())

def fun_5():
    rst = re.match("[1-9]?\d", "9")
    print(rst.group())

    rst = re.match("[1-9]?\d", "19")
    print(rst.group())

    rst = re.match("[1-9]?\d", "09")
    print(rst.group())


    rst = re.match("[1-9]?\d$", "09")
    #匹配为空
    #print(rst.group())

    rst = re.match("[1-9]?\d|\d+$", "09")
    print(rst.group())

    rst = re.match("[1-9]?\d$|\d+$", "09")
    print(rst.group())

    #匹配邮箱
    rst = re.match("\w{4,30}@163\.com", "wangdapeng@163.com" )
    print(rst.group())

    #匹配邮箱
    rst = re.match("\w{4,30}@(163|126|qq)\.com", "wangdapeng@126.com" )
    print(rst.group())


def fun_6():
    s = "i love wangxiaojing and zhangmingmin and lihua"
    #search查找的结果只能是一个
    rst = re.search("o", s)
    print(rst.group())


    rst = re.findall("[oi]", s)
    print(type(rst))
    print(rst)

    rst = re.sub("[oi]", "8", s)
    print(type(rst))
    print(rst)
    print(s)

fun_6()