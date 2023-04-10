from typing import List
from random import randint
import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
    
        nums, repeatable = self.merge_lst(nums)
        print(nums)
        while repeatable:
            nums, repeatable = self.merge_lst(nums)
            print(nums)
        return max(nums)
    
    def merge_lst(self, nums):
        start = 0
        res = []
        repeatable = False
        while start < len(nums):
            end = start + 1
            while end < len(nums):
                avg = math.ceil(sum(nums[start: end]) / (end - start))
                if nums[end] >= nums[start] and nums[end] >= avg:
                    end += 1
                else:
                    break
            avg = math.ceil(sum(nums[start: end]) / (end - start))
            res.append(avg)
            print(res, start, end)
            if len(res) > 1 and res[-1] > res[-2]:
                repeatable = True
            # print(nums[start:end], res)
            start = end
        print('-')
        return res, repeatable

if __name__ == '__main__':
    sol = Solution()
    nums = [13,13,20,0,8,9,9]
    # nums = [randint(0, 1000000000) for _ in range(100000)]
    # print(nums)
    print(sol.minimizeArrayValue(nums))