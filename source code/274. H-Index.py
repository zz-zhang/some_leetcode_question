from typing import List
from random import randint

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        res = 0
        for idx, citation in enumerate(citations):
            res = max(res, min(idx+1, citation))
        return res

if __name__ == '__main__':
    sol = Solution()
    citations = [1,3,1]
    citations = [randint(0, 1000) for _ in range(100)]
    print(citations)
    print(sol.hIndex(citations))