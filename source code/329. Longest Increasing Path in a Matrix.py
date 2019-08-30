class Solution:
    def longestIncreasingPath(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        flatten = sum(matrix, [])
        indices = [n[0] for n in sorted(enumerate(flatten), key=lambda x:x[1])]
        indices = [(int(index / col), index % col) for index in indices]

        min_num = matrix[indices[0][0]][indices[0][1]]
        padding = [[min_num - 1 for _ in range(col + 2)]] +\
                  [[min_num - 1] + line + [min_num - 1] for line in matrix] +\
                  [[min_num - 1 for _ in range(col + 2)]]


        dp = [[1 for c in range(col + 2)] for r in range(row + 2)]
        for r in range(row + 2):
            dp[r][0] = dp[r][-1] = 0
        for c in range(col + 2):
            dp[0][c] = dp[-1][c] = 0

        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for (r, c) in indices:
            for d in dir:
                if padding[r + 1][c + 1] > padding[r + 1 + d[0]][c + 1 + d[1]]:
                    dp[r + 1][c + 1] = max(dp[r + 1][c + 1], dp[r + 1 + d[0]][c + 1 + d[1]] + 1)


        result = 0
        for line in dp:
            # print(line)
            result = max(line) if max(line) > result else result
        return result

if __name__ == '__main__':
    sol = Solution()
    matrix =[
[]
]
    print(sol.longestIncreasingPath(matrix))
