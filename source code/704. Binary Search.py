from typing import *
from random import randint
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if i != mid:
                    i = mid
                else:
                    i += 1
            else:
                if j != mid:
                    j = mid
                else:
                    j -= 1
        if nums[i] == target:
            return i
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    # nums =  [-1,0,3,5,9,12]
    nums = sorted(list(set([randint(-(10 ** 4), 10 ** 4) for _ in range(10 ** 4)])))
    target = nums[100]
    print(nums)
    print(sol.search(nums, target))

        