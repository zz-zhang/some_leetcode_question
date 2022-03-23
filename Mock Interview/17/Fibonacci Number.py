from typing import *

class Solution:
    def fib(self, n: int) -> int:
        res = [0, 1]
        if n <= 1:
            return res[n]
        
        for i in range(2, n + 1):
            res.append(res[-1] + res[-2])
        return res[-1]

if __name__ == '__main__':
    sol = Solution()
    n = 0
    print(sol.fib(n))