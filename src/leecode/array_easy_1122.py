from collections import OrderedDict


class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        out_list = []
        ordered_dic2 = OrderedDict()
        ret_list = []
        for x in arr2:
            ordered_dic2[x] = 0
        for x in arr1:
            if x in ordered_dic2:
                ordered_dic2[x] += 1
            else:
                out_list.append(x)
        for k, v in ordered_dic2.items():
            ret_list += [k] * v
        ret_list.extend(sorted(out_list))

        return ret_list


lst1 = [3, 1, 2, 3, 2, 4, 3, 6, 7, 9, 2, 3, 19]
lst2 = [2, 1, 4, 3, 9, 6]

s = Solution()
print(s.relativeSortArray(lst1, lst2))
