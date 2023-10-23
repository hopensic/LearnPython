import datetime
import os
import sys
from pathlib import Path

week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
folder = 'D:/01.dropbox/Dropbox/11.家人/03.family-diary/2023'


def ge():
    day = input('请输入日期\n')
    day = datetime.date.today() if len(day) == 0 else day
    print(f'生成的日期是:{day}\n')
    file_name = f'{str(day)}.md'
    day_str = str(day)
    date_p = datetime.datetime.strptime(day_str, '%Y-%m-%d').date()
    title = f'# {date_p.year}年{date_p.month}月{date_p.day}日 {week_list[date_p.weekday()]} \r\n '
    f = open(f"{folder}/{file_name}", "w")
    f.write(title)
    f.close()
    print('生成成功!\n')
    os.system('pause')


def rn():
    search_path = Path(folder)
    while (True):
        day = input('请输入日期\n')
        day = datetime.date.today() if len(day) == 0 else day
        results = list(search_path.rglob(f"{day}*.md"))
        if day == 'q':
            os.system('pause')
            return
        elif len(results) > 1:
            print("找到的日期文件多于1,请重新输入!\n")
        elif len(results) == 0:
            print("没有找到可以修改的文件，请重新输入\n")
        else:
            break
    print(f'生成的日期是:{day}\n')
    content = input('请输入标题\r\n')
    new_file_name = f'{str(day)}-{content}.md'
    results[0].rename(f'{folder}/{new_file_name}')
    print(f'生成的文件名是:{new_file_name}\n')
    print('更改成功!\n')
    os.system('pause')


def main(argv):
    action = argv[1]
    if action == 'ge':
        ge()
    else:
        rn()


if __name__ == "__main__":
    main(sys.argv)
