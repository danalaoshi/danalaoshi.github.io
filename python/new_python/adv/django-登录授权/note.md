#  0 概念
- 认证(uthentication ): 解决你是谁的问题，例如你是不是系统的用户
- 授权(authorization)：解决你有啥权限的问题，例如在系统里你是否可以编辑内容，是否是超级管理员等
-  在程序中，这俩可能会混淆

# 1 单系统登录
- http协议的无状态性导致服务器不能记住上次访问的内容和状态
- 发展出相应的解决问题
    - 请求参数
    - session
- 弊端
    - 此方法只对单系统可用
    - 例如访问淘宝可以把喜欢的东西放入购物车，但是再访问京东的时候，京东肯定是认不出你的购物车内的信息的
   
# 2. SSO(SingleSignOn)
 - 问题提出：假定服务器有多个独立系统，能否多个独立系统共享一套验证信息
 - 正常多服务器登录时序图
![sso](./pic/sso.jpg)

 - sso退出登录时序图
  
![sso_logout](./pic/sso_logout.jpg)
    
 
# 3. 跨域读写cookie
- 参考　　https://www.cnblogs.com/yueshutong/p/9468035.html
## 3.1 利用HTML的script标签跨域写Cookie

比如当前域是www.a.com,下面的script标签是跨域写cookie的核心，通过此标签实现了向www.b.com域写入cookie：


	<script type="text/javascript" src="http://www.b.com/setCookie?cname=token&cval=123456"></script>

- P3P协议
	P3P是一种被称为个人隐私安全平台项目（the Platform for Privacy Preferences）的标准，能够保护在线隐私权，使Internet冲浪者可以选择在浏览网页时，是否被第三方收集并利用自己的个人信息。如果一个站点不遵守P3P标准的话，那么有关它的Cookies将被自动拒绝，并且P3P还能够自动识破多种Cookies的嵌入方式。p3p是由全球资讯联盟网所开发的。

- 举个例子：

  我们在访问A网站时，理论上说，我们只能把Cookie信息保存到A站域名下，而不能写入到B网站下。如果想要跨域读写Cookie，只是通过script标签变相访问B网站在一些浏览器是行不通的，此时B网站的服务器应该告诉浏览器允许A网站写入Cookie，否则浏览器将会拒绝执行，这就是P3P协议。

- 服务端如何告诉浏览器？
	- P3P提供了一种简单的方式 ，来加载用户隐私策略，只要在http响应的头信息中增加 
	
    	
        response.setHeader("P3P","CP=NON DSP COR CURa ADMa DEVa TAIa PSAa PSDa IVAa IVDa CONa HISa TELa OTPa OUR UNRa IND UNI COM NAV INT DEM CNT PRE LOC);
        
       而无需指定隐私策略文件也可以达到指定隐私策略的目的。 CP=后面的字符串分别代表不同的策略信息。

- 因为P3P协议所以不能保证所有浏览器都能通过script标签方式跨域写Cookie，有的浏览器本身就是拒绝跨域的。

- 这种方式是不能保证跨域写cookie的成功性。

##３.２　通过URL参数实现跨域信息传递
- 我们要在A域实现写入token到B域，需要在A域设计一个servlet接收请求

	
    @WebServlet(name = "tg")
	public class Servlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 	throws IOException {
        //获取请求的目标域
        String from = request.getParameter("from");
        //生成token，
        String token = "123456";
        //重定向到目标域
        response.sendRedirect(from + "?cname=token&cval=" + token);
     }
    ...
    }
- 由a域发起请求，请求地址：http://www.a.com/tg?from=http://www.b.com/set_cookie, 请求后该Servlet会获取from参数的值并生成token最后让客户端重定向到http://www.b.com/set_cookie?cname=token&cval=123456，然后B域的Servlet("set_cookie")获取Url参数写入Cookie到客户端，代码：


		 //将要写入的cookie项，调用者通过参数传递
        String cookieName = request.getParameter("cname");
        String cookieValue = request.getParameter("cval");

        //生成cookie
        Cookie cookie = new Cookie(cookieName,cookieValue);
        cookie.setPath("/");
        //一般可以将domain设置到顶级域
        //cookie.setDomain("www.b.com");
        response.addCookie(cookie);
        
## 3.3 读取其它域的Cookie
- 利用script标签执行另一个域实现的读取cookie方法，script标签返回结果将是变量定义形式的JS代码，每一个变量表示一个cookie项，这些代码加载后，此页面后续JS代码可以直接在script脚本中读取已定义的变量值，即各cookie值。

		<script type="text/javascript" src="http://www.b.com/reaf_cookies"></script>
        HTML页面读取

		<script>
		alert(token);
		</script>
- B域的url为/read_cookies的Servlet的实现
如图，首先我们先在request中获取cookie数组，然后for循环遍历拼接为类似var token='test123';的字符串。最重要的是设置ContentType为application/javascript

	 protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        Cookie[] cookies = request.getCookies();
        StringBuilder stringBuilder = new StringBuilder();
        //一定要设置响应类型，否则可能导致IE不解析js直接进行下载操作
        response.setContentType("application/javascript");

        if (cookies != null) {
            for (Cookie cookie : cookies) {
                //结果类似于这样 var token='123456';
                stringBuilder.append("var ")
                        .append(cookie.getName())
                        .append("=")
                        .append("'")
                        .append(cookie.getValue())
                        .append("'")
                        .append(";");
            }
            response.getWriter().append(stringBuilder.toString());
        }
     }