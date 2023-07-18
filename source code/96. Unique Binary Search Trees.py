class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i]: number of BSTs when n==i
        if n <= 2:
            return n
        dp = [1, 1, 2]
        for i in range(3, n + 1):
            sub_res = 0
            for j in range(0, i):
                sub_res += dp[j] * dp[i - j - 1]    # #_of_left_subtree * #_of_right_subtree
            dp.append(sub_res)
            # print(i, dp)
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    n = 10
    print(sol.numTrees(n))