from typing import List
from random import randint
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i+1:]):
                j = i + 1 + j
                if num_j > num_i:
                    dp[j] = max(dp[j], dp[i] + 1)
        # print(dp)
        return max(dp)

if __name__ == '__main__':
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18,4,5,6,7]
    nums = [randint(-10000, 10000) for _ in range(1)]
    print(nums)
    print(sol.lengthOfLIS(nums))
