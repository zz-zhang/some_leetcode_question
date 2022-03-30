from random import randint
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i < j - 1:
            # breakpoint()
            mid = (i + j) // 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                j = mid
            else:
                i = mid
            # print(i, j)
        # print(matrix[i][0], matrix[j][0])
        # print(target)

        line = matrix[j] if matrix[j][0] <= target else matrix[i]
        i = 0
        j = len(line) - 1
        while i < j - 1:
            mid = (i + j) // 2
            if target == line[mid]:
                return True
            if target < line[mid]:
                j = mid
            else:
                i = mid
            # print(i, j)
        if line[i] == target or line[j] == target:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    matrix = [[1], [3]]
    # print(matrix)
    target = 3
    print(sol.searchMatrix(matrix, target))