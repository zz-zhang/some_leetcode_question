from typing import List
from random import randint

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = [g - c for g, c in zip(gas, cost)]
        if sum(rest) < 0:
            return -1

        res = 0
        curr_rest = 0
        for idx, r in enumerate(rest):
            curr_rest += r
            if curr_rest < 0:
                res = idx + 1
                curr_rest = 0
        return res

if __name__ == '__main__':
    sol = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    # gas = [randint(0, 1000) for _ in range(10000)]
    # cost = [randint(0, 1000) for _ in range(10000)]
    print(gas)
    print(cost)
    print(sol.canCompleteCircuit(gas, cost))