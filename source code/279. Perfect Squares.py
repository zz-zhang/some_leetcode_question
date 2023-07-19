from typing import List
from pprint import pprint
import math

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [0xffffffff for _ in range(n + 1)]
        dp[0] = 0
        for num in squares:
            for i in range(num, n + 1):
                dp[i] = min(dp[i], dp[i - num] + 1)
            # print(num, dp)
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    n = 10000
    print(sol.numSquares(n))