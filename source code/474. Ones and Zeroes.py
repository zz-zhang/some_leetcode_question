from typing import List
from pprint import pprint

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        weight = [(s.count('0'), s.count('1')) for s in strs]
        # print(weight)
        dp = [[[0 for _ in range(n + 1)] for __ in range(m + 1)] for ___ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            w_0, w_1 = weight[i - 1]
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    if j - w_0 >= 0 and k - w_1 >= 0:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - w_0][k - w_1] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[-1][-1][-1]

if __name__ == '__main__':
    sol = Solution()
    strs = ["10","0","1"]
    m = 1
    n = 1
    print(sol.findMaxForm(strs, m, n))