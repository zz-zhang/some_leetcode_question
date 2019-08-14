class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        used = [[0 for _ in __] for __ in matrix]
        x, y = 0, 0
        dir = 0
        m = len(matrix)
        n = len(matrix[0])
        while sum(sum(used, [])) < m * n:
            result.append(matrix[x][y])
            used[x][y] = 1
            if 0 <= x + direction[dir][0] < m and \
                0 <= y + direction[dir][1] < n and \
                used[x + direction[dir][0]][y + direction[dir][1]] == 0:
                x += direction[dir][0]
                y += direction[dir][1]
            else:
                dir = (dir + 1) % 4
                x += direction[dir][0]
                y += direction[dir][1]
        # print(result)
        return result

if __name__ == '__main__':
    sol = Solution()
    matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    # print(sum(sum(matrix, [])))
    print(sol.spiralOrder(matrix))
