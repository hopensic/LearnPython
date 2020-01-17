class Solution:
    def canReach(self, arr: list, start: int) -> bool:
        stacks = [start]
        le = len(arr)
        while True:
            if len(stacks) == 0:
                break
            poped = stacks.pop()
            if arr[poped] == 0:
                return True
            if arr[poped] < 0:
                continue
            small = poped - arr[poped]
            big = poped + arr[poped]
            arr[poped] *= -1

            if -1 < small < le and arr[small] > -1:
                stacks.append(small)
            if -1 < big < le and arr[big] > -1:
                stacks.append(big)
        return False


lst = [3,0,2,1,2]
start1 = 2

s = Solution()
print(s.canReach(lst, start1))
