from typing import *
from pprint import pprint

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for __ in range(n)]
        res[0][0] = 1
        current = 2
        i = 0
        j = 0
        while current <= n * n:
            while j + 1 < n and res[i][j + 1] == 0:
                j += 1
                res[i][j] = current
                current += 1
            while i + 1 < n and res[i + 1][j] == 0:
                i += 1
                res[i][j] = current
                current += 1
            while j - 1 >= 0 and res[i][j - 1] == 0:
                j -= 1
                res[i][j] = current
                current += 1
            while i - 1 >= 0 and res[i - 1][j] == 0:
                i -= 1
                res[i][j] = current
                current += 1
        # pprint(res)
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 20
    print(sol.generateMatrix(n))