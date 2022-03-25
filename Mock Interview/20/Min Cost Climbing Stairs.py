from typing import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [10 ** 7 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        # print(dp)
        return min(dp[-1], dp[-2])

if __name__ == '__main__':
    sol = Solution()
    cost = [100,1,1,1,1,100,1,1,100,1]
    res = sol.minCostClimbingStairs(cost)
    print(res)