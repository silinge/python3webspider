# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# # print(response.read().decode('utf-8'))
# # print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
"""给链接传递参数实现举例
urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
data参数 传递这个参数 用POST方式
"""

# import urllib.parse
# import urllib.request

# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding="utf8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read())
# timeout 参数 如果请求超出了设置的这个时间，还没有得到响应就会抛出异常 如果不指定就会使用全局默认时间
# 实例
# import urllib.request
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())

# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# import urllib.request
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
# 看看Request 可以通过怎样的参数来构造
# import urllib.request
# class urllib.request.Request(url, data=None,
# header={}, origin_req_host=None,
# unverifiable=False, method=None)
"""
url 必须要有 
data b必须使用bytes(字节流类型) 如果是字典 可以先用urllib.parse 模块
urlencode()进行编码
headers 一个字典 它是请求头 可以构造请求是通过headers参数构造，也可以调用
请求实例add_header()来添加
添加请求头常见用法是修改User-Agent来伪装浏览器 默认是Python-urllib
可以设置成谷歌 火狐 IE
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4022.0 Safari/537.36


User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0

origin_req_host 指的是请求方的host名称或ip

unverifiable 表示这个请求是否是无法验证的 默认 False 表示用户没有足够权限
来选择接收这个请求的结果 例如 请求一个html中图片 但是没有自动抓取图像的权限 
这是 unverifiable=True
method是一个字符串 指示请求使用的方法 GET POST PUT
"""
# 举个例子
# from urllib import request, parse
# url = 'http://httpbin.org/post'
# headers = {'User-Agent':'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
# 'Host':'httpbin.org'
# }

# dict = {'name':'Tom'}
# data = bytes(parse.urlencode(dict),
# encoding='utf8' #utf8 utf-8 看清楚
# )
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header() #这个添加headers也一样。
# response = request.urlopen(req)

# print(response.read().decode('utf-8'))

"""
urllib.request模块中的BaseHander类 它是所有其他Handler的父类
提供最基本的方法 例如 default_open protocol_request等。
举个栗子
HTTPDefaultErrorHandler 用于处理HTTP响应错误，抛出HTTPError类型异常。
HTTPRedirectHandler用于重定向
HTTPCookieProcessor 用于处理Cookies
HTTPPasswordMgr用于管理密码 它维护了用户名密码的表
HTTPBasicAuthHandler用于管理认证 如果一个链接打开时需要认证 那么可以用它里解决认证问题

https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler

另外一个类 OpenerDirector 称之为Opener 引入Opener 为了实现更高级的功能
Request和urlopen相当于类库为你封装了极其常用的请求方法 利用他们可以完成基本的请求 
但深入一层进行配置 要用到Opener
"""
# 再举个栗子 验证页面 借助HTTPBasicAuthHandler
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# #import 多了不能使用enter换行 要喊错
# from urllib.error import URLError
# username = 'admin'
# password = 'root'
# url='http://localhost:6000/'
# # url = 'http://www.baidu.com'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

# 添加代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener

# proxy_handler = ProxyHandler({
#     'http':'http://127.0.0.1:9743','https':'https://127.0.0.1:9743'
# })

# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
#  处理cookie

# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)

