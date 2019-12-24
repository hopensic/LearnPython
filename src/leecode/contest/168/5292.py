from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: list, k: int) -> bool:
        nums.sort()
        counter = sorted(Counter(nums).items())
        dic = dict(counter)
        while len(dic) > 0:
            # 取第一个元素
            first_key, first_value = next(iter(dic.items()))
            dic[first_key] -= 1
            if dic[first_key] == 0:
                del dic[first_key]
            for i in range(k - 1):
                first_key += 1
                if first_key not in dic:
                    return False
                else:
                    dic[first_key] -= 1
                    if dic[first_key] == 0:
                        del dic[first_key]
        return True


lst = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3
s = Solution()
print(s.isPossibleDivide(lst, 3))
