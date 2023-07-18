class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1, 1]
        for idx in range(2, n+1):
            sub_res = 1
            for idx2 in range(2, idx):
                sub_res = max(sub_res, idx2 * dp[idx - idx2], (idx - idx2) * idx2)
                # print(idx, idx2, idx - idx2, sub_res)

            dp.append(sub_res)
            # print(dp)
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    n = 9
    print(sol.integerBreak(n))
