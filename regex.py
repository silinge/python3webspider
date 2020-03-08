# 正则表达式
# \w 匹配字母数字下划线
# \W 匹配不是字母数字及下划线的字符
# \s 匹配任意空白字符 等价于[\t\n\t\f]
# \S 匹配任意非空字符
# \d匹配任意数字等价于[0-9]
# \D匹配任意非数字字符
# \A匹配字符串开头
# \Z匹配字符串结尾 如果存在换行 只匹配到换行前的结束字符串
# \z 匹配字符串结尾 如果存在换行 同时还会匹配换行符
# \G 匹配最后匹配完成的位置
# \n匹配一个换行符
# \t匹配一个制表符
# ^匹配一行字符串的开头
# $匹配一行字符串的结尾
# . 匹配任意字符 除了换行符 当re.DOTALL标记被指定是，则可以匹配包括换行符的任意字符
# [...] 用来表示一组字符 单独列出 比如[amd]匹配a、 m、 或者d.
# [^...] 不在[]中的字符 [^amd] 匹配除了a m d 之外的字符。
# * 匹配0和多个表达式
# +匹配1或多个表达式
# ？匹配0或1个前面的正则表达式定义的片段 非贪婪方式
# {n} 精确匹配n个前面的表达式
# {n,m} 匹配n到m次由前面正则表达式定义的片段 贪婪模式
# ()匹配括号内的表达式 表示一个组
# match
# import re
# content = 'Hello 1234 4563 World_This is a Regex Demo.'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())
# 使用的match 如果匹配不到 返回None 第一个正则表达式 第二个参数传入要匹配的字符串
# import re
# content = 'Hello 12345 World_This is a Regexies Demons'
# result = re.match('^\w{5}\s\d{5}\s\w{10}\s\w{2}\s\w\s\w{8}\s\w{4}', content)
# print(result)
# print(result.group())
# print(result.span())

# 通用匹配  点星
# import re
# content = "Hello there 345633. You are seeing a regex demons"
# result = re.match('^He.*ons$', content) # there should be two arguments !!!!!!
# print(result)
# print(result.group())
# print(result.span())

# 贪婪和非贪婪
# import re
# content = "Hello Jude how are you 83452=3= a new regex demo"
# result = re.match('^Hello.*(\d+).*demo$', content) 贪婪
# result = re.match('^Hello.*?(\d+).*demo$', content)  非贪婪
# print(result)
# print(result.group(1))
'''在贪婪匹配下 .*会匹配尽可能多的字符 正则表达式中.*后面是\d+ 也就是至少一个数字 
并没有指定具体多少个数字 因此.*就尽可能匹配多的字符 这样就匹配到了8345 到 5， 得个\d+ 
留一个 那就是2了 而把.* 换乘成.*? 就成立非贪婪匹配 那就是尽可能少的匹配 83452 都留给\d+了。
在做匹配的时候字符串中间尽量使用非贪婪匹配也就是用.?来代替一面出现匹配结果缺失的情况'''


# 如果.*?出现在结尾则可能匹配不到结果 因为它尽可能少的匹配结果
# import re
# content = "http://weibo.com/comment/avScbwq"
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1:',result1.group(1))
# print('result2:',result2.group(1))

# 修饰符 正则表达式可以包含可选修饰符来控制匹配的模式 修饰符被指定为一个可选的标志
# import re
# content = '''Hello 345679 World is not
# perfect this is a Regex demo'''
# result = re.match('^Hello.*?(\d+).*?demo$', content) 这个匹配不到换行符 会报错
# result = re.match('^Hello.*?(\d+).*?demo$', content, re.S) #加修饰符
# 这个修饰符re.S 在网页匹配中经常用到
# print(result.group(1))


