from random import randint
from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for idx, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((idx, temp))
            else:
                day, prev_temp = stack[-1]
                while len(stack) > 0 and temp > prev_temp:
                    # print(len(stack))
                    res[day] = idx - day
                    stack.pop()     # TLE if use "stack = stack[:-1]"
                    if len(stack) > 0:
                        day, prev_temp = stack[-1]

                stack.append((idx, temp))
            # print(stack)
            # print(res)
        return res

if __name__ == '__main__':
    sol = Solution()
    temperatures = [randint(30, 30) for _ in range(10 ** 5)] + [31]
    temperatures = [73,74,75,71,69,72,76,73]
    # print(temperatures)
    sol.dailyTemperatures(temperatures)