class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # (r, c) -> (c, n - 1 - r)
        n = len(matrix)
        new_matrix = [[__ for __ in _] for _ in matrix]
        # print(n)
        for r in range(0, n):
            for c in range(0, n):
                matrix[c][r] = new_matrix[n-1-r][c]

        # for row in matrix:
        #     print(row, '\n')


if __name__ == '__main__':
    sol = Solution()
    matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

    sol.rotate(matrix)
