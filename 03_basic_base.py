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
import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())