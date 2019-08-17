class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(0, len(p) + 1)] for __ in range(0, len(s) + 1)]
        dp[0][0] = True
        for p_index in range(0, len(p)):
            if p[p_index] != '*':
                break
            dp[0][p_index + 1] = True
        for p_i in range(0, len(p)):
            for s_i in range(0, len(s)):
                if p[p_i] == '*':
                    dp[s_i + 1][p_i + 1] = dp[s_i][p_i] or dp[s_i + 1][p_i] or dp[s_i][p_i + 1]
                elif p[p_i] in {s[s_i], '?'}:
                    dp[s_i + 1][p_i + 1] = dp[s_i][p_i]
                else:
                    dp[s_i + 1][p_i + 1] = False
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    s = 'abac'
    p = 'a*bc'
    print(sol.isMatch(s, p))
