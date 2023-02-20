from typing import List
from random import randint

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for idx, manager in enumerate(manager):
            if manager != -1:
                graph[manager].append(idx)
        
        res = 0
        q = [(headID, 0)]
        while len(q) > 0:
            manager, time = q[0]
            res = max(res, time)
            for subordinate in graph[manager]:
                q.append((subordinate, time + informTime[manager]))
            q = q[1:]
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 6
    headID = randint(0, n)
    manager = [2,2,-1,2,2,2]
    informTime = [0,0,1,0,0,0]
    print(sol.numOfMinutes(n, headID, manager, informTime))
