from typing import List
from random import randint

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        nums = sorted(nums)
        self.search(nums, len(nums))
        return self.res

    def search(self, nums, length, sub_res=[]): 
        for idx, n in enumerate(nums):
            if idx > 0 and nums[idx - 1] == n:
                continue
            self.res.append(sub_res + [n])
            if length >= 1:
                self.search(nums[idx+1:], length-1, sub_res + [n])
            

if __name__ == '__main__':
    sol = Solution()
    nums = [0]
    nums = [randint(-10, 10) for _ in range(10)]
    print(nums)
    print(sol.subsetsWithDup(nums))
