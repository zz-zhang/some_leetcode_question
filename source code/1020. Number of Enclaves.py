from typing import List


class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    enclave, area = self.dfs(grid, i, j)
                    # print(i, j, enclave, area)
                    if enclave:
                        count += area
        return count

    def dfs(self, grid, x, y):
        area = 1
        if grid[x][y] != 1:
            return True, 0
        enclave = True
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        grid[x][y] = 2
        if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
            enclave = False
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                enclave_next, area_next = self.dfs(grid, next_x, next_y)
                enclave = enclave and enclave_next
                area += area_next
        return enclave, area


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    print(sol.numEnclaves(grid))
    