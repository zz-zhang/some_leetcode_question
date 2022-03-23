from typing import *

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
           return x ** y

class Solution:
    def findSolution(self, customfunction, z: int) -> List[List[int]]:
        res = []
        for x in range(1, 1001):
            for y in range(1, 1001):
                z_ = customfunction.f(x, y)
                if z_ == z:
                    res.append([x, y])
                elif z_ > z:
                    break
        print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    z = 5
    sol.findSolution(CustomFunction(), z)