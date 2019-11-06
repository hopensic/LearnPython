from hands_on_python.common.commons import ps

"""逐行读取"""

#filename = "pi_million_digits.txt"
filename = "E:\game\pi-billion.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("请输入你的生日，以yymmdd的格式输入:")
if birthday in pi_string:
    print("你的生日出现在圆周率中")
    print("你的生日在圆周率中的位数是第" + str(pi_string.index(birthday))+"位")
else:
    print("Your birthday does not appear in the first million digits of pi")
ps()
