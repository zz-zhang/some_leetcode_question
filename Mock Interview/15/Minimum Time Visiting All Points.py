from typing import *

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for ((x1, y1), (x2, y2)) in zip(points[:-1], points[1:]):
            dis_x = abs(x2 - x1)
            dis_y = abs(y2 - y1)
            # breakpoint()

            if dis_x > 0 and dis_y > 0:
                slope_dis = min(dis_x, dis_y)
                res += slope_dis
                dis_x -= slope_dis
                dis_y -= slope_dis
            res += dis_x
            res += dis_y
            # print(res)
        return res

if __name__ == '__main__':
    sol = Solution()
    points = [[0,0], [1,1], [-1, -1]]
    print(sol.minTimeToVisitAllPoints(points))