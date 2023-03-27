from typing import List
import random

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        group = [i for i in range(n)]
        for s, e, d in roads:
            s = s - 1
            e = e - 1
            self.disset_merge(group, s, e)
            # print(s, e, group)

        res = 100001
        # print(group)
        for s, e, d in roads:
            s = s - 1
            e = e - 1
            if self.disset_find(group, s) == self.disset_find(group, 0) and d < res:
                res = d

        return res

    def disset_find(self, group, node):
        if group[node] == node:
            return node
        else:
            group[node] = self.disset_find(group, group[node])
            return group[node]

    def disset_merge(self, group, n1, n2):
        group[self.disset_find(group, n1)] = self.disset_find(group, n2) 
            

if __name__ == '__main__':
    sol = Solution()
    n = 13
    roads = [[2,12,1891],[10,9,4138],[11,3,2007],[1,10,9390],[12,8,1915],[6,2,1098],[5,4,2795],[3,13,4562],[9,7,9202],[4,6,6752],[8,11,1480],[7,5,9827]]

    # n = 100000
    # roads =[[random.randint(1, 100000), random.randint(1, 100000), random.randint(1, 10000)]]

    print(sol.minScore(n, roads))