from random import randint
from typing import *

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter_top = {n+1: 0 for n in range(6)}
        counter_bottom = {n+1: 0 for n in range(6)}
        counter_duplicated = {n+1: 0 for n in range(6)}

        total_num = len(tops)
        for t, b in zip(tops, bottoms):
            counter_top[t] += 1
            counter_bottom[b] += 1
            if t == b:
                counter_duplicated[t] += 1

        print(counter_top)
        print(counter_bottom)
        print(counter_duplicated)

        res = 2 * 10 ** 4
        for k in range(1, 6 + 1):
            if counter_top[k] + counter_bottom[k] - counter_duplicated[k] != total_num:
                continue
            res = min(res, counter_top[k] - counter_duplicated[k], counter_bottom[k] - counter_duplicated[k])

        return res if res != 2 * 10 ** 4 else -1

if __name__ == '__main__':
    sol = Solution()
    tops = [randint(1,6) for _ in range(100)]
    bottoms = [randint(1,6) for _ in range(100)]
    print(sol.minDominoRotations(tops, bottoms))