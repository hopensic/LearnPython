from datetime import datetime

'''
tag: ^442 ^medium ^array
name: ^(Find All Duplicates in an Array)
'''


class Solution:
    def findDuplicates(self, nums):
        ret_lst = []
        for idx, num in enumerate(nums):
            if num == -1 or num == 0:
                continue
            if num == nums[num - 1]:
                if idx != num - 1:
                    ret_lst.append(num)
                    nums[idx] = -1
                    nums[num - 1] = -1
                continue
            else:
                pre = num
                pre_index = idx
                post = nums[pre - 1]
                post_index = pre - 1
                nums[pre_index] = 0

                while True:
                    if post == 0 or post == -1:
                        nums[post_index] = pre
                        break
                    # 继续循环
                    nums[post_index] = pre
                    pre_index = post_index
                    pre = post
                    post_index = post - 1
                    post = nums[post_index]
                    if pre == post:
                        ret_lst.append(post)
                        nums[post_index] = -1
                        break

        return ret_lst


# lst = [4, 3, 2, 7, 8, 2, 3, 1]
# lst = [10,2,5,10,9,1,1,4,3,7]
lst = [10, 2, 5, 10, 9, 1, 1, 4, 3, 7]

t1 = datetime.now()
s = Solution()
print(s.findDuplicates(lst))
t2 = datetime.now()
print(t2 - t1)
