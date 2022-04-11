from typing import List
from random import randint
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        length = m * n
        k = k % length
        # print(n, m)
        # print(len(grid))
        grid = [item for row in grid for item in row]
        print(grid)
        grid = grid[-k:] + grid[:-k]
        print(grid)
        grid = [[grid[i * m + j] for j in range(m)] for i in range(n)]
        return grid

if __name__ == '__main__':
    sol = Solution()
    n = m = 50
    # grid = [[randint(-1000, 1000) for _ in range(m)] for __ in range(n)]
    # k = randint(0, 100)
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 23
    print(grid)
    print(k)
    res = sol.shiftGrid(grid, k)
    # print(res)