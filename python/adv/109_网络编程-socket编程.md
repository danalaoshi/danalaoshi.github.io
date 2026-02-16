---
layout: default
title: 网络编程-socket编程
parent: Python编程
nav_order: 32
---
# Socket 编程

socket 编程相关的模块是 socket，所以在使用 socket 编程的时候，需要导入 socket 模块：

```python
import socket
```

## socket 编程概述

socket 编程属于传输层编程，主要研究的是两台机器如何发送基本字符或者字节流信息，或者可以理解成，socket 编程研究的是如何一个字节一个字节的把信息传输给对方，而此时双方并不关心每一个字节具体的含义，反正我发过去就完了。而一旦发送完毕，你发送的内容到底是啥意思，发送者的意图等，属于 HTTP 协议的范围，HTTP 协议属于应用层协议，默认两台机器能顺利发送完整有序的字符信息。

一个不太恰当的例子，socket 编程相当于快递公司，它只负责把货物安全按时发到制定人员，如果你发送的是一堆货物，则货物可能分不同的批次车次运输到对方，而具体如何运输，发货方其实没必要知道。但一旦发送到对方手中，货物的使用方式、作用和价值等等，属于取决于收货方，跟快递公司无关，此处收货方发货收货双方可以认为是 HTTP 协议。

- TCP/IP 协议族
    - TCP（传输控制协议，Transmission Control Protocol）
        - 基于链接的，每次传输数据都要建立链接
        - 建立链接需要消耗资源、带宽等，需要消耗时间
        - 传输数据安全、可靠，数据传输有序
    - UDP（用户数据报协议，User Datagram Protocol）
        - 无连接
        - 安全性差，数据接受无顺序
        - 传输消耗带宽小，没有专门链接需要消耗资源
    - 可以把 TCP 理解成挂号信，我们的信用卡法律文书等重要文件，如果邮寄需要发送挂号信，此时信件的邮寄过程中实时信息更新，可查可追溯，所以安全。
    - UDP 则相当于普通信件，我们邮寄平信的时候，只要把信件交给快递员就好了，至于信件能不能送到、何时送到，没有保障，也不能查看。

- socket：套接字，在网络里边，特指通过 IP 地址和端口进行通信的一种机制
- IP 地址：用来唯一标示网络中的设备地址，通过 IP 地址可以找到网络中任何一台设备
- 端口：
    - 进行应用程序身份鉴定的一个数字，一台机器可能有很多程序，每台程序进行网络通信都要有自己的特定的端口号
    - 理论上数值是 0-65535 之间
    - 一般 1000 以下不推荐开发者自行使用
    
## UDP 编程

在开始编程之前我们需要先看几个概念：

- 无连接：
    UDP 是没有链接的编程，即发送数据只要有 IP 和端口号就发送，至于对方能不能接受，端口和 IP 是否正确不在考虑范围之内。

- 客户端 (Client) 和 服务器端 (Server)：
    我们以前的编程都是一个程序，因为我们需要模拟通信过程，也就是需要有至少两方参与，我们习惯把发起通信的一方称为客户端 (Client)，把另一方称为服务器端 (Server)。在我们进行 socket 编程的时候，要想让程序跑起来，一般我们需要写两个程序，然后分别运行。

- Server 端流程
    1. 建立 socket，socket 是负责具体通信的一个实例

        ```python
        # 建立socket，负责跟对方进行通信
        # socket初始化需要两个参数
        # 1. AF_INET:指定socket编程使用IPv4协议族
        # 2. SOCK_DGRAM:指定通信方式为UDP方式
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ```

    2. 绑定，为创建的 socket 指派固定的端口和 IP 地址

        ```python
        # 绑定ip和端口
        # 127.0.0.1 这个地址代表的是机器本身
        # 7777：端口，负责指定服务器上的对应的应用
        # 端口随机指定，一般大于1000小于65535
        # 所谓端口地址，是一个有字符串和整数组成的元组
        # 注意bind函数的参数只有一个tuple
        sock.bind(("127.0.0.1", 7777))
        ```

    3. 接受对方发送内容

        ```python
        # 接收数据
        # 如果对方不发送或者还没发送数据，则服务器端只能等待
        # recvfrom接收的返回值是一个元组形式，前一个选项是数据，后一个选项是对方的地址
        # 参数的含义是缓冲区的大小
        data, addr = sock.recvfrom(500)
        
        # 发送的数据信息只能是bytes格式
        # 要想让信息显示出来，一般需要进行解码操作
        text = data.decode()
        print(type(text))
        ```

    4. 给对方发送反馈，此步骤为非必须步骤

        ```python
        # 需要给client发送反馈信息，此步骤为非必须项
        rsp = "I have received your msg"
        # 发送的数据格式要求是一个字节串
        # 由字符串得到字节串需要进行编码操作
        data = rsp.encode()
        # 发送数据给对方
        sock.sendto(data, addr)
        ```

