from pprint import pprint
from random import randint
from typing import List


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac = [[0 for _ in range(m)] for __ in range(n)]
        atl = [[0 for _ in range(m)] for __ in range(n)]

        for i in range(n):
            pac[i][0] = 1
            atl[i][m - 1] = 1
        for i in range(m):
            pac[0][i] = 1
            atl[n - 1][i] = 1

        for x in range(n):
            for y in range(m):
                if pac[x][y] == 1:
                    self.flow(x, y, heights, pac, [(x, y)])
                if atl[x][y] == 1:
                    self.flow(x, y, heights, atl, [(x, y)])

        res = []
        # pprint(pac)
        # pprint(atl)
        for x in range(n):
            for y in range(m):
                if pac[x][y] == atl[x][y] == 1:
                    res.append([x, y])
        return res

    def flow(self, x, y, heights, flow_map, visited=[]):
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if (next_x, next_y) not in visited:
                if 0 <= next_x < len(heights) and 0 <= next_y < len(
                        heights[0]):
                    if flow_map[next_x][next_y] == 0 and heights[next_x][
                            next_y] >= heights[x][y]:
                        flow_map[next_x][next_y] = 1
                        self.flow(next_x, next_y, heights, flow_map,
                                  visited + [(next_x, next_y)])


if __name__ == '__main__':
    sol = Solution()
    n = 1
    m = 1
    # heights = [[2,1],[1,2]]
    heights = [[randint(0, 10**5) for _ in range(m)] for __ in range(n)]
    print(heights)
    print(sol.pacificAtlantic(heights))
