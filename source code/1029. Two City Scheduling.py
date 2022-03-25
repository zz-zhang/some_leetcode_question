from random import randint
from typing import *

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs = sorted(costs, key=lambda x:(x[0], x[1]))
        # print(costs)
        res = [(c[0], 0) for c in costs[:n]] + [(c[1], 1) for c in costs[n:]]
        

        max_gain = 1
        idx_a, idx_b = 0, 0
        # print(res, sum([item[0] for item in res]))
        while max_gain > 0:
            max_gain = 0
            for i in range(len(costs)):
                for j in range(i + 1, len(costs)):
                    if res[i][1] != res[j][1]:
                        gain_i = costs[i][res[i][1]] - costs[i][1 - res[i][1]]
                        gain_j = costs[j][res[j][1]] - costs[j][1 - res[j][1]]
                        gain = gain_i + gain_j
                        if gain > max_gain:
                            max_gain = gain
                            idx_a = i
                            idx_b = j
            if max_gain > 0:
                # print(idx_a, idx_b, max_gain)
                res[idx_a] = (costs[idx_a][1 - res[idx_a][1]], 1 - res[idx_a][1])
                res[idx_b] = (costs[idx_b][1 - res[idx_b][1]], 1 - res[idx_b][1])

                # print(res, sum([item[0] for item in res]))
            # breakpoint()
        return sum([item[0] for item in res])

if __name__ == '__main__':
    sol = Solution()
    costs = [[randint(1, 1000), randint(1, 1000)] for _ in range(100)]
    # costs = [[84, 520], [4, 850], [29, 779], [82, 258], [33, 503], [11, 71], [55, 688], [78, 749], [80, 874], [88, 658]]
    print(costs)
    res = sol.twoCitySchedCost(costs)
    print(res)