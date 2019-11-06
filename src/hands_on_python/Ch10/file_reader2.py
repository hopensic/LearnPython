from hands_on_python.common.commons import ps

with open('text_files\pi_digits2.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
ps()

