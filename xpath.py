''' xpath XML Path Language XML路径语言 最初是用来搜寻XML文档 也适用于HTML文档搜索
xpath 规则
表达式描述
nodename 选取此节点的所有子节点
/ 从当前节点选取直接子节点
// 从当前节点选取子孙节点
. 选取当前节点
.. 选取当前节点的父节点
@ 选取属性
举个例子
//title[@lang='eng'] title 节点的所有子孙节点 同时属性lang的值为eng的节点
再举个例子


from lxml import etree
text = '
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
        </ul>
    </div>
'
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
导入lxml库的etree 模块 然后声明一段HTML文本 调用HTML类初始化 这样成功构建xpath解析对象
html文本最后一个li节点没有闭合 etree模块可以自动修正html文本


from lxml import etree
html = etree.parse("test.html", etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
这次输出结果不同了 多了一个DOCTYPE声明 对解析无任何影响

用//开头的XPath规则选取所有符合要求的节点


from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)


通过/或//即可查找元素子节点或子孙节点 想选择li节点的所有直接a子节点

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

知道子节点 用来查找父节点
from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]//../@class')
print(result)

使用parent::来获取父节点

from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

属性匹配 使用@符号进行属性过滤

from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

文本获取

from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
这里没有获取文本 XPath中text方法前面是/ 此处/含义是选取直接子节点 很明显li的直接子节点都是a节点
文本都是在a节点内部 所有这么匹配到的结果是被修正的li节点内部的换行符 因为自动修正的li节点
的尾标签换行了

如果想获取li节点内部的文本 两种方式 先选取a节点再获取文本 或者使用//
这是一

from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

这是二

from lxml import etree
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

属性获取 获取属性 用@符号 获取li节点下所有a节点的href属性

from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

属性多值匹配

from lxml import etree
 text =
    <li class="li li-first"><a href="link.html">first item</a></li>


html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

这里除了li 还有是li什么的 匹配不上 用上contains方法



from lxml import etree
text =
    <li class="li li-first"><a href="link.html">first item</a></li>

html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

多属性匹配 根据多个属性确定一个节点 利用运算符and

from lxml import etree
text =
<li class="li li-first" name="item"><a href="link.html">first item</a></li>

html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

xpath 运算符

or and mod(除法) + - * div(除法) = !=不等于 < <= > >=


按顺序选择指定匹配第几个节点 即使多个节点满足条件 只取一瓢

from lxml import etree
text =
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
 </div>

html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result=html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last() - 2]/a/text()')
print(result)


xpath的100多个方法 http://www.w3school.com.cn/xpath/xpath_functions.asp
节点轴选择


from lxml import etree

text =
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
 </div>

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)


第一 调用ancestor轴 获取祖先节点 需要跟两个冒号 然后是节点选择器 使用* 表示匹配所有节点  返回结果是第一个
li节点的所有祖先节点 包括html body div ul

二 加了限定条件 冒号后面加div 得到结果只有div这个祖先节点
三 调用attribute轴 获取所有属性值 其后跟的选择器是* 代表获取节点的所有属性返回值就是li节点的所有属性值
四 child轴 获取所有直接子节点 加了限定条件 选取href属性为link1.html的a节点
五 调用descendant轴 获取所有子孙节点 加了限定条件获取span节点 结果只包含span节点不包含a节点。
六 调用following轴 获取但其节点之后的所有节点，使用*匹配 但又加了索引选择所有只获取第二个后续节点。
七 following-sibling轴 获取当前节点之后的所有同级节点 使用*匹配 获取所有后续同级节点
'''