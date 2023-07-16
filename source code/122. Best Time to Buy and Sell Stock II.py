from typing import List
from random import randint
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit += (prices[sell] - prices[buy])
            buy += 1
            sell += 1
        return profit

if __name__ == '__main__':
    sol = Solution()
    prices = [7,6,4,3,1]
    
    prices = [randint(0, 1000) for _ in range(3000)]
    print(prices)
    print(sol.maxProfit(prices))