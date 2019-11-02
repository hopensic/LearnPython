from common.commons import ps

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
ps()

