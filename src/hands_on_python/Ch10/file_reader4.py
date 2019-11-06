from hands_on_python.common.commons import ps

"""逐行读取"""

filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
ps()
