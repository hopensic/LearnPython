import json

from common.commons import ps

filename = 'numbers.json'
try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except Exception:
    print(1)
    raise
else:
    print(numbers)
ps()
