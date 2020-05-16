from collections import Counter, defaultdict
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        judge_dic = defaultdict(list)
        no_judge_set = set()
        for lst in trust:
            no_judge_set.add(lst[0])
            judge_dic[lst[1]].append(lst[0])
        all_people = set(list(range(1, N + 1)))

        possible_judge = all_people - no_judge_set

        if len(possible_judge) == 0:
            return -1

        for k, v in judge_dic.items():
            if len(v) == N - 1 and k in possible_judge:
                return k
        return -1


N = 1
arr = [[]]
t1 = datetime.now()
s1 = Solution()
print(s1.findJudge(N, arr))
t2 = datetime.now()
print(t2 - t1)
