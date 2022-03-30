from typing import List
from pprint import pprint


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        orig_color = image[sr][sc]
        visited = [[0 for _ in range(len(image[0]))]
                   for __ in range(len(image))]
        self.dfs(image, sr, sc, newColor, orig_color, visited)
        return image

    def dfs(self, image, x, y, new_color, orig_color, visited):
        if image[x][y] != orig_color or visited[x][y] == 1:
            return

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        image[x][y] = new_color
        visited[x][y] = 1
        for step_x, step_y in directions:
            next_x = x + step_x
            next_y = y + step_y
            if 0 <= next_x < len(image) and 0 <= next_y < len(image[0]):
                self.dfs(image, next_x, next_y, new_color, orig_color, visited)
        return


if __name__ == '__main__':
    sol = Solution()
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 0
    sc = 1
    newColor = 1
    pprint(sol.floodFill(image, sr, sc, newColor))