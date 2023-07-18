from typing import List
from pprint import pprint

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        capacity = sum(nums) // 2
        dp = [[0 for _ in range(capacity + 1)] for __ in range(len(nums) + 1)]
        for idx, num in enumerate(nums):
            idx = idx + 1
            for capa in range(1, capacity + 1):
                if capa-num >= 0:
                    dp[idx][capa] = max(dp[idx-1][capa], dp[idx-1][capa-num]+num)
                else:
                    dp[idx][capa] = dp[idx-1][capa]
        # pprint(dp)
        if dp[-1][-1] == sum(nums) // 2:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    nums = [1,5,10,6]
    print(sol.canPartition(nums))