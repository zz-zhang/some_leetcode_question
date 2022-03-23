from typing import *

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        recoder = {}
        for candy in candyType:
            if candy not in recoder:
                recoder[candy] = 1
        res = len(recoder.keys()) if len(recoder.keys()) < len(candyType) // 2 else len(candyType) // 2
        return res

if __name__ == '__main__':
    sol = Solution()
    candyType = [1,1,2,2,3,3]
    print(sol.distributeCandies(candyType))