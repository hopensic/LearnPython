import itertools as it
from collections import defaultdict

base_list = [0.5, 1, 1.25, 2, 2.5, 5]
le = len(base_list)
dic_combination = {}
for i in range(1, le + 1):
    c = list(it.combinations(base_list, i))
    for t in c:
        key = sum(t)
        lst = dic_combination.get(key)
        if lst:
            dic_combination[key] = lst if len(t) >= len(lst) else t
        else:
            dic_combination[key] = t

weight_dic = {x / 10: (x / 10 - 1) / 2 for x in range(70, 160, 5) if (x / 10 - 1) / 2 in dic_combination}

a = {k*2: dic_combination[weight_dic[k]] for k in weight_dic}

