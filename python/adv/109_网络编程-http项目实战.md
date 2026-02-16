# HTTP项目实战-WebServer 

我们已经学过了HTTP协议和Socket编程，本项目实战的目的是：
- 复习HTTP协议, HTTP协议请参看前面章节
- 复习Socket编程, socket请参看前面章节
- 巩固以前学过的Python编程，提高代码量
- 项目按功能分为几个版本，每个版本独立编码

##  v1
实验目的:`
- 通过socket方式建立WebServer项目，能够正确解析HTTP方式访问并根据访问内容做出正确反馈。 
- 通过实验使学生深刻理解HTTP协议
- 复习前端知识，主要是HTML知识

###  创建项目
- 选择创建一个空python项目
- 添加一个python文件，名称为sw_server.py
- 建立程序主流程，不关注功能
 

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind( ("127.0.0.1", 9999))
        sock.listen() # 参数backlog表明阻塞队列的长度， n+1

        skt,addr = sock.accept()

        lines = getAllLine(skt)
        for line in lines:
            print(line)


        skt.close()
        sock.close()

###  添加处理函数 getLine
- Http访问是按行组织信息
- 程序需要按行读出每一行内容


    def getLine(sock):

        b1 = sock.recv(1)
        b2 = 0
        data = b''

        while  b2 != b'\r' and b1 != b'\n' :
            b2 = b1
            b1 = sock.recv(1)
            if not b1:
                return str(data)
            data += bytes(b2)

        return data.strip(b'\r')

### 添加读取所有输入功能
- 添加函数getAllLine
- 负责读取一次访问socket的多有头信息


    def getAllLine(sock):

        data = b''
        dataList = list()
        data = b''

        while True:
            data = getLine(sock)
            if data:
                dataList.append(data)
            else:
                return dataList
### 添加反馈功能
- 一旦程序接收到信息，需要进行反馈应答
- 程序添加反馈文字，代码如下

        rsp = "hello world"
        byteRsp = rsp.encode('ASCII')
        skt.send(byteRsp)

- 做成函数sendRspLine(sock, data)，同时取消反馈代码，改成对函数的调用

         def sendRspLine(sock, data):
            sock.send(data.encode("ASCII"))
            return None
 
 - 主程序代码如下：
 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind( ("127.0.0.1", 9999))
        sock.listen() # 参数backlog表明阻塞队列的长度， n+1

        skt,addr = sock.accept()

        lines = getAllLine(skt)

        for line in lines:
            print(line)

        hw = "Hello World"
        sendRspLine(skt, hw)

        skt.close()
        sock.close()

###  整理反馈为标准HTTP反馈
- 添加函数，能按行反馈内容
- 整理反馈信息为按照HTTP协议格式反馈


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind( ("127.0.0.1", 9999))
        sock.listen() # 参数backlog表明阻塞队列的长度， n+1

        skt,addr = sock.accept()

        lines = getAllLine(skt)
        for line in lines:
            print(line)

        hw = "Hello World"
        sendRspLine(skt, hw)

        skt.close()
        sock.close()

- 添加完整反馈函数，一次性把整个HTTP返回内容全部反馈，代码如下：

        def sendRspAll(sock, data):

            sendRspLine(sock, "HTTP/1.1 200 OK")

            strRsp = "Content-Length: "
            strRsp += str(len(data))
            sendRspLine(sock, strRsp )

            sendRspLine(sock, "Content-Type: text/html")

            sendRspLine(sock, "")
            sendRspLine(sock, data)
            
- 修改主程序，调用sendRspAll

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind( ("127.0.0.1", 9999))
        sock.listen() # 参数backlog表明阻塞队列的长度， n+1

        skt,addr = sock.accept()

        lines = getAllLine(skt)
        for line in lines:
            print(line)

        hw = "Hello World"
        sendRspAll(skt, hw)

        skt.close()
        sock.close()

###   完整代码
        import socket

        def getLine(sock):

            b1 = sock.recv(1)
            b2 = 0
            data = b''

            while  b2 != b'\r' and b1 != b'\n' :
                b2 = b1
                b1 = sock.recv(1)
                if not b1:
                    return str(data)
                data += bytes(b2)

            return data.strip(b'\r')


        def getAllLine(sock):

            data = b''
            dataList = list()
            data = b''

            while True:
                data = getLine(sock)
                if data:
                    dataList.append(data)
                else:
                    return dataList

        def sendRspLine(sock, data):

            data += "\r\n"
            sock.send(data.encode("ASCII"))
            return None


        def sendRspAll(sock, data):

            sendRspLine(sock, "HTTP/1.1 200 OK")

            strRsp = "Content-Length: "
            strRsp += str(len(data))
            sendRspLine(sock, strRsp )

            sendRspLine(sock, "Content-Type: text/html")

            sendRspLine(sock, "")
            sendRspLine(sock, data)




        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind( ("127.0.0.1", 9999))
        sock.listen() # 参数backlog表明阻塞队列的长度， n+1

        skt,addr = sock.accept()

        lines = getAllLine(skt)
        for line in lines:
            print(line)

        hw = "Hello World"
        sendRspAll(skt, hw)

        skt.close()
        sock.close()


## v2 
### 实验目的
- 利用OOP重构代码，即从新修改代码结构
- 通过重构为以后功能添加做好准备
- 原先代码采用面向过程的方式编写，不利于功能扩展

### 分析
- 对服务器的模拟需要单独使用类， 类名可以定为WebServer
- 这样每次启动服务器只需要在主程序中创建服务器程序的实例并启动就好
- 对传入的每个socket进行单独处理，定义一个专门处理socket的类，类名WebSocketHandler
- 这样理论上讲就可以对每一个传入的的socket链接启动一个实例去处理
- 以后扩展属于哪个类的业务就可以修改哪个类


### WebSever
- 定义启动函数start，用来启动实例
- 初始化需要用户输入IP和port，如果没有需要给出默认值
- 服务器需要为每个请求单独处理（多线程）
- 如果没有学习多线程内容可以直接处理，只不过程序是阻塞方式运行
- 每传入一个socket，需要单独起一个线程处理

### SocketHandler
- 利用初始化函数对函数进行初始化， 因为是处理socket，所以初始化函数可以用
socket当参数
- 把上个例子的代码可以直接拿过来用，修改成私有变量
- 确定函数被多线程调用的入口

###  测试
- 代码完成后进行基本测试
- 浏览器需要显示出反馈信息来

### 完整代码
大致内容如下，源码去麦扣网下载(http://www.mycode.wang)
- webserver.py代码：

        # WebServer.py
        import socket
        import threading

        from sockhandler import SocketHandler

        class WebServer():
            sock = None

            def __init__(self, ip='127.0.0.1', port=7853):
                self.ip = ip
                self.port = port

                self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
                self.sock.bind((self.ip, self.port))
                self.sock.listen(1)
                print("WebServer is started............................")

            def start(self):
                while True:
                    skt, addr = self.sock.accept()

                    if skt:
                        print("Received a socket {0} from {1} ................. ".format(skt.getpeername(), addr))
                        sockHandler = SocketHandler(skt)
                        thr = threading.Thread(target=sockHandler.startHandler , args=( ) )
                        thr.setDaemon(True)
                        thr.start()
                        thr.join()

                        skt.close()
                        print("Socket {0} handling is done............".format(addr))



        if __name__ == '__main__':
            ws = WebServer()
            ws.start()


- sockhandler.py代码

        class SocketHandler:

            def __init__(self, sock):
                self.sock = sock
                self.headInfo = set()

            def startHandler(self):
                self.headHandler()
                self.sendRsp()
                return None

            def headHandler(self):
                self.headInfo = self.__getAllLine()
                print(self.headInfo)
                return None

            def sendRsp(self):
                data = "HELLO WORLD"
                self.__sendRspAll(data)
                return None


            def __getLine(self):

                b1 = self.sock.recv(1)
                b2 = 0
                data = b''

                while  b2 != b'\r' and b1 != b'\n' :
                    b2 = b1
                    b1 = self.sock.recv(1)
                    if not b1:
                        return str(data)
                    data += bytes(b2)

                return data.strip(b'\r')


            def __getAllLine(self):

                data = b''
                dataList = list()
                data = b''

                while True:
                    data = self.__getLine()
                    if data:
                        dataList.append(data)
                    else:
                        return dataList

                return None

            def __sendRspLine(self,data):

                data += "\r\n"
                self.sock.send(data.encode("ASCII"))
                return None


            def __sendRspAll(self, data):

                self.__sendRspLine("HTTP/1.1 200 OK")

                strRsp = "Content-Length: "
                strRsp += str(len(data))
                self.__sendRspLine( strRsp )

                self.__sendRspLine("Content-Type: text/html")

                self.__sendRspLine("")
                self.__sendRspLine(data)
                
## V3                

### 实验目的
- 是程序能够使用配置文件
- 让程序具有更强的可配置性

引入配置文件的概念的原因
- 避免硬编码
- 修改方便
- 部署方便

 配置文件可以使用静态类，json格式，xml格式和专用的cfg格式，此处因为
 课程原因，使用静态类概念引入，配置文件放入类中，直接读取。
 
 实际使用中，建议时候用cfg格式的专用配置文件格式。 

### ServerContent
- 用以存放有关WebServer的相关配置
- 代码如下：
    - 以后对所有关于Sever的配置修改直接修改ServerContent类就好，不需要改动代码


            class ServerContent:
                ip = '127.0.0.1'
                port = 9999


### SocketHandlerContent
- 用于存放SockedtHandler类的一些信息
- 代码如下：


        class SocketHandlerContent:
            head_protocal = "HTTP/1.1 "
            head_code_200 = "200 "
            head_status_OK = "OK"

            head_content_length = "Content-Length: "
            head_content_type = "Content-Type: "
            content_type_html = "text/html"

            blank_line = ""

### 测试代码运行情况
- 使用浏览器访问IP+端口
- 代码需要能准确返回HELLO WORLD

###  sockethandler 代码

        from sockethandlercontent import SocketHandlerContent

        class SocketHandler:

            def __init__(self, sock):
                self.sock = sock
                self.headInfo = set()

            def startHandler(self):
                self.headHandler()
                self.sendRsp()
                return None

            def headHandler(self):
                self.headInfo = self.__getAllLine()
                print(self.headInfo)
                return None

            def sendRsp(self):
                data = "HELLO WORLD"
                self.__sendRspAll(data)
                return None

        #####################################3

            def __getLine(self):

                b1 = self.sock.recv(1)
                b2 = 0
                data = b''

                while  b2 != b'\r' and b1 != b'\n' :
                    b2 = b1
                    b1 = self.sock.recv(1)
                    if not b1:
                        return str(data)
                    data += bytes(b2)

                return data.strip(b'\r')


            def __getAllLine(self):

                data = b''
                dataList = list()
                data = b''

                while True:
                    data = self.__getLine()
                    if data:
                        dataList.append(data)
                    else:
                        return dataList

                return None

            def __sendRspLine(self,data):

                data += "\r\n"
                self.sock.send(data.encode("ASCII"))
                return None


            def __sendRspAll(self, data):

                self.__sendRspLine(SocketHandlerContent.head_protocal +
                                   SocketHandlerContent.head_code_200 +
                                   SocketHandlerContent.head_status_OK)

                strRsp = SocketHandlerContent.head_content_length
                strRsp += str(len(data))
                self.__sendRspLine( strRsp )

                self.__sendRspLine(SocketHandlerContent.head_content_type +
                                   SocketHandlerContent.content_type_html)


                self.__sendRspLine( SocketHandlerContent.blank_line)
                self.__sendRspLine(data)

### webserver代码

        import socket
        import threading

        # 导入需要用到的类信息
        from sockhandler import SocketHandler
        from servercontent import ServerContent

        class WebServer():
            sock = None

            def __init__(self, ip='127.0.0.1', port=7853):
                self.ip = ip
                self.port = port

                self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
                self.sock.bind((self.ip, self.port))
                self.sock.listen(1)
                print("WebServer is started............................")

            def start(self):
                while True:
                    skt, addr = self.sock.accept()

                    if skt:
                        print("Received a socket {0} from {1} ................. ".format(skt.getpeername(), addr))
                        sockHandler = SocketHandler(skt)
                        thr = threading.Thread(target=sockHandler.startHandler , args=( ) )
                        thr.setDaemon(True)
                        thr.start()
                        thr.join()

                        skt.close()
                        print("Socket {0} handling is done............".format(addr))




        if __name__ == '__main__':
            ws = WebServer( ip=ServerContent.ip, port=ServerContent.port)
            ws.start()

## V4

### 实验目的
- 增加静态页返回功能，用户的访问返回欢迎界面
- 欢迎页面为制作好的静态HTML页面

### 制作返回页面
- 利用html知识制作返回页面
- 静态页面放入webapp中

### 修改SocketHandler
- 修改SocketHandler，添加返回页面功能sendWebPage
- 读取文件的过程中需要利用配置信息
- 代码如下:

        def sendWebPage(self, path):
            fp =  os.path.join(SocketHandlerContent.base_path, path)
            with open(fp,mode='r') as f:
                html = f.read()
                self.__sendRspAll(html)

## V5

### 实验目的
- 增加路由功能，路由即根据不同的访问URL和访问方法，调用不停的处理函数的模块
- 增加对静态文件的支持, 静态文件即服务器上一些图片，不需要经常更改的文件内容

### 路由功能
- 路由即根据不同的访问URL和访问方法，调用不停的处理函数的模块
- 增加路由功能需要先对http协议头进行分析，分析出对方请求的文件路径
- 需要修改对http传入信息的读取功能，将所有传入请求信息分析后存入数据结构
- 修改后代码如下：


        def headHandler(self):
            tmpHead = self.__getAllLine()
            for line in tmpHead:
                if  ":" in line:
                    infos = line.split(": ")
                    self.headInfo[infos[0]] = infos[1]
                else:
                    infos = line.split(" ")
                    self.headInfo["protocal"] = infos[2]
                    self.headInfo["method"] = infos[0]
                    self.headInfo["uri"] = infos[1]

            return None

- 增加函数reqRoute,对传入请求添加简单路由功能
- 代码如下：

        def startHandler(self):
            self.headHandler()
            self.reqRoute()
            return None

        def reqRoute(self):

            uri = self.headInfo.get("uri","BadReq")
            if uri == "/":
                self.sendWebPage("index.html")
            
            return None

###  增加对静态ico的处理
- 由于浏览器的固定设置，每次请求完资源后会发送一个对favicon.ico的请求
- favicon.icom即本网站的小图标
- 根据需要，需要增加静态文件favicon.ico 
- 在主目录下建立static文件夹，放入favicon.ico
- 路由模块中添加sendStaticIco
- 会出现错误：

        pytException in thread Thread-12:
        Traceback (most recent call last):
          File "/home/augsnano/anaconda3/envs/pWS/lib/python3.5/threading.py", line 914, in _bootstrap_inner
            self.run()
          File "/home/augsnano/anaconda3/envs/pWS/lib/python3.5/threading.py", line 862, in run
            self._target(*self._args, **self._kwargs)
          File "/home/augsnano/workspace/WS/V5/sockhandler.py", line 13, in startHandler
            self.reqRoute()
          File "/home/augsnano/workspace/WS/V5/sockhandler.py", line 22, in reqRoute
            self.sendStaticIco("favicon.ico")
          File "/home/augsnano/workspace/WS/V5/sockhandler.py", line 52, in sendStaticIco
            ico = f.read()
          File "/home/augsnano/anaconda3/envs/pWS/lib/python3.5/codecs.py", line 321, in decode
            (result, consumed) = self._buffer_decode(data, self.errors, final)
        UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start bytehon


- 解决方案：
    1. 打开文件以 rb形式打开
    2. 发送内容的时候不需要编码，直接发送
    3. 内容不需要附加'\r\n'结尾字符

- 代码如下：


        def reqRoute(self):

            uri = self.headInfo.get("uri","BadReq")
            if uri == "/":
                self.sendWebPage("index.html")
            if uri == "/favicon.ico":
                self.sendStaticIco("favicon.ico")

            return None


        def sendStaticIco(self, path):
            fp =  os.path.join(SocketHandlerContent.base_path, "static", path)
            with open(fp,mode='rb') as f:
                ico = f.read()
                self.__sendRspAll(ico, SocketHandlerContent.content_type_ico)

        def __sendRspLine(self,data):

            if type(data) == bytes:
                self.sock.send(data)
            else:
                data += "\r\n"
                self.sock.send(data.encode("utf-8"))
            return None

## V6
### 实验目的
- 理解相应的返回代码的含义
- 添加404反馈, 即当用户访问不存在的资源的时候，返回404页面
- 添加500反馈, 即当服务器内部崩溃的时候，返回500页面报错

### 修改结构和相应代码
- 创建文件夹web
- 所有html网页放入web文件夹下
- 修改相应reqRoute代码
- 代码修改后如下：


        def reqRoute(self):

            uri = self.headInfo.get("uri","BadReq")

            if uri == "/":
                self.sendWebPage("web/index.html")
            if uri == "/favicon.ico":
                self.sendStaticIco("static/favicon.ico")
            if uri == "/index.html":
                self.sendWebPage("web/index.html")

            return None
            
- 修改相应的sendWebPage 和 sendStaticIco 代码
- 测试修改后运行情况

### 添加404反馈
- 制作404 静态网页并放入web文件夹
- 修改路由函数，如果访问资源不存在就返回404页面
- 代码如下：


        def reqRoute(self):

            uri = self.headInfo.get("uri", "BadReq")

            htmlUri = os.path.join(SocketHandlerContent.base_path, "web", uri)
            icoUri = os.path.join( SocketHandlerContent.base_path, "static", uri)

            if not os.path.exists(htmlUri) and not os.path.exists(icoUri):
                print('ERROR')
                self.sendWebPage("web/404.html")

            if uri == "/":
                self.sendWebPage("web/index.html")
            if uri == "/favicon.ico":
                self.sendStaticIco("static/favicon.ico")
            if uri == "/index.html":
                self.sendWebPage("web/index.html")

            return None

### 添加505反馈
- 添加505页面
- 异常处理中添加505反馈
- 示例只采用一个异常处理
- 代码如下：


        def reqRoute(self):

            try:
                uri = self.headInfo['uri']
                #uri = self.headInfo.get("uri")
            except Exception:
                self.sendWebPage(SocketHandlerContent.file_500)
                return None

            htmlUri = os.path.join(SocketHandlerContent.base_path, "web", uri)
            icoUri = os.path.join( SocketHandlerContent.base_path, "static", uri)

            if not os.path.exists(htmlUri) and not os.path.exists(icoUri):
                self.sendWebPage(SocketHandlerContent.file_404)

            if uri == "/":
                self.sendWebPage(SocketHandlerContent.file_index)
            if uri == "/favicon.ico":
                self.sendStaticIco(SocketHandlerContent.file_ico)
            if uri == "/index.html":
                self.sendWebPage(SocketHandlerContent.file_index)

            return None

### 添加特殊返回时的返回头信息
- 404,500等特殊的返回，需要更改返回代码为404,500
- 重构函数 sendWebPage
- 重构函数 sendRspAll
- 代码如下：



        def sendWebPage(self, path, code="200"):
            fp =  os.path.join(SocketHandlerContent.base_path, path)
            with open(fp,mode='r') as f:
                html = f.read()
                self.__sendRspAll(html, code=code)
                
        def __sendRspAll(self,
                         data,
                         content_type = SocketHandlerContent.content_type_html,
                         code="200"):

            if code == "404":
                self.__sendRspLine(SocketHandlerContent.head_protocal +
                                   SocketHandlerContent.head_code_404 +
                                   SocketHandlerContent.head_status_NOTFOUND)
            if code == "500":
                self.__sendRspLine(SocketHandlerContent.head_protocal +
                                   SocketHandlerContent.head_code_500 +
                                   SocketHandlerContent.head_status_INTERNAL_ERROR)
            if code == "200":
                self.__sendRspLine(SocketHandlerContent.head_protocal +
                                   SocketHandlerContent.head_code_200 +
                                   SocketHandlerContent.head_status_OK)

            strRsp = SocketHandlerContent.head_content_length
            strRsp += str(len(data))
            self.__sendRspLine( strRsp )

            self.__sendRspLine(SocketHandlerContent.head_content_type +
                               content_type)


            self.__sendRspLine( SocketHandlerContent.blank_line)
            self.__sendRspLine(data)