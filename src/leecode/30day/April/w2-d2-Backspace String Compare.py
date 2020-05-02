from collections import Counter
from _collections import defaultdict
from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

from datetime import datetime


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        len1, len2 = len(S) * -1, len(T) * -1
        p1, p2 = -1, -1
        num_of_well1, num_of_well2 = 0, 0
        while p1 >= len1 or p2 >= len2:
            # num_of_char1, num_of_char2 = 0, 0
            while True:
                if p1 == len1 - 1:
                    break
                if S[p1] == '#':
                    num_of_well1 += 1
                    p1 -= 1
                else:
                    if num_of_well1 > 0:
                        num_of_well1 -= 1
                        p1 -= 1
                    else:
                        break

            while True:
                if p2 == len2 - 1:
                    break
                if T[p2] == '#':
                    num_of_well2 += 1
                    p2 -= 1
                else:
                    if num_of_well2 > 0:
                        num_of_well2 -= 1
                        p2 -= 1
                    else:
                        break
            if p1 < len1:
                break
            if p2 < len2:
                break
            if S[p1] != T[p2]:
                return False
            p1 -= 1
            p2 -= 1

        # 大的循环退出后
        if p1 >= len1 or p2 >= len2:
            return False
        else:
            return True


S = "bxj##tw"
T = "bxj###tw"
t1 = datetime.now()
s = Solution()
print(s.backspaceCompare(S, T))
t2 = datetime.now()
print(t2 - t1)