- Client 端流程
    1. 建立通信的 socket 实例

        ```python
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ```

    2. 发送内容到指定服务器

        ```python
        text = "I love wangxiaojing"
        # 发送的数据只能是bytes格式
        # str格式数据要想转换成bytes格式需要编码
        data = text.encode()
        # 特别注意地址信息的格式
        sock.sendto(data, ("127.0.0.1", 7777))
        ```

    3. 接受服务器给定的反馈内容，如果期待对方回复的话。

        ```python
        # 如果对方没有反馈，此函数会一直等待
        # data是一个bytes格式的内容
        data, addr = sock.recvfrom(1000)
        
        # bytes格式内容转换成字符串需要进行解码
        text = data.decode()
        
        print(text)
        ```

整个通信过程如下图所示：

![UDP 通信过程](pic/01_01_010.png)

代码如下（代码分服 server 端和客户端两个文件）：

```python
'''
Server端流程
 1. 建立socket，socket是负责具体通信的一个实例
 2. 绑定，为创建的socket指派固定的端口和ip地址
 3. 接受对方发送内容
 4. 给对方发送反馈，此步骤为非必须步骤
'''

# 服务端代码 
# socket模块负责socket编程
import socket

# 模拟服务器的函数
def serverFunc():
    # 1. 建立socket

    # socket.AF_INET:使用ipv4协议族
    # socket.SOCK_DGRAM: 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定ip和port
    # 127.0.0.1: 这个ip地址代表的是机器本身
    # 7852： 随手指定的端口号
    # 地址是一个tuple类型，(ip, port)
    addr = ("127.0.0.1", 7852 )
    sock.bind( addr )


    # 接受对方消息
    # 等待方式为死等， 没有其他可能性
    # recvfrom接受的返回值是一个tuple，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    # rst = sock.recvfrom(500)
    data, addr = sock.recvfrom(500)

    print(data)
    print(type(data))

    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = data.decode()
    print(type(text))
    print(text)


    # 给对方返回的消息
    rsp = "Ich hab keine Hunge"

    # 发送的数据需要编码成bytes格式
    # 默认是utf8
    data = rsp.encode()
    sock.sendto(data, addr)


if __name__ == '__main__':
    print("Starting server.........")
    serverFunc()
    print("Ending server........")



'''
- Client端流程
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
'''
# 客户端代码
import socket
def clientFunc():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    text = "I love jingjing"

    # 发送的数据必须是bytes格式
    data = text.encode()

    # 发送
    sock.sendto(data,  ("127.0.0.1", 7852))


    data, addr  = sock.recvfrom(200)

    data = data.decode()

    print(data)


if __name__ == '__main__':
    clientFunc()
```

关于上述代码，有几个说明需要再提一下：

- 源代码案例 01 是服务器，02 是客户端
- 启动的时候需要先启动服务端程序，这样客户端发送数据才不会报错
- 传输的数据是 bytes 格式，发送端需要先编码，由 str 转换成 bytes，接收端需要接收后解码，由 bytes 格式转换成 str
- 原则上服务器程序要求永久运行，需要用死循环实现，具体实现参考源代码案例 03

## TCP 编程

TCP 编程是面向链接的传输，即每次传输之前需要先建立一个链接。同样在编写程序的时候，客户端和服务器端两个程序需要编写。大致过程和方法跟 UDP 编程相似，只不过：

- 增加了传输的时候建立/关闭链接的过程
- 建立 socket 实例的时候使用参数不同
- 接收/发送函数名称不同

