from random import randint
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse=True)
        # print(stones)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones = stones[2:]
            else:
                stones[1] = stones[0] - stones[1]
                stones = sorted(stones[1:], reverse=True)
            # print(stones)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0

if __name__ == '__main__':
    sol = Solution()
    # stones = [81, 432, 964, 431, 78, 443, 416, 635, 420, 903, 155, 665, 905, 296, 752, 627, 631, 681, 817, 222, 42, 244, 134, 893, 450, 737, 858, 988, 962, 978]
    stones = [randint(0, 1000) for _ in range(30)]
    print(stones)
    print(sol.lastStoneWeight(stones))