class Solution:
    def set_to_zero(self, matrix, row, col, m, n):
        length = 1
        while row - length >= 0 or\
                row + length < m or\
                col - length >= 0 or\
                col + length < n:
            if row - length >= 0:
                matrix[row-length][col] = 0
            if row + length < m:
                matrix[row+length][col] = 0
            if col - length >= 0:
                matrix[row][col-length] = 0
            if col + length < n:
                matrix[row][col+length] = 0
            length += 1

    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        set_loc = []
        for row in range(0, m):
            for col in range(0, n):
                if matrix[row][col] == 0:
                    set_loc.append((row, col))

        for (row, col) in set_loc:
            self.set_to_zero(matrix, row, col, m, n)


if __name__ == '__main__':
    sol = Solution()
    matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    sol.setZeroes(matrix)
    for row in matrix:
        print(row)
