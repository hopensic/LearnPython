from datetime import datetime


class Solution:
    def stringShift(self, ss: str, shift) -> str:
        le = len(ss)
        left, right = 0, 0
        for lst in shift:
            if lst[0] == 0:
                left += lst[1]
            else:
                right += lst[1]
        if left == right:
            return ss
        elif left > right:
            dif = (left - right) % le
            return ss[dif:] + ss[:dif ]
        else:
            dif = (right - left) % le
            return ss[le - dif:] + ss[:le - dif]


ss = "wpdhhcj"
shift = [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 6]]
t1 = datetime.now()
s = Solution()
print(s.stringShift(ss, shift))
t2 = datetime.now()
print(t2 - t1)
