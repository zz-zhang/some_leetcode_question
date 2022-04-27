from collections import defaultdict
from typing import List


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parents = list(range(len(s)))
        self.rank = [1] * len(s)
        s = [(idx, c) for idx, c in enumerate(list(s))]

        for loc1, loc2 in pairs:
            if not self.connected(loc1, loc2):
                # print(loc1, loc2)
                self.union(loc1, loc2)
                # print(self.parents)

        unions = defaultdict(list)
        locations = defaultdict(list)
        for idx, c in s:
            unions[self.root(idx)].append(c)
            locations[self.root(idx)].append(idx)

        for key in unions.keys():
            unions[key] = sorted(unions[key])
            locations[key] = sorted(locations[key])

        # print(unions)
        # print(locations)
        res = [''] * len(s)

        for key in unions.keys():
            for idx, c in zip(locations[key], unions[key]):
                res[idx] = c
        return ''.join(res)

    def connected(self, n1, n2):
        return self.root(n1) == self.root(n2)

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if self.rank[r1] > self.rank[r2]:
            self.parents[r2] = r1
        elif self.rank[r1] < self.rank[r2]:
            self.parents[r1] = r2

        else:
            self.parents[r2] = r1
            self.rank[r1] += 1

    def root(self, n):
        while n != self.parents[n]:
            n = self.parents[n]
        return n


if __name__ == '__main__':
    sol = Solution()
    s = "cba"
    pairs = [[0,1],[1,2]]
    print(sol.smallestStringWithSwaps(s, pairs))