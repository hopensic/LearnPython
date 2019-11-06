from hands_on_python.Ch11.name_function import get_formatted_name
from hands_on_python.common.commons import ps

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
ps()
