from common.commons import ps

"""逐行读取"""

filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
ps()
