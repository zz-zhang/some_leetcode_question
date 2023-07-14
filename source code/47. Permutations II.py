from typing import List
from random import randint

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums = sorted(nums)
        self.search(nums)
        return self.res

    def search(self, nums, sub_res=[]):
        if len(nums) == 0:
            self.res.append(sub_res)
            return
        for idx, n in enumerate(nums):
            if idx == 0 or nums[idx - 1] != n:
                self.search(nums[:idx] + nums[idx+1:], sub_res + [n])
            

if __name__ == '__main__':
    sol = Solution()
    # nums = [1]
    nums = [randint(-10, 10) for _ in range(8)]
    print(nums)
    print(sol.permuteUnique(nums))
