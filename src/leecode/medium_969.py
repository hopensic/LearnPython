from datetime import datetime

'''
tag: ^969 ^medium ^array  ^sort
name: ^(Pancake Sorting)
'''


class Solution:
    def pancakeSort(self, A: list) -> list:
        le = len(A)
        ret_lst = []
        sorted_lst = sorted(A, reverse=True)
        for idx, num in enumerate(sorted_lst):
            if A[(-1) * (idx + 1)] == num:
                continue
            else:
                # 找到最大的位置
                idx_max_num = A[:-1].index(num)
                # 如果最大的位置不在第一个，需要将它移到第一个，将最大的数换到第一个
                if idx_max_num > 0:
                    ret_lst.append(idx_max_num + 1)
                    for j in range(int((idx_max_num + 1) / 2)):
                        A[j], A[idx_max_num - j] = A[idx_max_num - j], A[j]
                print(A)

                # 依次循环 将第一个换到最后，倒数第二......
                if idx == 0:
                    ret_lst.append(le)
                    A.reverse()
                    print(A)
                else:
                    ret_lst.append(le - idx)
                    for j in range(int((le - idx) / 2)):
                        A[j], A[le - 1 - idx - j] = A[le - 1 - idx - j], A[j]
                    print(A)

        return ret_lst


lst = [3,7,6,1,8,4,2,9,5]

t1 = datetime.now()
s = Solution()
print(s.pancakeSort(lst))
t2 = datetime.now()
print(t2 - t1)
