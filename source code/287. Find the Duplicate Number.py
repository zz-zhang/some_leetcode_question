from typing import *
import sys
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from array import array
        recoder = array('b', [False] * (10 ** 5 + 1))
        for num in nums:
            if recoder[num] == 1:
                return num
            recoder[num] = 1

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,4,2,2]
    print(sol.findDuplicate(nums))