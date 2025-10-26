# Tkinter

一般来讲这种图形化编程属于CS软件结构的产物，现在很少用了，即便是使用也有一些很优秀的解决方案，比如
Electron，QT等，我们之所以介绍Tkinter是希望大家能了解GUI的编程原理，同时对前面知识是一个综合巩固。

## Tkinter简介

对Tkinter进行简单的介绍下。

###  GUI
图形用户界面（Graphical User Interface，简称GUI，又称图形用户接口）是指采用图形方式显示的计算机操作用户界面。

作为一个图形化显示，几乎每种语言都用基于本语言的解决显示解决方案，对于Python来讲，常见的GUI框架有
Tkinter, wxPython,PyQT,PyGame, Turtle等，每个框架都有自己的特点，但使用原理都差不太多，我们
这里以Tkinter为例进行介绍。

至于为什么要用Tkinter作为案例，因为... ...我只会这个呀！

### 常见基于Python的GUI框架介绍
#### Tkinter

`Tkinter`是绑定了`Python`的`TK GUI`工具集，是`Python`包装的`Tcl`(ToolCommandLanguage)代码，通过内嵌的`Python`解释器调用`Tcl`
解释器实现，`Tkinter`的调用转换成`Tcl`命令，然后交给`Tcl`解释器进行解释，实现`Python`的`GUI`界面.

`Tkinter`的优点:
- 历史最悠久
- 是`Python`事实上的标准`GUI`
- `Python`使用`TK GUI` 工具集的标准借口，已经包括在标准Python Window中,跨平台性能好
- 使用简单，学习曲线低
- 轻量级

`Tkinter`的缺点：　
- 做出来的产品比较吃藕 
- 功能简单 
- 对于`Ｃ＋＋`效率不高

####　PyGTK

`PyGTK`是比较流行的`Tkinter`的代替品，各平台下表现都比较好。

`PyGTK`的优点：
- 是`Tkinter`的一个比较流行提单品，`GNOME`下一些应用的`GUI`是`PyGTK`实现，比如`Bittorent`,`GIMP`

`PyGTK`的缺点：
- `Windows`下表现一般，导致跨平台有些问题

#### wxPython

`wxPython`是跨平台GUI工具集`wxWidgets`(C++)的`Python`包装，作为`Python`的一个扩展模块存在, 其中比较大的
有点是比较流行，跨平台比较好。

#### PyQT
`PyQT`是跨平台`GUI`工具集`Qt`的`Python`实现，作为`Python`的插件实现

`PyQT`优点：　
- 比较流行
- 功能强大
- 界面漂亮
- 跨平台支持好 
  

`PyQT`的缺点是可能存在商业授权存问题.

### HelloWorld

我们来看一下`Tkinter`的第一个案例，这个案例调用`Tkinter`的测试函数，想我们显示一个对话框。

    # V1.0 测试
    import tkinter 
    tkinter._test()
运行后会得到一个对话框，可以通过点击`QUIT`来退出。

上面案例只是一个测试，能证明你的环境没问题并能调用`tkinter`相关功能。

我们下面看下典型的`Hello world`的`Tkinter`版本。

