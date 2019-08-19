class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dic = [str(_) for _ in range(1, 27)]
        dp = [0 for item in s]
        single_end = [0 for item in s]
        single_end[0] = 1
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i: i + 1] in dic:
                dp[i] = dp[i - 1]
                single_end[i] = dp[i - 1]
            else:
                single_end[i] = 0
            if s[i - 1:i + 1] in dic:
                dp[i] += single_end[i - 1]
        # print(dp)
        # print(single_end)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    s = '1012'
    print(sol.numDecodings(s))
