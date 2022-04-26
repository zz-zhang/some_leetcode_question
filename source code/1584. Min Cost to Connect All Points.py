from collections import defaultdict
from random import randint
from typing import List


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for idx1, (x1, y1) in enumerate(points):
            for idx2, (x2, y2) in enumerate(points[idx1 + 1:]):
                distances.append((idx1, idx1 + idx2 + 1, abs(x1 - x2) + abs(y1 - y2)))
        distances = sorted(distances, key=lambda x: x[-1])
        # print(distances)

        parent = list(range(len(points)))
        rank = [1] * len(points)
        result = 0
        # print(unions)
        for p1, p2, dis in distances:
            if not self.connected(parent, p1, p2):
                self.union(parent, rank, p1, p2)
                result += dis
            # print(p1, p2)
        return result
    
    def get_root(self, parent, node):
        while node != parent[node]:
            node = parent[node]
        return node

    def connected(self, parent, n1, n2):
        return self.get_root(parent, n1) == self.get_root(parent, n2)

    def union(self, parent, rank, n1, n2):
        root1 = self.get_root(parent, n1)
        root2 = self.get_root(parent, n2)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] > rank[root2]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            rank[root2] += 1

if __name__ == '__main__':
    sol = Solution()
    points = [[3,12],[-2,5],[-4,1]]
    points = [[randint(-10 ** 6, 10 ** 6), randint(-10 ** 6, 10 ** 6)] for _ in range(1000)]
    print(points)
    print(sol.minCostConnectPoints(points))