from typing import List


class Solution:

    def countSubIslands(self, grid1: List[List[int]],
                        grid2: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    is_sub = self.dfs(grid1, grid2, i, j)
                    print(i, j, is_sub)
                    if is_sub:
                        count += 1
        return count

    def dfs(self, grid1, grid2, x, y):
        if grid2[x][y] != 1:
            return True
        is_sub = True if grid1[x][y] == 1 else False
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        grid2[x][y] = 2
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if 0 <= next_x < len(grid2) and 0 <= next_y < len(grid2[0]):
                is_sub_next = self.dfs(grid1, grid2, next_x, next_y)
                is_sub = is_sub and is_sub_next
        return is_sub


if __name__ == '__main__':
    sol = Solution()
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(sol.countSubIslands(grid1, grid2))
