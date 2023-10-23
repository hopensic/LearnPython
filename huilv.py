import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取中国人民银行网站的HTML内容
url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/index.html"
response = requests.get(url)

# html = urlopen(url)
# bsObj=BeautifulSoup(html.read())

html_content = response.text

# 使用BeautifulSoup解析HTML内容
# soup = BeautifulSoup(html_content, "html.parser")
soup = BeautifulSoup(html_content)

lst = soup.find_all("span")



# 提取所需的数据
data = []
table = soup.find("table", class_="table")
rows = table.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    if len(cells) == 6:
        date = cells[0].text.strip()
        for i in range(1, len(cells), 2):
            currency = cells[i].text.strip()
            exchange_rate = cells[i + 1].text.strip()
            data.append([date, currency, exchange_rate])

# 将数据存储到Excel表格中
df = pd.DataFrame(data, columns=["Date", "Currency", "Exchange Rate"])
df.to_excel("exchange_rates.xlsx", index=False)
