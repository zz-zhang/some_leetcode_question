from typing import *

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 1:
            return False

        diff_idx = []
        for idx, (char1, char2) in enumerate(zip(s, goal)):
            if char1 != char2:
                diff_idx.append(idx)

        if len(diff_idx) == 2:
            idx1, idx2 = diff_idx
            if s[idx1] == goal[idx2] and s[idx2] == goal[idx1]:
                return True
            else:
                return False

        if len(diff_idx) != 0:
            return False

        recoder = {}
        for char in s:
            if char in recoder:
                return True
            else:
                recoder[char] = 1
        return False
        
if __name__ == '__main__':
    sol = Solution()
    s = "abcaa"
    goal = "abcbb"
    print(sol.buddyStrings(s, goal))