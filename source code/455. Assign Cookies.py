from typing import List
from random import randint
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        g_idx = len(g) - 1
        s_idx = len(s) - 1
        res = 0
        while g_idx >=0 and s_idx >= 0:
            if s[s_idx] >= g[g_idx]:
                res += 1
                g_idx -= 1
                s_idx -= 1
            else:
                g_idx -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    g = [1,2,3]
    s = [1, 1]
    # g = [randint(1, 2**31-1) for _ in range(300)]
    # s = [randint(1, 2**31-1) for _ in range(300)]
    print(g)
    print(s)
    print(sol.findContentChildren(g, s))