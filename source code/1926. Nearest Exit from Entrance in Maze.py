from pprint import pprint
from typing import List


class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        q = [(entrance[0], entrance[1], 0)]
        visited = [[0 for _ in range(m)] for __ in range(n)]
        visited[entrance[0]][entrance[1]] = 1
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        while len(q) > 0:
            x, y, depth = q[0]
            for step_x, step_y in directions:
                next_x = x + step_x
                next_y = y + step_y
                if 0 <= next_x < n and 0 <= next_y < m:
                    if maze[next_x][next_y] == '.' and visited[next_x][next_y] == 0:
                        if next_x == 0 or next_x == n - 1 or next_y == 0 or next_y == m - 1:
                            # print(next_x, next_y)
                            return depth + 1
                        else:
                            visited[next_x][next_y] = 1
                            q.append((next_x, next_y, depth + 1))
            q = q[1:]
        return -1
            


if __name__ == '__main__':
    sol = Solution()
    maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
    entrance = [0, 1]
    pprint(maze)
    print(sol.nearestExit(maze, entrance))
