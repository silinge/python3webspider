# import requests
# def get_one_page(url):
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36'
#         }
#     response = requests.get(url, headers = headers)
#     if response.status_code == 200:
#         return response.text
#     return None
#
# def mainly():
#     url = "https://maoyan.com/board/4"
#     html = get_one_page(url)
#     print(html)
#
# mainly()
# 查看页面真实的源代码 在开发者模式下network查看 而不是使用elements选项卡
'''<dd>.*?board-index.*?>(.*?)</li> 一个dd节点  它的排名信息是class board-index 的i节点内利用非贪婪匹配提取i节点内信息
然后需要提取电影的图片 后面有a节点 其内部有两个img节点 第二个img 节点的data-src属性 用正则表达式改写
<dd>.*?board-index.*?>(.*?)</li>.*?data-src="(.*?)"

再往后 提取电影的名称 它在后面的p节点内 class 为name 所以可以用name做一个标志位 然后进一步提取a节点内的正文内容
<dd>.*?board-index.*?>(.*?)</li>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>

还往后 提取主演 发布时间评分等内容 写一个
<dd>.*?board-index.*?>(.*?)</li>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?
star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</li>.*?fraction.*?>
(.*?)</li>.*?</dd>
换行了 用re.S 这个正则表达式匹配一个电影结果 匹配7个信息 使用findall提取所有内容

'''
import re
import requests

def get_one_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36'
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
#                          '(.*?)</a>.*star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
#                          '(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
#     # 长代码的换行 使用右斜杠 正则表达式失灵了 使用enter 没有问题
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {'index':item[0],
#             'image':item[1],
#             'title':item[2],
#             'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
#             'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
#             'score':item[5].strip() + item[6].strip()}
#         return items
    # print(items)

# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
#         re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {'index': item[0],
#             'image': item[1],
#             'title': item[2].strip(),
#             'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
#             'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
#             'score': item[5].strip() + item[6].strip()}
#
# url = "https://maoyan.com/board/4"
# html = get_one_page(url)
# how = parse_one_page(html)
# print(how)

'''抓到了再整理一下


import re
import requests

def get_one_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36'
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                         '(.*?)</a>.*star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
                         '(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }
        print(items)
url = "https://maoyan.com/board/4"
html = get_one_page(url)
parse_one_page(html)
print()
但是这个yield不成功 没出结果

假如提取完了 再写入文件 通过JSON库的dumps方法实现字典的序列化 指定ensure_ascii参数为False
来保证输出结果为中文形式而不是Unicode编码


import json
import re
import requests

def get_one_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36'
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                         '(.*?)</a>.*star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
                         '(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    # for item in items:
    #     yield {'index': item[0],
    #            'image': item[1],
    #            'title': item[2].strip(),
    #            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
    #            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
    #            'score': item[5].strip() + item[6].strip()}
    return items


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

url = "https://maoyan.com/board/4"
html = get_one_page(url)
content = parse_one_page(html)
write_to_file(content)
yield 再次失败

整合代码


import json
import re
import requests

def get_one_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36'
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                         '(.*?)</a>.*star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
                         '(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {'index': item[0],
               'image': item[1],
               'title': item[2].strip(),
               'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
               'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
               'score': item[5].strip() + item[6].strip()}
    # return items


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# def mainly():
#     url="https://maoyan.com/board/4"
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         write_to_file(item)

# mainly()
# 分页爬取 爬10页

def mainly(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    for i in range(10):
        mainly(offset=i * 10)
        '''
# 完整代码

import json
import re
import requests
from requests.exceptions import RequestException
import time

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36'
            }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                         '(.*?)</a>.*star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>'
                         '(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {'index': item[0],
               'image': item[1],
               'title': item[2].strip(),
               'actor': item[3].strip()[3:],
               'time': item[4].strip()[5:],
               'score': item[5] + item[6]}

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def mainly(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        mainly(offset=i * 10)
        time.sleep(2)