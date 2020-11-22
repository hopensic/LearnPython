from typing import List

total_num = 4  # 候选的数字
used_num = 3  # 需要使用的数字

lst = [i for i in range(1, total_num + 1)]


def find_num(needed_num: int, p_lst: List):
    cur_lst = []
    for i in range(len(p_lst)):
        m = p_lst[i]
        rem_lst = p_lst[:i] + p_lst[i + 1:]
        if needed_num == 1:
            return [[p] for p in p_lst]
        else:
            for p in find_num(needed_num - 1, rem_lst):
                cur_lst.append([m] + p)
    return cur_lst


res = find_num(used_num, lst)
print(res)
print(len(res))
