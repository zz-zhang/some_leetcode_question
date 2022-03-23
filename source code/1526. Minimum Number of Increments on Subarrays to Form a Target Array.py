from random import randint
from typing import *

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # return self.brute(target) # TLE
        res = 0
        prev = 0
        for num in target:
            res += max(num - prev, 0)
            prev = num
        return res
    
    def brute(self, target):
        res = 0
        all_zero = False
        while not all_zero:
            i = 0
            all_zero = True
            # print('-')
            while i < len(target):
                min_val = 10 ** 6
                min_idx = i
                while i < len(target) and target[i] == 0:
                    i += 1
                if i < len(target):
                    all_zero = False
                # print(i, len(target), all_zero)
                start = i
                while i < len(target) and target[i] != 0:
                    if target[i] < min_val:
                        min_val = target[i]
                        min_idx = i
                    i += 1
                # print(start, i, min_val)
                if start != i:
                    for idx in range(start, i):
                        target[idx] -= min_val
                    res += min_val
                # print(target)
                i += 1
                # print(i)
        # print(res)
        return res
            

if __name__ == '__main__':
    sol = Solution()
    # target = [3,0,3,1,3]
    target = [randint(1, 10 ** 5) for _ in range(1000)]
    print(target)
    sol.minNumberOperations(target)