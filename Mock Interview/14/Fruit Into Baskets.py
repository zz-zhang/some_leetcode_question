from random import randint
from typing import *

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        i = 1
        while i < len(fruits) and fruits[i] == fruits[0]:
            i += 1
        if i == len(fruits):
            return len(fruits)

        start = 0
        f1 = fruits[start]
        f2 = fruits[i]
        res = i - start
        while i < len(fruits):
            # breakpoint()
            if fruits[i] != f1 and fruits[i] != f2:
                # print(f1, f2, start, i)
                res = max(res, i - start)
                if fruits[i-1] == f1:
                    f2 = fruits[i]
                else:
                    f1 = f2
                    f2 = fruits[i]
                start = i - 1
                while start > 0 and fruits[start-1] == fruits[start]:
                    start -= 1
                if start == 1 and fruits[start] == fruits[0]:
                    start = 0
            i += 1
        else:
            # print(f1, f2, start)
            res = max(res, i - start)
        return res


if __name__ == '__main__':
    sol = Solution()
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    fruits = [1,0,1,4,1,4,1,2,3]


    print(sol.totalFruit(fruits))