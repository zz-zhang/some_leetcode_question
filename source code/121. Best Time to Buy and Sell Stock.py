from typing import List
import random

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for p in prices:
            res = max(res, p - min_price)
            # print(p, min_price, res)
            if p < min_price:
                min_price = p
        return res

if __name__ == '__main__':
    sol = Solution()
    prices = [0,1,5,3,6,4]
    prices = [random.randint(0, 10000) for _ in range(1000)]
    print(prices)
    print(sol.maxProfit(prices))