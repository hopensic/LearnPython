class Solution:
    def numSpecialEquivGroups(self, A):
        cnt = set()
        for word in A:
            k = ''.join(sorted(word[0::2]) + sorted(word[1::2]))
            if k in cnt:
                continue
            else:
                cnt.add(k)
        return len(cnt)


lst = ["abc","acb","bac","bca","cab","cba"]

s = Solution()
print(s.numSpecialEquivGroups(lst))
