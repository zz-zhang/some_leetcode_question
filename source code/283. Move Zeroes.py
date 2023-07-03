from typing import List
from random import randint

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        faster, slower = 0, 0
        while faster < len(nums):
            nums[slower] = nums[faster]

            if nums[faster] == 0:
                faster += 1
            else:
                faster += 1
                slower += 1
        #     print(nums)
        # print(nums)
        for idx in range(slower, len(nums)):
            nums[idx] = 0
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [randint(-1000, 1000) for _ in range(1000)] + [0] * 100
    # nums = [randint(1, int(1e4)) for _ in range(1000)]
    print(nums)
    print(sol.moveZeroes(nums))