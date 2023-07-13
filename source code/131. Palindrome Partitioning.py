from typing import List
from random import randint

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.search(s)
        return self.res

    def search(self, s, sub_res=[]):
        if len(s) == 0:
            self.res.append(sub_res)
            return
        for end in range(1, len(s) + 1):
            if self.is_palindrome(s[:end]):
                self.search(s[end:], sub_res + [s[:end]])
        

    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "a"
    print(s)
    print(sol.partition(s))