# 已经输出了cookie 还可以输出文件文本
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("https://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)
# 使用debug能够生成txt文件 正常运行却不行
"""LWPCookieJar同样可以读取保存Cookie 保存格式与MozillaCookieJar不同 
保存成libwww-perl(LWP)格式的Cookie文件。
cookie = http.cookiejar.LWPCookieJar(filename)
试一下
"""
# import http.cookiejar, urllib.request
# filename = 'cookies_lwp.txt'
# # cookie = http.cookiejar.LWPCookieJar(filename)
# # handler = urllib.request.HTTPCookieProcessor(cookie)
# # opener = urllib.request.build_opener(handler)
# # response = opener.open("https://www.baidu.com")
# # cookie.save(ignore_discard=True, ignore_expires=True)
# debug运行 不知道为什么 继续看看吧
# 生成文件后读取
# import http.cookiejar, urllib.request
# # LWP-Cookies-2.0 这里要声明文本格式 不然这个lwp格式报错
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies_lwp.txt', ignore_discard=True, ignore_expires=True)
# # 前一段生成了txt文件 这一段才能load 文件需要先存在 不能凭空load
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')

# print(response.read().decode('utf-8'))

"""
 URLError 错误处理 是urllib库的模块 继承了OSError类
 """
# from urllib import request, error
# try:
#      response = request.urlopen('https://www.google.com')
# except error.URLError as e:
#     print(e.reason)

"""
HTTPError 是URLError的子类 具有三个属性
code 返回HTTP状态码 比如404 不存在 500服务器内部的错误
reason 返回错误原因
headers 返回请求头
"""
# from urllib import request, error
# try:
#     response = request.urlopen('https://www.googlev.com')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')

# 想要更好的
# from urllib import request, error

# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('IT IS OK WA.')

# 再举个例子
# import socket
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('time out')
"""解析链接 urllib 提供了parse模块 它定义了处理URL的标准接口 抽取 合并以及链接转换 协议有
file ftp gopher hdl http https imap mailto mms news nntp prospero rsync rtsp sftp
sip sips snews svn svn+ssh telnet wais
urlparse 识别和分段
from urllib.parse import urlparse
result = urlparse("http://www.baidu.com/index.html;uers?id=5#comment")
print(type(result), result)
返回结果包括6部分 scheme netloc path params query fragment
以这个链接为例 http://www.baidu.com/index.html;user?id=5#comment
://前面就是scheme 代表协议 第一个/符号前面便是netloc 即域名后面是path 即访问路径
分号;后面是params 代表参数 问号？后面是查询条件query一般用作GET类型的URL；井号后面是锚点 
用于直接定位于页面内部的下拉位置 like scheme://netloc/path;paramas?query#fragment 
urlparse API

urllib.parse.urlparse(urlstring, scheme="", allow_fragments=True)
urlstring 必填项 待解析的URL
scheme 协议 默认是http和https
from urllib.parse import urlparse
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)
假如url不包含params 和query fragment 便会被解析为path的一部分
from urllib.parse import urlparse
result = urlparse("http://www.baidu.com/index.html#comment", allow_fragments=False)
print(result)

from urllib.parse import urlparse
result = urlparse("http://www.baidu.com/index.html#comment", allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
我们分别用索引和属性名获取了scheme 和netloc 二者结果一样 没问题

urlunparse 方法 它接受的参数是一个可迭代对象 参数长度必须是6
from urllib.parse import urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=9', 'comment']
print(urlunparse(data))

 urlsplit 它不再单独解析params 只返回5个结果 params合并到path中去 返回结果SplitResult 是元组
也可以用索引来获取
from urllib.parse import urlsplit
result = urlsplit("http://www.baidu.com/index.html;user?id=5#comment")
print(result)
from urllib.parse import urlsplit
result = urlsplit("http://www.baidu.com/index.html;user?id=5#comment")
print(result.scheme, result[0])
urlunsplit 约等于urlunparse方法类似 长度还必须是5
from urllib.parse import urlunsplit
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
urljoin 生产链接 提供一个base_url作为第一参数 将新的链接作为第二个参数 urljoin会分析base_url
scheme netloc和path 对链接确实的部分进行补充 返回结果
from urllib.parse import urljoin
base_url = 'https://www.baidu.com'
print(urljoin(base_url, 'FAQ.html'))
print(urljoin(base_url, 'http://aisuranove.com/videos.html'))
print(urljoin(base_url + '/about.html', 'http://www.google.com/FAQ.html'))
print(urljoin(base_url + '/about.html', 'https://cn.bing.com/FAQ.html?question=3'))
print(urljoin(base_url + '?wd=abc', "https://python.org/index.php"))
print(urljoin(base_url, "?category=2#comment"))
print(urljoin("www.baidu.com", "?category=2#comment"))
print(urljoin('www.baidu.com#comment', '?category=2'))

urlencode 构造GET请求参数
from urllib.parse import urlencode
params = {
    'name':'Mary',
    'age':24
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)
parse_qs 反序列化 GET请求参数 使用parse_qs转回字典
from urllib.parse import parse_qs
query = 'name=Harode&amp;age=25'
print(parse_qs(query))
parse_qsl 将参数转化成元组组成的列表
from urllib.parse import parse_qsl
query='name=Marie&amp;age=29'
print(parse_qsl(query))
quote 用于将内容转化为URL编码格式 URL带有中文参数时 可能导致乱码 这个方法可以转中文字符
from urllib.parse import quote
kw = '红烧鲫鱼'
url = "https://www.baidu.com/s?wd=" + quote(kw)
print(url)
unquote 看上一条 转回来 有啥不一样
from urllib.parse import unquote
url = "https://www.baidu.com/s?wd=%E7%82%B8%E9%B8%A1"
print(unquote(url))
robots 协议 robots.txt 来确定哪个页面能爬哪个不能
User-agent:* #描述爬虫的名称 规定认那些爬虫
Disallow:/ #指定不能抓取哪些文件和目录
Allow:/public/#指定能抓取哪些文件和目录 disallow 和 allow一般一起使用 这个表示只允许抓取public
User-agent:*
Disallow:/
禁止所有爬虫访问任何目录
User-agent:*
Disallow:
允许所有爬虫访问任何目录
User-agent:*
Disallow:/private/
Disallow:/tmp/
禁止访问某些目录
User-agent:WebCrawler
Disallow:
User-agent:*
Disallow:/
只允许某一个爬虫访问

常见爬虫名称 BaiduSpider Googlebot 360Spider YodaoBot 有道 ia_archiver 这个是Alexa Scooter 这是altaista
使用robotparser 来解析robots.txt 提供一个类 RobotFileParser 来判断是否有权限爬取
urllib.robotparser.RobotFileParser(url='')
ser_url：设置robots.txt文件链接
read 读取robots.txt 
parse 解析robots.txt
can_fetch 传入两个参数 第一个 User-agent 二要抓取的URL 返回True或者False 表示能不能爬
mtime 返回抓取和分析robots.txt 的时间
modified 将当前时间设置为上次抓取和分析robots.txt 的时间

from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url("https://www.oneplusbbs.com/robots.txt")
rp.read()
print(rp.can_fetch("*", 'https://www.oneplusbbs.com/thread-5244101-1.html'))
print(rp.can_fetch("*", "https://www.oneplusbbs.com/search-forum-srchtxt-lineageos.html"))
用parser方法执行读取和分析
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
rp = RobotFileParser()
rp.parse(urlopen("https://www.oneplusbbs.com/robots.txt").read().decode("utf-8").split("\n"))
print(rp.can_fetch("*", "https://www.oneplusbbs.com/thread-5244101-1.html"))
print(rp.can_fetch("*", "https://www.oneplusbbs.com/search-forum-srchtxt-lineageos.html"))
这一节就到这儿了。"""