from platform import java_ver
from typing import List

from random import randint


class Solution:

    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            res = max(res, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    height = [randint(0, 10 ** 4) for _ in range(2)]
    print(height)
    print(sol.maxArea(height))