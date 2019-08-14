class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(0, n)] for __ in range(0, m)]
        for i in range(0, m):
            dp[i][0] = 1
        for i in range(0, n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # for line in dp:
        #     print(line)
        # print(dp[m - 1][n - 1])
        return dp[m - 1][n - 1]
if __name__ == '__main__':
    sol = Solution()
    m, n = 100, 100
    print(sol.uniquePaths(m, n))
