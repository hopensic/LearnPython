class Solution:
    def checkIfExist(self, arr: list) -> bool:
        le = len(arr)
        for i in range(le):
            for j in range(le):
                if i == j:
                    continue
                if arr[j] == 2 * arr[i]:
                    return True

        return False


arr =  [10,2,5,3]
s = Solution()
print(s.checkIfExist(arr))
