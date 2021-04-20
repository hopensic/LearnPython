import feedparser

# d = feedparser.parse('http://feedparser.org/docs/examples/atom10.xml')
d = feedparser.parse('https://rsshub.app/twitter/user/DIYgod')

wc = {}
for e in d.entries:
    if 'summary' in e:
        summary = e.summary
    else:
        summary = e.description
    words=ge
