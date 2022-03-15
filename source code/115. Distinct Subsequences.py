class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        if len(t) == 0:
            return 1
        dp = [[0 for _ in range(len(t) + 1)] for __ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        # for line in dp:
        #     print(line)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    s = "b"
    t = "b"
    print(sol.numDistinct(s, t))