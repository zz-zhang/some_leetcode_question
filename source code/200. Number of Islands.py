from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, x, y):
        if grid[x][y] != '1':
            return
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        grid[x][y] = '2'
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                self.dfs(grid, next_x, next_y)
        return


if __name__ == '__main__':
    sol = Solution()
    grid = [['0', '1'], ['1', '0']]
    print(sol.numIslands(grid))