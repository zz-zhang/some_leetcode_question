from typing import List
from random import randint
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        for char in s:
            if char == '#':
                stack_s = stack_s[:-1]
            else:
                stack_s.append(char)
        for char in t:
            if char == '#':
                stack_t = stack_t[:-1]
            else:
                stack_t.append(char)

        # print(stack_s)
        # print(stack_t)
        if len(stack_s) != len(stack_t):
            return False
        for char_s, char_t in zip(stack_s, stack_t):
            if char_s != char_t:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "#c#"
    t = ""
    print(sol.backspaceCompare(s, t))