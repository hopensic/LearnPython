from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def frequencySort(self, s: str) -> str:

        a = Counter(s)
        o=a.most_common()

        return ''.join([t[0] * t[1] for t in sorted(Counter(s).items(), key=lambda item: item[1], reverse=True)])


strs = "aabbcccdeeeee"
s1 = Solution()
print(s1.frequencySort(strs))
