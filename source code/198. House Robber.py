from typing import List
from random import randint

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums)+1)]
        # dp[i][0] -> the earning if we rob the ith house
        # dp[i][0] -> the earning if we don't rob the ith house
        for idx, num in enumerate(nums):
            idx = idx + 1
            dp[idx][0] = dp[idx-1][1] + num
            dp[idx][1] = max(dp[idx-1][0], dp[idx-1][1])

        # print(dp)
        return max(dp[-1][:])
            

if __name__ == '__main__':
    sol = Solution()
    nums = [2,7,9,3,1]
    nums = [randint(0, 400) for _ in range(50)]
    print(nums)
    print(sol.rob(nums))