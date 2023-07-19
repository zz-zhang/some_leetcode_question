from typing import List
from pprint import pprint

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for j in range(target + 1):
            for num in nums:
                if j - num >= 0:
                    dp[j] += dp[j - num]
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    nums = [9]
    target = 3
    print(sol.combinationSum4(nums, target))