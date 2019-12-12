from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes):
        ret_lst = []
        list_dic = defaultdict(list)

        for index, size in enumerate(groupSizes):
            list_dic[size].append(index)
            if size == len(list_dic[size]):
                ret_lst.append(list_dic[size])
                del list_dic[size]

        return ret_lst


lst = [3, 3, 3, 3, 3, 1, 3]
s = Solution()
print(s.groupThePeople(lst))
