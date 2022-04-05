from pprint import pprint
from typing import List
from random import randint
from pprint import pprint

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # print(len(mat), len(mat[0]))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = 10 ** 5
        q = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        visited = [[0 for _ in range(len(mat[0]))] for __ in range(len(mat))]
        while len(q) > 0:
            x, y, depth = q[0]
            # print(x, y)
            # visited[x][y] = 1
            for step_x, step_y in directions:
                next_x = x + step_x
                next_y = y + step_y
                if 0 <= next_x < len(mat) and 0 <= next_y < len(mat[0]):
                    if mat[next_x][next_y] != 0:
                        mat[next_x][next_y] = min(mat[next_x][next_y], depth + 1)
                        if visited[next_x][next_y] == 0:
                            q.append((next_x, next_y, depth + 1))
                            visited[next_x][next_y] = 1
            q = q[1:]
        return mat

if __name__ == '__main__':
    sol = Solution()
    n = 10 ** 2
    m = 10 ** 2
    mat = [[1 for _ in range(m)] for __ in range(n)]
    mat[0][0] = 0
    # print(mat)
    mat = sol.updateMatrix(mat)
    print(mat)

