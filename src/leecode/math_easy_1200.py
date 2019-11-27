class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        compared = abs(arr[0] - arr[1])
        ret_lst = [[arr[0], arr[1]]]
        le = len(arr)
        for i in range(1, le - 1):
            t = abs(arr[i] - arr[i + 1])
            if t < compared:
                compared = t
                ret_lst.clear()
                ret_lst.append([arr[i], arr[i + 1]])
            elif t == compared:
                ret_lst.append([arr[i], arr[i + 1]])
        return ret_lst


lst = [3, 8, -10, 23, 19, -4, -14, 27]
s = Solution()
print(s.minimumAbsDifference(lst))
