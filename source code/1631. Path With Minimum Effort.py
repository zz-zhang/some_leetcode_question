from collections import defaultdict
from email.policy import default
from pprint import pprint
from typing import List
import heapq
from numpy import insert


class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        min_heap = [(0, (0, 0))]
        visited = set()
        res = 0

        while len(min_heap) > 0:
            effort, (r, c) = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            res = max(effort, res)
            if (r, c) == (row - 1, col - 1):
                break
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for next_r, next_c in directions:
                if 0 <= next_r < row and 0 <= next_c < col and (next_r, next_c) not in visited:
                    effort = abs(heights[r][c] - heights[next_r][next_c])
                    heapq.heappush(min_heap, (effort, (next_r, next_c)))
        return res



if __name__ == '__main__':
    heights = [[1,10,6,7,9,10,4,9]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))
