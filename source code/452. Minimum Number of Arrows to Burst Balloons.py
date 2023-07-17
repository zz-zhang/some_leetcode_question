from typing import List
from random import randint, choice

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        # print(points)

        res = 0
        idx = len(points) - 1
        while idx >= 0:
            s, e = points[idx]
            next_idx = idx - 1
            while next_idx >= 0:
                ns, ne = points[next_idx]
                if ne < s:
                    res += 1
                    break
                next_idx -= 1
            else:
                res += 1
            idx = next_idx
        return res

if __name__ == '__main__':
    sol = Solution()
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(points)
    print(sol.findMinArrowShots(points))