from collections import Counter


class Solution:
    def commonChars(self, A):
        count_lst = [Counter(chars) for chars in A]
        common_dic = {}
        le = len(count_lst)
        if le == 1:
            return list(A[0])
        for i in range(le - 1):
            if i == 0:
                common_dic = self.cmp(count_lst[i], count_lst[i + 1])
            else:
                common_dic = self.cmp(count_lst[i + 1], common_dic)
        return [x for x in Counter(common_dic).elements()]

    def cmp(self, dic1, common_dic):
        for ck, cv in common_dic.items():
            if ck in dic1:
                common_dic[ck] = min(cv, dic1[ck])
            else:
                common_dic[ck] = 0
        return common_dic


lst =["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]
s = Solution()
print(s.commonChars(lst))
