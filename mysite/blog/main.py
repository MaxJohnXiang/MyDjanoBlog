# -*- coding:utf-8 -*-
import urllib
import os
import re
#loadurl()这个函数呢，是防打开链接超时，如果超时返回空字符，则主调函数会再次调用(while语句就可以实现)，正常的话返回html代码，一个网页不算大，如果你的网络超级好，timeout可以缩短
def loadurl(url):
    try:
        conn = urllib.urlopen(url,timeout=5)
        html = conn.read()
        return html
    except urllib.URLError:
        return ''
    except Exception:
        print("unkown exception in conn.read()")
        return ''

html =loadurl("http://www.meizitu.com/a/5252.html")
print(html)