import string
from random import choice

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = {char: t.count(char) for char in t}
        left = 0
        right = 0
        counter_sub = {char: 0 for char in s}
        min_length = len(s)
        res = [0, len(s)]

        while right < len(s):
            counter_sub[s[right]] += 1
            # if self.covered(counter_t, counter_sub):
            while self.covered(counter_t, counter_sub):
                # breakpoint()
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    res = [left, right]
                counter_sub[s[left]] -= 1
                left += 1
                
            right += 1
        # print(res)
        res_str = s[res[0]: res[1]+1]
        counter_sub = {char: res_str.count(char) for char in res_str}
        # print(res_str)
        # breakpoint()
        if self.covered(counter_t, counter_sub):
            return res_str
        else:
            return ""


    def covered(self, counter_t, counter_sub):
        for char, times in counter_t.items():
            if char not in counter_sub:
                return False
            if counter_sub[char] < times:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "a"
    t = "b"
    # s = ''.join(choice(string.ascii_letters) for _ in range(1000))
    # t = ''.join(choice(string.ascii_letters) for _ in range(10))
    # t = s[10:50]
    # t = t[:5] + t[10:]
    print(s)
    print()
    print(t)
    print()
    print(sol.minWindow(s, t))