'''修饰符
re.l 使匹配对大小写不敏感
re.L 做本地化识别匹配 locale-aware
re.M 多行匹配 影响^ $
re.S 使匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符 这个标志会影响\w, \W, \b, \B 
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解
'''
# 转义匹配
# import re
# content = '(谷歌一下，你就收费)www.bing.com'
# result = re.match('\(谷歌一下，你就收费\)www.bing.com', content)
# print(result)
# import re
# content = 'Extra stings Hello 34345676 word or world. this is a regex demo'
# result =re.match('Hello.*?(\d+).*?demo', content)
# # match方法 一直是从头开始匹配 换个别的 search方法 他匹配时扫描整个字符串 然后返回第一个成功匹配的结果
# result1 = re.search('He.*?(\d+).*?demo', content)
# print(result1)

# import re
# html = '''
#     <div id="sons-list">
#         <h2 class='title'>经典老歌</h2>
#         <p class="introduction">
#         经典老歌列表
#         </p>
#         <ul id="list" class="list-group">
#             <li data-view="2">一路上有你</li>
#             <li data-view="7">
#             <a href="2.mp3" singer="任贤齐">沧海一声笑</a>
#             </li>
#             <li data-view="4" class="active">
#             <a href="3.mp3" singer="齐秦">往事随风</a>
#             </li>
#             <li data-view="6"><a href="4.mp3" singer="beyond">光辉岁月</a></li>
#             <li data-view="5"><a href="5.mp3" singer="陈慧琳">记事本</a></li>
#             <li data-view="5"><a href="6.mp3" singer="邓丽君">甜蜜蜜</a></li>
#         </ul>
#     </div>
# '''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)

# 改变一下条件 不加active
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# 得到第一个结果 沧海一声笑  匹配第一个目标

# 如果re.S也不要 有换行符的就匹配不到了 那就是光辉岁月
# result=re.search('<li.*?singer="(.*?)">(.*?)</a>', html)

# if result:
#     print(result.group(1), result.group(2))

# 由于使用同一个html内容 接着写findall的方法 它能找到所有符合条件的值
# result1 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)>(.*?)</a>', html, re.S)
# print(result1)
# print(type(result1))
# for result in result1:
#     print(result)
#     print(result[0],result[1], result[2])

# sub 除了使用正则表达式提取信息外 可能还需要借助它来修改文本 例如把一串文本剔除数字 使用sub方法
# import re
# content = '2dd2e2syaow39Ssdjyad903kjsfdh3id893sad'
# content = re.sub('\d+', '<', content)
# content = re.sub('[a-gA-O]+', ' ', content)
# print(content)
# print(content2)
# 可以剔除可以替换

# 处理html歌名
import re
# html = '''
#     <div id="sons-list">
#         <h2 class='title'>经典老歌</h2>
#         <p class="introduction">
#         经典老歌列表
#         </p>
#         <ul id="list" class="list-group">
#             <li data-view="2">一路上有你</li>
#             <li data-view="7">
#             <a href="2.mp3" singer="任贤齐">沧海一声笑</a>
#             </li>
#             <li data-view="4" class="active">
#             <a href="3.mp3" singer="齐秦">往事随风</a>
#             </li>
#             <li data-view="6"><a href="4.mp3" singer="beyond">光辉岁月</a></li>
#             <li data-view="5"><a href="5.mp3" singer="陈慧琳">记事本</a></li>
#             <li data-view="5"><a href="6.mp3" singer="邓丽君">甜蜜蜜</a></li>
#         </ul>
#     </div>
# '''

# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])

# 使用sub达到同样的效果 先剔除a标签 再提取
# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())

# compile方法 可以将正则字符串编译成正则表达式对象 以便在后面的匹配中复用
# compile 还可以传入修饰符 :re.S等 再使用search find 就不需要再次传入了
# import re
# content1 = '2030-12-24 11:02'
# content2 = '2010-05-21 01:22'
# content3 = '2023-02-14 17:43'
# pattern = re.compile('\d{2}:\d{2}')
# pattern = re.compile('^\d{4}-')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)