在下面的案例中，我们会创建一个空面板, 空面板的标题为`Hello world`，在最后我们
调用`mainloop`让程序进入事件循环(事件循环后面会讲).`

    import tkinter
    base = tkinter.Tk()
    base.wm_title("Hello world")
    base.mainloop()


## `TKinter`基础使用

###  标签(Label)

1. 便签`Label`就是起说明作用的一组文字信息


        import tkinter
        
        base = tkinter.Tk()
        base.wm_title("Label Test")
          
        # 支持属性很多background, font, underline等
        # 第一个参数，制定所属
        lb = tkinter.Label(base, text="Python AI")
        lb.pack()
        
        base.mainloop()

2. Label 可以定义很多个，可以定义背景颜色等


        import tkinter
        
        base = tkinter.Tk()
        base.wm_title("Label Test")
          
        # 支持属性很多background, font, underline等
        # 第一个参数，制定所属
        lb1= tkinter.Label(base, text="Python AI")
        lb1.pack()
        
        lb2= tkinter.Label(base, text="绿色背景", background="green")
        lb2.pack()
        
        lb3= tkinter.Label(base, text="蓝色背景", background="blue")
        lb3.pack()
        
        base.mainloop()

### 按钮(Ｂutton）
按钮`Button`一般当做命令使用, 点击按钮做什么事情, 使用方法和标签类似

按钮当做命令使用,点击下会有相应的动作,这个动作可以理解成一个函数, 问题是这个函数怎么知道你让他去干活了?
这个就需要绑定, 即告诉这个按钮被点击后去执行什么函数.

按钮具备相应的修饰类的属性,比如长款,背景颜色等, 相关属性可以直接设置,比如下面代码:

        import tkinter
    
        baseFrame = tkinter.Tk()
    
        btn1 = tkinter.Button(baseFrame, text="测试按钮")
        btn1['width'] = 30
        btn1['height'] = 30
        btn1.pack()
    
        btn2 = tkinter.Button(baseFrame, text="显示按钮")
        btn2['width'] = 20
        btn2['height'] = 30
        btn2['background'] = 'green'
        btn2.pack()
    
        baseFrame.mainloop()

### 事件绑定的方式

绑定处理函数有两种, 即`command`和`bind`.

1.  `command`属性

    按钮的构造函数有一个参数是`command`, 可以通过这个传递入在点击后需要被调用的函数.


          import tkinter
        
          def showLabel():
          		global baseFrame
          		lb = tkinter.Label(baseFrame, text="显示Label")
          		lb.pack()


        	baseFrame = tkinter.Tk()
    
          btn = tkinter.Button(baseFrame, text="Show Label", command=showLabel)
          btn.pack()
    
          baseFrame.mainloop()


2. `bind`函数
   
    `bind` 函数用来绑定主题和函数
   
    `bind` 的第一个参数是事件类型,它采用的描述方式是这
          样的 `<MODIFIER-MODIFIER-TYPE-DETAIL>`

     - `MODIFIER` 即修饰符,定义组合键,比如按下控制键和切换键再按哪个键, 取值比如控制键`Control`, `Shift`等, 全部取值键参看后面本章备注
     - `TYPE` 表示按键的类型类型,取值例如:`Activate`等, 全部取值请看本章备注
     - `DETAIL` 表示按键的详细信息,具体是按的哪个键, 比如字母`M`等

     - 常见的鼠标左键单击为<Button-1>


   下面代码颜色了单机鼠标左键的效果:

        import tkinter
    
        def showLabel(event):
            global baseFrame
            lb = tkinter.Label(baseFrame, text="显示Label")
            lb.pack()


        baseFrame = tkinter.Tk()
    
        btn = tkinter.Button(baseFrame, text="Show Label")
        btn.bind("<Button-1>", showLabel)
        btn.pack()
    
        baseFrame.mainloop()

   另外一个案例,稍微复杂一点: 

        import tkinter
    
        def reg():
            name = e1.get()
            pwd = e2.get()
    
            t1 = len(name)
            t2 = len(pwd)
    
            if name == "111" and pwd == "222":
                    lb3["text"] = "登录成功"
            else:
                    lb3['text'] = "用户名或密码错误"
                    e1.delete(0,t1)
                    e2.delete(0,t2)
    
        baseFrame = tkinter.Tk()
    
        lb1 = tkinter.Label(baseFrame, text="用户名")
        lb1.grid(row=0, column=0, stick=tkinter.W )
    
        e1 = tkinter.Entry(baseFrame)
        e1.grid(row=0, column=1, stick=tkinter.E)
    
        lb2 = tkinter.Label(baseFrame, text="密码: ")
        lb2.grid(row=1, column=0, stick=tkinter.W )
    
        e2 = tkinter.Entry(baseFrame)
        e2.grid(row=1, column=1, stick=tkinter.E)
        e2['show'] = '*'
    
        btn = tkinter.Button(baseFrame, text="登录", command = reg)
        btn.grid(row=2, column=1, stick=tkinter.E)
    
        lb3 = tkinter.Label(baseFrame, text="")
        lb3.grid(row = 3)
    
        baseFrame.mainloop()

> 绑定参数`MODIFIEL`取值: Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4, Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,B3, Alt, Button4, B4, Double, Button5, B5 Triple , Mod1, M1 。

> 绑定参数`TYPE`取值: Activate, Enter, Map, ButtonPress, Button, Expose, Motion, ButtonRelease,FocusIn, MouseWheel, Circulate, FocusOut, Property, Colormap, Gravity Reparent, Configure, KeyPress, Key, Unmap, Deactivate, KeyRelease Visibility, Destroy,Leave

3. 常见事件
    - 鼠标单击事件
        - `<Button-1>`: 单击鼠标左键
        - `<Button-2>`: 单击鼠标中间键（如果有）
        - `<Button-3>`: 单击鼠标右键
        - `<Button-4>`: 向上滚动滑轮
        - `<Button-5>`: 向下滚动滑轮【鼠标双击事件】

    - 鼠标双击事件
        - `<Double-Button-1>`: 鼠标左键双击
        - `<Double-Button-2>`: 鼠标中键双击
        - `<Double-Button-3>`: 鼠标右键双击

    - 鼠标释放事件
        - `<ButtonRelease-1>`: 鼠标左键释放
        - `<ButtonRelease-2>`: 鼠标中键释放
        - `<ButtonRelease-3>`: 鼠标右键释放

    - 鼠标按下并移动事件(即拖动)
        - `<B1-Motion>`: 左键拖动
        - `<B2-Motion>`: 中键拖动
        - `<B3-Motion>`: 右键拖动

    - 鼠标其他操作
        - `<Enter>`: 鼠标进入控件（放到控件上面）
        - `<FocusIn>`: 控件获得焦点
        - `<Leave>`: 鼠标移出控件
        - `<FocusOut>`: 控件失去焦点

    - 键盘按下事件
        - `<Key>`: 键盘按下，事件event中的keycode,char都可以获取按下的键值
        - `<Return>`: 键位绑定，回车键，
        - `<BackSpace>`
        - `<Escape>`
        - `<Left>`
        - `<Up>`
        - `<Right>`
        - `<Down>`

    - 组合使用
        - `Ctrl+Alt-KeyPress-A>`：同时按下`Ctrl+Shift+Alt+A`等4个键
        - `<KeyPress-A>`：按下键盘中的`A`键


###  输入框(Entry)

- 输入框，功能比较单一
  
- 使用过程类似, 即先定义一个输入框实例, 定义的时候以主框架作为参数
  
- 通过特定属性可以更改输入框行为,例如`entry['show'] = "*"`， 设置遮挡字符

输入框案例如下:

      import tkinter
    
      def reg():
          name = e1.get()
          pwd = e2.get()
    
          t1 = len(name)
          t2 = len(pwd)
    
          if name == "111" and pwd == "222":
              lb3["text"] = "登录成功"
          else:
              lb3['text'] = "用户名或密码错误"
              e1.delete(0,t1)
              e2.delete(0,t2)
    
      baseFrame = tkinter.Tk()
    
      lb1 = tkinter.Label(baseFrame, text="用户名")
      lb1.grid(row=0, column=0, stick=tkinter.W )
    
      e1 = tkinter.Entry(baseFrame)
      e1.grid(row=0, column=1, stick=tkinter.E)
    
      lb2 = tkinter.Label(baseFrame, text="密码: ")
      lb2.grid(row=1, column=0, stick=tkinter.W )
    
      e2 = tkinter.Entry(baseFrame)
      e2.grid(row=1, column=1, stick=tkinter.E)
      e2['show'] = '*'
    
      btn = tkinter.Button(baseFrame, text="登录", command = reg)
      btn.grid(row=2, column=1, stick=tkinter.E)
    
      lb3 = tkinter.Label(baseFrame, text="")
      lb3.grid(row = 3)
    
      baseFrame.mainloop()

### 菜单(Menu)

本节讲述菜单的各种用法, 菜单常用分类为:
- 普通菜单
- 级联菜单
- 弹出式菜单

> 在mac上运行可能会出现一些显示问题, 目前包括普通菜单显示不出来, 级联菜单显示一部分等

我们分别讲述:


####  普通菜单

普通菜单的定义大致用法如下:

1. 第一个`Menu`类定义的是`parent`, 即弹出的所有菜单都是这个菜单的子类
2. 利用`add_command`添加菜单项，如果该菜单是顶层菜单，则从左向右添加，否则是下拉菜单, 其中:
    - `label`: 用来指定菜单项名称，
    - `command`: 指定被点击后调用的方法
    - `acceletor`：指定的是快捷键
    - `underline`: 指定是否有下划线
    - `menu`:属性指定使用哪一个作为顶层菜单

我们先来定义常见的菜单,按照以上步骤,我们参看下面案例:

    import tkinter
    
    baseFrame = tkinter.Tk()
    # 定义父级菜单,
    menubar = tkinter.Menu(baseFrame)
    # 添加弹出的菜单内容
    for item in ['File', 'Edit', 'View', 'About']:
        menubar.add_command(label=item)
    
    baseFrame['menu'] = menubar
    
    baseFrame.mainloop()

#### 级联菜单

级联菜单即菜单的分成, 可以通过菜单选择子菜单,然后还可能继续向下选择:

级联菜单的编写大致过程为:
1. 建立`Menu`实例
2. `add_command`
3. `add_cascade`

其中: 

- `add_cascade`: 级联菜单,作用是引出后面的菜单
- `add_cascade`的:
    - `menu`属性: 指明把菜单级联到哪个菜单项上
    - `label`属性: 指明菜单项的名称

请参看下面代码:

    import tkinter
    
    baseFrame = tkinter.Tk()
    
    menubar = tkinter.Menu(baseFrame)
    
    #  注意参数
    emenu = tkinter.Menu(menubar)
    for item in ['Copy', 'Past', 'Cut']:
        emenu.add_command(label=item)
    
    menubar.add_cascade(label='File')
    menubar.add_cascade(label='Edit', menu=emenu)
    menubar.add_cascade(label='About')
    
    baseFrame['menu'] = menubar
    
    baseFrame.mainloop()

####  弹出菜单

- 弹出菜单叫上下文菜单，或者右键菜单
- 实现大致思路：
    1. 建立菜单并向菜单项添加各种功能
    2. 坚挺鼠标右键
    3. 如果右键单击，则根据位置判定弹出惨淡
    4. 弹出调用Menu的pop方法
    
- `add_separator`：增加分隔符

实现请参看下面案例:

    import tkinter
    
    def makeLabel():
        global baseFrame
        tkinter.Label(baseFrame, text="PHP是最好的编程语言，我用Python").pack()
    
    baseFrame = tkinter.Tk()
    
    menubar = tkinter.Menu(baseFrame)
    
    for x in ['麻辣香菇', '气锅鸡', '东坡肘子']:
        menubar.add_separator()
        menubar.add_command(label=x)
    
    menubar.add_command(label='重庆火锅', command=makeLabel)
    
    def pop(event):
        # 注意使用 event.x 和 event.x_root的区别
        menubar.post(event.x_root, event.y_root)
    
    baseFrame.bind("<Button-3>", pop)

#### `ChekcButton` and `RadioButton`

惨淡中可能会用到选择框和单选框, 这两种组件的时候用过程类似,
即定义完毕后使用函数添加:

- `add_radiobutton`
- `add_checkbutton`
  

具体请参看下面案例:

    import tkinter
    
    baseFrame = tkinter.Tk()
    
    m = tkinter.Menu(baseFrame)
    m2 = tkinter.Menu(m)
    for item in ['Python', 'Perl', 'Php', 'Rubby']:
        m2.add_checkbutton(label=item)
    
    m2.add_separator()
    
    for item in ['Java', 'C++', 'C']:
        m2.add_radiobutton(label=item)
    
    m.add_cascade(label='Lang', menu=m2)
    
    baseFrame['menu']=m
    baseFrame.mainloop()

## 人机交互

人机交互主要研究的是如何使用输入输出的内容, 这里把 `tkinter`中一些简单的部件都放入这一节课, 不算严格意义上的人机交互内容.

### 消息框

用来弹出一个消息,显示给用户,一般会给用户一些选择,比如取消,确定之类的的.

    import tkinter
    
    msg = tkinter.Message(text="I love python and you")
    msg.config(bg="green", font=('times', 18, 'italic'))
    msg.pack(fill=tkinter.X)
    
    tkinter.mainloop()

### 对话框

对话框, 一般采用弹出方式,用来让用户明确输入一些内容:

`TKinter`为我们提供三种标准的对话框:
1. `messagebox`
2. `filedialog`
3. `colorchooser`

需要注明一下, 这个`python`两个版本有点区别:
- `python2.x` 中三个 模块分别是`tkMessageBox`, `tkFileDialog`, `tkColorChooser`，分别独立，使用需要导入
- `python3.x` 中全部归属`tkinter`

#### `messagebox`

- 用来跟用户进行简短交流，例如出错提示等
- 消息框一般有以下几种：
    1. `askokcancel`
    2. `askquesiton`
    3. `askretrycancel`
    4. `askyesno`
    5. `showerror`
    6. `shjowwinfo`
    7. `showwarning`
    
- 消息框需要带三个参数：
    - `title`: 标题
    - `message`: 具体消息
    - `option`: 选项可以有以下含义：
        1. `default`: 指定默认格式
        2. `icon`: 指定图标，取值包括`ERROR, INFO,QUESTION,WARNING`, 不能自己定义
        3. `parent`: 如果不指定，对话框默认显示在根窗口

- 关于返回值：
    1. 返回布尔值的类型：`askokcancel, askretrycancel, askyesno`
    2. 返回`yes/ok`: `askquestion`
    3. 返回`ok`: `showerror, showinfo, showwarning`

参看以下案例:

    import tkinter
    import tkinter.messagebox as mb
    baseFrame = tkinter.Tk()
    
    def showError(event):
        msgRst = mb.showerror(title='错误框', message="粗错了")
        print(msgRst)
        msgRst  = mb.askquestion(title="QUESTION", message="May I ask u a question?", icon=mb.INFO)
        print(msgRst)
    
    baseFrame.bind('<Button-1>', showError)
    
    baseFrame.mainloop()

#### `filedialog`

- 一般用来打开或者保存等与文件操作相关的交互
- 返回值：
    - 如果选择打开某个文件，则返回文件的完整路径
    - 点击取消则返回空串
- 可能用到的参数：
    - `defaultextension`: 指定文件后缀
    - `filetypes`:指定筛选文件类型的下拉菜单选项，值由二元组成（类型名，后缀），例如：
      
            filetypes=[("PNG",".png"),("JPG",".jpg")]
      
    - `initialdir`: 打开默认路径
    - `title`
    - `parent`: 依附的父亲窗口，默认为根窗口

使用请参看下面代码:

        import tkinter
        import tkinter.filedialog as fd
    
        baseFrame = tkinter.Tk()
    
        def showFD(event):
        				fileName = fd.askopenfilename()
        				print(fileName)
    
                # 需要注意次函数返回值是一个结构, 非普通字符串
                fileName = fd.askopenfile()
                print(fileName)
    
                fileName = fd.askdirectory()
                print(fileName)
    
                fileName = fd.asksaveasfile()
                print(fileName)
    
        baseFrame.bind('<Button-1>', showFD)
    
        baseFrame.mainloop()

#### `colorchooser`

- 调色板，颜色选择器
- 参数：
    1. `color`: 用于指定初始化颜色，默认是浅灰色
    2. `option`: 可选`title, parent`
- 返回值：
    - 选择颜色后点击“确定”，返回两个值，第一个是RGB值，第二个是对应的十六进制颜色值
    - 点击“取消”返回（None,None)
    

参看下面代码:

        import tkinter
        import tkinter.colorchooser as cc
    
        baseFrame = tkinter.Tk()
    
        def cb():
            color  = cc.askcolor("RED", title="选个色子：")
            print(color)
            color  = cc.askcolor("RED", title="Choose Again：")
            print(color)
    
        btn = tkinter.Button(baseFrame, text="open", command=cb)
        btn.pack()
    
        baseFrame.mainloop()

## 其他控件

### `CheckButton`

- 实例化跟`Button`很像
- 属于按钮类，所以有`command`属性

使用请参见以下代码:

        import tkinter
    
        baseFrame = tkinter.Tk()
    
        time1 = 0
        time2 = 0
    
        def textPython():
            global lb, cbPython, time1
    
            if time1 % 2 == 0:
                time1 += 1
                lb['text'] = "Python被选择"
            else:
                time1 += 1
                lb['text'] = "Python被取消"
    
        # IntVar，StringVar此类数据的使用需要在 tkinter.Tk()之后，否则报错
        v = tkinter.IntVar()
    
        def textJava():
            value = v.get()
            if value == 0:
                lb['text'] = "Java被取消"
            else:
                lb['text'] = "Java被选中"
    
        cbPython = tkinter.Checkbutton(baseFrame, text="Python", command=textPython)
        cbPython.pack()
    
        cbJava = tkinter.Checkbutton(baseFrame, variable=v, text="Java", command=textJava)
        cbJava.pack()
    
        lb = tkinter.Label(baseFrame, text= "   ")
        lb.pack()
    
        baseFrame.mainloop()

### `Radiobutton`

- 跟`Checkbutton`类似，不同的是需要设置一组，实现一组内只能选择一个
-  参数`variable`: 定义一个可以用来传送值的变量，需要定义为IntVar
- 参数`value`: variable所传送的值

请参看以下代码:

        import tkinter
    
        baseFrame = tkinter.Tk()
    
        def textSelect():
            global lb
    
            value = v.get()
            print(value)
    
            if value == 0:
                lb['text'] = "Python被选择"
                return None
    
            if value == 1:
                lb['text'] = "Java被选择"
                return None
    
            print("ERRRRRRRRRRRROR........{0}".format(value))
            return None
    
        #IntVar，StringVar此类数据的使用需要在 tkinter.Tk()之后，否则报错
        v = tkinter.IntVar()
    
        cbPython = tkinter.Radiobutton(baseFrame, variable=v, text="Python",  value=0, command=textSelect)
        cbPython.pack()
    
        cbJava = tkinter.Radiobutton(baseFrame, variable=v, text="Java", value=1,  command=textSelect)
        cbJava.pack()
    
        lb = tkinter.Label(baseFrame, text= "   ")
        lb.pack()
    
        baseFrame.mainloop()

### `Text`

- 用来批量输入文字
- `indexes`用法：
     - 行列坐标: `row, col` 方式, 行从1开始，列从0开始，可以是引号，可以是浮点数写法

具体使用参看下面代码:

    import tkinter
    
    baseFrame = tkinter.Tk()
    
    t = tkinter.Text(baseFrame, width=50, height=10)
    t.pack()
    t.insert(1.4, "I love python")
    print(t.get(1.5, 1.8))
    
    # mark_set创建一个标签，可以用来表示位置
    t.mark_set("one", 1.6)
    t.insert("one", "哈哈")
    
    baseFrame.mainloop()

### `canvas`

- 画布，可以自由的在上面绘制图形的一个小舞台
- 在画布上绘制对象，通常用`create_xxx(xxx=对戏类型，例如line， rectangle，text)`
  

具体使用参看下面代码:

    # 一个简单的画布例子
    import tkinter
    
    baseFrame = tkinter.Tk()
    
    cvs = tkinter.Canvas(baseFrame, width=300, height=200)
    cvs.pack()
    
    cvs.create_line(23,23, 190,234)
    cvs.create_text(56,67, text="I LOVE PYTHON")


    baseFrame.mainloop()

下面案例用来绘制五角星:

    # V5 绘制一个五角星
    import tkinter
    import math as m
    
    baseFrame = tkinter.Tk()
    
    w = tkinter.Canvas(baseFrame, width=300, height=300, background="gray" )
    w.pack()


    center_x = 150
    center_y = 150
    
    r = 150
    
    points = [
        #左上点
        center_x - int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),
    
        #右上点
        center_x + int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),
    
        #左下点
        center_x - int(r * m.sin( m.pi / 5)),
        center_y + int(r * m.cos( m.pi / 5)),
    
        #顶点
        center_x,
        center_y - r,
    
        #右下点
        center_x + int(r * m.sin(m.pi / 5)),
        center_y + int(r * m.cos(m.pi / 5)),
    ]
    
    w.create_polygon(points, outline="green", fill="yellow")
    w.create_text(150,150, text="五角星")
    
    baseFrame.mainloop()

- `canvas`的作用是把一定组件“画”到画布上，显示出来，`canvas`所支持的组件包括：
    1. `arc`
    2. `bitmap`
    3. `image(BitmapImage, PhotoImage)`
    4. `line`
    5. `oval`
    6. `polygon`
    7. `rectangle`
    8. `text`
    9. `window(组件)`
    
- 每次调用`create_xxx`都会返回一个创建的组件的`ID`，同时候也可以用`tag`属性指定其标签名称
  
- 以下代码，通过调用  `canvas.move` 实现一个一次性动作
  
        import tkinter
        
        baseFrame = tkinter.Tk()
        
        def btnClick(event):
             global  w
             w.move(id_ball, 12,5)
             w.move("fall", 0,5)
        
        w = tkinter.Canvas(baseFrame, width=500, height=400)
        w.pack()
        w.bind("<Button-1>", btnClick)
        
        # 创建组件后返回id
        id_ball  = w.create_oval(20,20, 50,50, fill="green")
        
        # 创建组件使用tag属性
        w.create_text(123,56, fill="red", text="ILovePython", tag="fall")
        # 创建的时候如果没有指定tag可以利用addtag_withtag添加
        # 同类函数还有 addtag_all, addtag_above, addtag_xxx等等
        id_rectangle = w.create_rectangle(56,78,173,110, fill="gray")
        w.addtag_withtag("fall", id_rectangle)
        
        baseFrame.mainloop()



## 实例: 屏保-TKinter版本

> 详细讲解在视频中,请大家参考视频讲解

在整个屏保的构成中,相对内容比较简单,主要构建就是`球`, 各种具有随机属性的球体.

球的构成大概如下:

- 颜色随机, 大小随机, 运动方向随机, 运动速度随机
- 遇到边缘需要反弹

有了球,需要构建一个游戏类,游戏类的生成大概思路是:

1. 创建很多`球`
2. 让这些球 运动起来
3. 如果鼠标移动, 退出




代码实现参考下面代码, 注释已经很详细了:

            import random
            import tkinter
    
            class RandomBall:
                def __init__(self, canvas, scrnwidth, scrnheight):
                    self.canvas = canvas
                    
    								# 球的初始位置, 要求是随机
                    self.xpos = random.randint(10, int(scrnwidth))
                    self.ypos = random.randint(10, int(scrnheight))
    
    								# 移动速度, 这里按每次移动距离计算
                    self.xvelocity = random.randint(4,20)
                    self.yvelocity = random.randint(4,20)
    
                    self.scrnwidth = scrnwidth
                    self.scrnheight = scrnheight
    								
    								# 圆的大小
                    self.radius = random.randint(20,120)
    
    								# 生成颜色, 随机的三个值 , 0-255 表示 
                    c = lambda : random.randint(0,255)
                    self.color = '#%02x%02x%02x'%(c(),c(),c())
    
                def create_ball(self):
    
                    x1 = self.xpos - self.radius
                    y1 = self.ypos - self.radius
                    x2 = self.xpos + self.radius
                    y2 = self.ypos + self.radius
                    
                    # 画圆的方式是确定对角的两个点后, 确定填充颜色和边缘颜色 
                    # 然后自动就画出圆形来了, 这里统一都是按椭圆来画的
                    self.item = self.canvas.create_oval(x1,y1,x2,y2, fill=self.color, outline=self.color)
    
                def move_ball(self):
                    self.xpos += self.xvelocity
                    self.ypos += self.yvelocity
    
                    # 移动过程中一旦碰到幕布边缘就需要反向运动
                    if self.ypos >= self.scrnheight - self.radius:
                       self.yvelocity = - self.yvelocity
    
                    if self.ypos <= self.radius:
                        self.yvelocity = abs(self.yvelocity)
    
                    if self.xpos >= self.scrnwidth - self.radius or self.xpos <= self.radius:
                        self.xvelocity = - self.xvelocity
                    
                    # 按每次移动距离移动球
                    self.canvas.move(self.item, self.xvelocity, self.yvelocity)
    
            class ScreenSaver:
            
                balls = []
    
                def __init__(self,num_balls):
                    self.root = tkinter.Tk()
                    # 取消边框
                    self.root.overrideredirect(1)
    
                    # 检测任何鼠标移动后即退出
                    self.root.bind('<Motion>', self.myquit)
                    
                    # 得到屏幕的长宽数据
                    w,h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                    self.canvas = tkinter.Canvas(self.root, width=w, height=h )
                    self.canvas.pack()
    
                    for i in range(num_balls ):
                        ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
                        ball.create_ball()
                        self.balls.append(ball)
                    
                    # 启动屏保
                    self.run_screen_saver()
                    self.root.mainloop()
    
                def run_screen_saver(self):
                    for ball in self.balls:
                        ball.move_ball()
                    # 每 200ms 让所有的球移动一次
                    self.canvas.after(200, self.run_screen_saver)
                
                # 退出
                def myquit(self,event):
                    self.root.destroy()
    
            if __name__ == "__main__":
            		ScreenSaver(12)

## 实例: 贪吃蛇-TKinter版本

这个游戏分为两个版本, 有一个是多线程,但其中因为年深日久发现很难理解, 所以大拿
童鞋又改了个好理解的版本,大家可以对照着看, 在视频里有分步骤讲解:

容易的版本:


    import tkinter
    import random

    WORLD_WIDTH = 600
    WORLD_HEIGHT = 400
    STEP = 20


    class SnakeWorld():
        def __init__(self):
        self.root = tkinter.Tk()

            # 创建画布
            self.canvas = tkinter.Canvas(self.root, width=WORLD_WIDTH, height=WORLD_WIDTH, bg='gray')
            self.canvas.pack()

            for i in range(0, WORLD_HEIGHT, 20):
                self.canvas.create_line((0, i), (WORLD_WIDTH, i))

            for i in range(0, WORLD_WIDTH, 20):
                self.canvas.create_line((i, 0), (i, WORLD_HEIGHT))

            self.score_show = ScoreShow(self.canvas)

            # 用来显示 分数, 显示位置固定
            self.food = Food(self.canvas)
            self.food.generate_food()

            self.snake = Snake(self.root, self.canvas)
            self.world_running()

            self.root.mainloop()

        def world_running(self):
            print("Hello world")
            self.snake.run()

            rst = self.check_bang()

            if rst > 0:
                self.snake.grow()
                self.food.generate_food()
                self.score_show.new_score(1)


            if rst < 0:
                self.game_over()

            self.root.after(1000, self.world_running)

        def game_over(self):
            self.canvas.create_text(200, 150, fill='white', text='Game Over')
            quitbtn = tkinter.Button(self, text='Quit', command=self.destroy)
            rebtn = tkinter.Button(self, text='Begin', command=self.__init__)
            self.canvas.create_window(200, 180, anchor='nw', window=quitbtn)

        def check_bang(self):
            snake_head = self.snake.get_head_pos()
            food_pos = self.food.food_pos

            if snake_head == food_pos:
                return 1

            if snake_head[0] < 0 or snake_head[0] > WORLD_WIDTH or \
                snake_head[1] <0 or snake_head[1] > WORLD_HEIGHT:
                return -1

            return 0

    class Food():
        def __init__(self, canv):
            self.canv = canv
            self.food_draw = None
            self.food_pos = (0,0)

        def generate_food(self):
            x = (random.randint(50, WORLD_WIDTH - 50) // STEP) * STEP
            y = (random.randint(50, WORLD_HEIGHT - 50) // STEP) * STEP

            if self.food_draw:
                self.canv.delete(self.food_draw)
                self.food_draw = None

            self.food_draw = self.canv.create_line((x, y + 10), (x + 20, y + 10), width=20,
                                                   fill="#00FF00")
            self.food_pos = (x,y)
            return None

    class ScoreShow():

        def __init__(self, canv):
            self.canv = canv
            self.score = 0

            self.score_text = self.canv.create_text(450, 20, fill='white', text='SCORE: 0')

        def new_score(self, score):
            self.score += score
            self.canv.itemconfigure(self.score_text,
                                      text='SCORE: {}'.format(self.score))




    class Snake():

        def __init__(self, tk, canv):
            self.root = tk
            self.canv = canv

            # 这个点位是在放个正常点位上加了半个格子宽度, 为的是取消
            # 方根骑缝现象
            self.snake_points = [110, 110, 110, 130, 110, 150]

            self.direction = 'Down'
            self.snake_line = self.canv.create_line(self.snake_points, width=20,
                                                    fill="red")

            self.root.bind('<Key-Left>', self.key_pressed)
            self.root.bind('<Key-Right>', self.key_pressed)
            self.root.bind('<Key-Up>', self.key_pressed)
            self.root.bind('<Key-Down>', self.key_pressed)

        def get_head_pos(self):
            return self.snake_points[0]-10, self.snake_points[1]-10

        def grow(self):
            self.snake_points.append(self.snake_points[-2])
            self.snake_points.append(self.snake_points[-1])

        def key_pressed(self, e):
            # keysym 按键名称
            if (self.direction == "Left" or self.direction == "Right") \
                    and \
                    (e.keysym == 'Left' or e.keysym == 'Right'):
                return None

            if (self.direction == "Up" or self.direction == "Down") \
                    and \
                    (e.keysym == 'Up' or e.keysym == 'Down'):
                return None

            self.direction = e.keysym

            return None

        def get_next_pos(self):
            x, y = self.snake_points[0], self.snake_points[1]

            if self.direction == 'Up':
                return x, y - STEP
            elif self.direction == 'Down':
                return x, y+STEP
            elif self.direction == 'Left':
                return x-STEP, y
            elif self.direction == 'Right':
                return x+STEP, y

        def run(self):

            pos = self.get_next_pos()
            self.snake_points.insert(0, pos[1])
            self.snake_points.insert(0, pos[0])

            self.snake_points = self.snake_points[:-2]

            self.canv.coords(self.snake_line, *self.snake_points)



    if __name__ == "__main__":
    sw = SnakeWorld()

旧版本实现参考:


        import queue
        import time
        from tkinter import *
        import threading
        import random


        class GUI(Tk):
            def __init__(self, queue):
                Tk.__init__(self)
                self.queue = queue
                self.is_game_over = False
    
                # 创建画布
                self.canvas = Canvas(self, width=500, height=300, bg='gray')
                self.canvas.pack()
                
                # 蛇就是一条线
                self.snake = self.canvas.create_line((0,0),(0,0), fill='#FFCC4C', width=10)
                # 蛇的食物
                self.food = self.canvas.create_rectangle(0,0,0,0,fill='#FFCC4C', outline='#FFCC4C')
                
                # 用来显示 分数, 显示位置固定
                self.points_earned = self.canvas.create_text(450, 20,fill='white', text='SCORE: 0')
                self.queue_handler()


            def queue_handler(self):
                try:
                    while True:
                        task = self.queue.get(block=False)
    
                        if task.get("game_over"):
                            self.game_over()
    
                        if task.get('move'):
                            points = [ x for point in task['move'] for x in point]
                            self.canvas.coords(self.snake, *points)
    
                        if task.get('food'):
                            self.canvas.coords(self.food, *task['food'])
                        elif task.get('points_earned'):
                            self.canvas.itemconfigure(self.points_earned,
                                                      text='SCORE: {}'.format(task['points_earned']))
    
                            self.queue.task_done()
    
                except queue.Empty:
                    if not self.is_game_over:
                        self.canvas.after(100, self.queue_handler)
    
            def game_over(self):
                self.is_game_over = True
                self.canvas.create_text(200,150, fill='white', text='Game Over')
                quitbtn = Button(self, text='Quit', command=self.destroy)
                rebtn = Button(self, text='Begin', command=self.__init__)
                self.canvas.create_window(200, 180, anchor='nw', window=quitbtn)


        class Food():
            def __init__(self,queue):
                self.queue = queue
                self.generate_food()


            def generate_food(self):
                x = random.randrange(5,490,10)
                y = random.randrange(5, 290,10)
    
                self.postion = x,y
                self.exppos = x - 5, y - 5, x + 5, y + 5
                self.queue.put({'food':self.exppos})


        class Snake(threading.Thread):
            def __init__(self,gui, queue):
                threading.Thread.__init__(self)
    
                self.gui = gui
                self.queue = queue
                self.daemon = True
                self.points_earned = 0
                self.snake_points = [(495,55),(485,55), (465,55),(455,55)]
                self.food = Food(queue)
                self.direction = 'Left'
                self.start()
    
            def run(self):
                if self.gui.is_game_over:
                    self._delete()
    
                while not self.gui.is_game_over:
                    self.queue.put({'move': self.snake_points})
                    time.sleep(0.5)
                    self.move()
    
            def key_pressed(self,e):
                # keysym 按键名称
                self.direction = e.keysym
    
            def move(self):
                new_snake_point = self.calculate_new_coordinates()
    
                if self.food.postion == new_snake_point:
                    self.points_earned += 1
                    self.queue.put({'points_earned': self.points_earned})
                    self.food.generate_food()
                else:
                    self.snake_points.pop(0)
                    self.check_game_over(new_snake_point)
                    self.snake_points.append(new_snake_point)


            def calculate_new_coordinates(self):
                last_x, last_y = self.snake_points[-1]
                if self.direction == 'Up':
                    new_snake_point = last_x, last_y - 10
                elif self.direction == 'Down':
                    new_snake_point = last_x, last_y + 10
                elif self.direction == 'Left':
                    new_snake_point = last_x - 10, last_y
                elif self.direction == 'Right':
                    new_snake_point = last_x + 10, last_y
    
                return new_snake_point
    
            def check_game_over(self, snake_point):
                x,y = snake_point[0], snake_point[1]
                if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
                    self.queue.put({'game_over': True})


        def main():
            q = queue.Queue()
            gui = GUI(q)
            gui.title("傻傻的贪吃蛇")
            #global  q, gui
            snake = Snake(gui,q)
    
            gui.bind('<Key-Left>', snake.key_pressed)
            gui.bind('<Key-Right>', snake.key_pressed)
            gui.bind('<Key-Up>', snake.key_pressed)
            gui.bind('<Key-Down>', snake.key_pressed)
            gui.mainloop()
    
        if __name__ == "__main__":
            main()
