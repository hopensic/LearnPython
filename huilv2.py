import re

from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver

# 获取中国人民银行网站母页面HTML内容
url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/index.html"
browser = webdriver.Edge()

try:
    browser.get(url)
    html_content = browser.page_source

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(html_content, features="lxml")
    lst = soup.find_all("td", {"height": 22})

    # 获取最新汇率的页面所在的表格
    newest_td = lst[0]
    sub_url_a_module = newest_td.find('a')
    sub_url = 'http://www.pbc.gov.cn' + sub_url_a_module['href']
    # 从页面获取到最新日期
    current_date = newest_td.find('span').string

    # 获取最新汇率子页面
    browser.get(sub_url)
    html_content = browser.page_source
    soup = BeautifulSoup(html_content, features="lxml")
    rate_content = soup.find("div", {"id": "zoom"}).find("p").string
    idx = rate_content.index('1美元')
    idx2 = rate_content.index('人民币1元对')
    export_lst = []
    # 外币兑人民币
    foreign_to_china = rate_content[idx:idx2]
    china_to_foreign = rate_content[idx2:len(rate_content) - 1]

    foreign_to_china_array = foreign_to_china.split('，')
    china_to_foreign_array = china_to_foreign.split('，')

    for line in foreign_to_china_array:
        if len(line) == 0:
            continue
        idx_dui = line.index("对")
        before_dui = line[:idx_dui]
        if line.find('日元') < 0:
            foreign_number = 1
            currency = before_dui[1:]
        else:
            currency = before_dui[3:]
            foreign_number = 100
        rate = re.findall(r'\d+\.\d+', line)
        export_lst.append([current_date, foreign_number, currency, rate[0], '人民币', line])
    export_lst.append(['-', '-', '-', '-', '-', ])

    for line in china_to_foreign_array:
        rate = re.findall(r'\d+\.\d+', line)
        last_number = re.finditer(r'\d', line)
        for i in last_number:
            pass
        currency_idx = i.span()[1]
        currency = line[currency_idx:]

        export_lst.append([current_date, 1, '人民币', rate[0], currency, line])

    df = pd.DataFrame(export_lst, columns=["日期", "数量", "币种1", "汇率", "币种2", "示例"])
    df.to_csv(f'd:/{current_date}.csv', encoding="utf_8_sig")
finally:
    browser.close()
