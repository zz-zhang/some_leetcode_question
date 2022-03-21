from typing import *
from pprint import pprint

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        min_sub = nums[0]
        max_sub = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_sub, max_sub = max_sub, min_sub
            min_sub = min(min_sub * num, num)
            max_sub = max(max_sub * num, num)
            ans = max(ans, max_sub)
            print(min_sub, max_sub, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,-2,4,4,0,-1]
    print(sol.maxProduct(nums))