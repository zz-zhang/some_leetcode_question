from typing import List
import random

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for row, line in enumerate(triangle[1:]):
            row = row + 1
            for col, num in enumerate(line):
                if col - 1 >= 0 and col < row:
                    triangle[row][col] = num + min(triangle[row-1][col-1], triangle[row-1][col])
                elif col < row:
                    triangle[row][col] = num + triangle[row-1][col]
                else:
                    triangle[row][col] = num + triangle[row-1][col-1]
        print(triangle)
        return min(triangle[-1])

if __name__ == '__main__':
    sol = Solution()
    triangle = [[-1],[3,2],[1,-2,-1]]

    # triangle = [[random.randint(-10, 10) for _ in range(row)] for row in range(1, 10)]
    print(triangle)
    print(sol.minimumTotal(triangle))