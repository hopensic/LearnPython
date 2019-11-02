from common.commons import ps

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datesets\n")
    file_object.write("I love creating apps than can run in a browser.\n")
ps()
