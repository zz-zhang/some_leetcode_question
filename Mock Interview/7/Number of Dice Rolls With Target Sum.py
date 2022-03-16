from pprint import pprint
class Solution:
    def numRollsToTarget(self, n, k, target):
        dp = [[0 for __ in range(0, target+1)] for _ in range(n)]
        for face in range(1, min(target+1, k+1)):
            dp[0][face] = 1
        for num in range(1, n):
            for tgt in range(1, target+1):
                dp[num][tgt] = int(sum(dp[num-1][max(0,tgt-k): tgt]) % (1e9+7))
        return dp[-1][-1]
    
    # @lru_cache(None)
    # def dp(self, n, k, target):
    #     if n == 0 and target == 0:
    #         return 1
    #     if target < 0 or n == 0:
    #         return 0

    #     return int(sum([self.dp(n-1, k, target-face) for face in range(1, k+1)]) % (1e9 + 7))



    def dfs(self, n, k, target, res=0):
        # print(n, k, target)
        if n == 1 and k >= target:
            return 1
        for num in range(1, k + 1):
            res += self.dfs(n-1, k, target-num)
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 1
    k = 6
    target = 3
    print(sol.numRollsToTarget(n, k, target))
        