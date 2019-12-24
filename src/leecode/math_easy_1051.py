


'''

tag: ^1051 ^easy ^math
name:



'''

class Solution:
    def heightChecker(self, heights: list) -> int:
        return len(list((filter(lambda t: (t[0] != t[1]), zip(heights, sorted(heights))))))


lst = [1, 8, 2, 7, 4, 6, 2, 1, 3]

s = Solution()
print(s.heightChecker(lst))
