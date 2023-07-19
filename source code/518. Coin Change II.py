from typing import List
from pprint import pprint

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
            # print(coin, dp)
        
        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    amount = 10
    coins = [10]
    print(sol.change(amount, coins))