import re

html = '<1>> aaa </html>'

txt = re.compile(r'<[^>]+>').sub('', html)
print(txt)
