from typing import List
from pprint import pprint

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
            split stones into two parts, where to make abs(sum(part1)-sum(part2)) be minimum.
            similar with Q416, we have a backpack with capacity of sum(stones)//2, and we put stones in it as part1.
            we need to maxmize part1 to make it close to sum(stones)//2
        '''
        # print(sum(stones))
        capacity = sum(stones) // 2
        dp = [[0 for _ in range(capacity + 1)] for __ in range(len(stones) + 1)]
        for idx, num in enumerate(stones):
            idx = idx + 1
            for capa in range(1, capacity + 1):
                if capa-num >= 0:
                    dp[idx][capa] = max(dp[idx-1][capa], dp[idx-1][capa-num]+num)
                else:
                    dp[idx][capa] = dp[idx-1][capa]
        # pprint(dp)
        return abs(2 * dp[-1][-1] - sum(stones))

if __name__ == '__main__':
    sol = Solution()
    stones = [31,26,33,21,40]
    print(sol.lastStoneWeightII(stones))