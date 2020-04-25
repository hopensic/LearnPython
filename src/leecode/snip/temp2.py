import operator
from collections import defaultdict
from itertools import accumulate

# lst = [1, -1, 1, 1, -1, -1, 0]
lst = [2, 0, -2, 4, 2, 0, -2]

target = 2

dic = defaultdict(int)
num = 0

for prefix_sum in accumulate(lst, operator.add):
    tmp = prefix_sum - target
    num = num + 1 if prefix_sum == target else num
    num = num + dic[tmp] if tmp in dic else num
    dic[prefix_sum] += 1

print(num)