- Server 端的编写流程
    1. 建立 socket 负责具体通信，这个 socket 其实只负责接受对方的请求，真正通信的是链接后从新建立的 socket

        ```python
        # 1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
        # 需要用到两个参数
        # AF_INET: 含义同udp一致
        # SOCK_STREAM: 表明是使用的tcp进行通信
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ```

    2. 绑定端口和地址

        ```python
        # 2. 绑定端口和地址
        # 此地址信息是一个元祖类型内容，元祖分两部分，第一部分为字符串，代表ip，第二部分为端口，是一个整数，推荐大于10000
        addr = ("127.0.0.1", 8998)
        sock.bind(addr)
        ```

    3. 监听接入的访问 socket，此过程可以理解成是等待客户端发起连接

        ```python
        # 3. 监听接入的访问socket
        sock.listen()
        ```

    4. 接受访问的 socket，可以理解接受访问即建立了一个通讯的链接通路

        ```python
        # 4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
        # accept返回的元祖第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()
        ```

    5. 接受对方的发送内容，利用接收到的 socket 接收内容，同 UDP 一样，发送的信息只能是 bytes 格式，所以需要进行解码编码操作。

        ```python
        # 5. 接受对方的发送内容，利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        #msg = skt.receive(500)
        msg = skt.recv(500)
        # 接受到的是bytes格式内容
        # 想得到str格式的，需要进行解码
        msg = msg.decode()
        ```

    6. 如果有必要，给对方发送反馈信息。需要注意的是，此时的发送反馈不需要填写客户端地址，因为发送反馈是按照已经建立好的链接发送的，即已经知道对方的地址。

        ```python
        # 6. 如果有必要，给对方发送反馈信息
        skt.send(rst.encode())
        ```

    7. 关闭链接通路

        ```python
        # 7. 关闭链接通路
        skt.close()
        ```

    8. 参看案例代码 04

        ```python
        import socket
        def tcp_srv():
            # 1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
            # 需要用到两个参数
            # AF_INET: 含义同udp一致
            # SOCK_STREAM: 表明是使用的tcp进行通信
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 2. 绑定端口和地址
            # 此地址信息是一个元祖类型内容，元祖分两部分，第一部分为字符串，代表ip，第二部分为端口，是一个整数，推荐大于10000
            addr = ("127.0.0.1", 8998)
            sock.bind(addr)
            # 3. 监听接入的访问socket
            sock.listen()

            while True:
                # 4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
                # accept返回的元祖第一个元素赋值给skt，第二个赋值给addr
                skt,addr = sock.accept()
                # 5. 接受对方的发送内容，利用接收到的socket接收内容
                # 500代表接收使用的buffersize
                #msg = skt.receive(500)
                msg = skt.recv(500)
                # 接受到的是bytes格式内容
                # 想得到str格式的，需要进行解码
                msg = msg.decode()

                rst = "Received msg: {0} from {1}".format(msg, addr)
                print(rst)
                # 6. 如果有必要，给对方发送反馈信息
                skt.send(rst.encode())

                # 7. 关闭链接通路
                skt.close()


        if __name__ == "__main__":
            print("Starting tcp server.......")
            tcp_srv()
            print("Ending tcp server.......")
        ```

- Client 端流程
    1. 建立通信 socket

        ```python
        # 1. 建立通信socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ```

    2. 链接对方，请求跟对方建立通路。实际使用当中，需要确保连接建立成功后才能发送数据。

        ```python
        # 2. 链接对方，请求跟对方建立通路
        addr = ("127.0.0.1", 8998)
        sock.connect(addr)
        ```

    3. 发送内容到对方服务器

        ```python
        # 3. 发送内容到对方服务器
        msg = "I love wangxiaojing"
        sock.send(msg.encode())
        ```

    4. 接受对方的反馈，当然前提是确保对方有反馈发回，否则会无限期等待。

        ```python
        # 4. 接受对方的反馈
        rst =  sock.recv(500)
        print(rst.decode())
        ```

    5. 关闭链接通路

        ```python
        # 5. 关闭链接通路
        sock.close()
        ```

    6. 参看案例代码 05

        ```python
        import socket
        def tcp_clt():
            # 1. 建立通信socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 2. 链接对方，请求跟对方建立通路
            addr = ("127.0.0.1", 8998)
            sock.connect(addr)
            # 3. 发送内容到对方服务器
            msg = "I love wangxiaojing"
            sock.send(msg.encode())
            # 4. 接受对方的反馈
            rst =  sock.recv(500)
            print(rst.decode())
            # 5. 关闭链接通路
            sock.close()


        if __name__ == "__main__":
            tcp_clt()
        ```

整个通信过程如下图所示：

![UDP 通信过程](pic/01_01_011.png)

socket 编程相对比较简单，在我们很多不太需要表示层参与的地方，比如物联网中，经常对一些简单消息直接用 socket 发送即可，因为信息数量少，有时候可能并不是太重要，直接采用 UDP 发送节省资源。UDP 编程还有一个常用的应用场景就是即时通信，即时通信需要长时间高频炉发送数据，但相对来讲信息重要性相对较低，此时采用 UDP 比较合适。
