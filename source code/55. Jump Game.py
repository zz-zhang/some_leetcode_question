from typing import List
from random import randint
# class Solution:
#   ''' 
#       2019/08
#   '''
#     def reachable(self, nums, target, max_length, accessable):
#         # print(target)
#         if target == 0:
#             return True
#         for i in range(max_length, 0, -1):
#             if target - i >= 0 and nums[target - i] >= i and accessable[target - i] == 1:
#                 if self.reachable(nums, target - i, max_length, accessable):
#                     return True
#         accessable[target] = 0
#         return False

#     def canJump(self, nums) -> bool:
#         max_length = max(nums)
#         accessable = [1 for _ in nums]
#         return self.reachable(nums, len(nums) - 1, max_length, accessable)

class Solution:
    '''
        2023/07, greedy
    '''
    def canJump(self, nums: List[int]) -> bool:
        arrived = [False for _ in nums]
        arrived[0] = True
        for idx, n in enumerate(nums):
            if arrived[idx]:
                for i in range(min(idx+n, len(nums)-1), idx, -1):
                    if not arrived[i]:
                        arrived[i] = True
                    else:
                        break
                
            # print(arrived)
        return arrived[-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1,0,4]
    # nums = [randint(0, 100000) for _ in range(10000)]
    print(nums)
    print(sol.canJump(nums))
