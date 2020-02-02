from collections import Counter


class Solution:
    def minSetSize(self, arr: list) -> int:
        counter = Counter(arr)
        k = int(len(arr) / 2)
        lst = [t for t in counter.values()]
        lst.sort(reverse=True)
        sums = 0
        for idx, x in enumerate(lst):
            sums += x
            if sums >= k:
                return idx + 1


arr =[1,2,3,4,5,6,7,8,9,10]

s = Solution()
print(s.minSetSize(arr))
