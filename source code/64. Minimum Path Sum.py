import random
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 
        return grid[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    inp = [[1,2,3],[4,5,6]]
    # inp = [[random.randint(0, 100) for _ in range(200)] for __ in range(200)]
    print(sol.minPathSum(inp))