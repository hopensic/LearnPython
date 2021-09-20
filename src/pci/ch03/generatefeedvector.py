from collections import defaultdict

import feedparser
import re


def getwords(html):
    # 去除所有html标记
    txt = re.compile(r'<[^>]+>').sub('*=', html)
    return txt


# 返回一个RSS订阅情况的标题和单词计数情况的字典
def getwordcounts(url):
    # 解析订阅源
    d = feedparser.parse(url)
    wc = defaultdict(int)

    # 循环遍历所有的文章条目
    for e in d.entries:
        summary = e.summary if 'summayr' in e else e.description
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc[word] += 1
    return d.feed.title, wc


u = "http://feeds.feedburner.com/37signals/beMH"
getwordcounts(u)