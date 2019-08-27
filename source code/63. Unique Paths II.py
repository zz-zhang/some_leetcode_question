class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid is None:
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]) + 1)] for __ in range(len(obstacleGrid) + 1)]
        if obstacleGrid[0][0] == 0:
            dp[1][1] = 1
        else:
            dp[1][1] = 0
        for i in range(1, len(obstacleGrid) + 1):
            for j in range(1, len(obstacleGrid[0]) + 1):
                if i == j == 1:
                    continue
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # for line in dp:
        #     print(line)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    grid = [[1]]
    print(sol.uniquePathsWithObstacles(grid))
