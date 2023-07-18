from typing import List
from pprint import pprint

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return 0
        if (target + sum(nums)) % 2 == 1:
            return 0
        sum_pos = (target + sum(nums)) // 2
        if sum_pos < 0:
            return 0
        dp = [[0 for _ in range(sum_pos + 1)] for __ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(sum_pos + 1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i-1]]
                
            
        # pprint(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    nums = [100]
    # nums = [1,1,1,1,1]
    target = -200
    print(sol.findTargetSumWays(nums, target))