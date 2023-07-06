from typing import List
from random import randint

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        keys = {chr(96+i): (30001 ** (i - 1)) for i in range(1, 27)}
        
        hash_p = sum([keys[char] for char in p])
        left, right = 0, len(p)
        all_hash_s = [sum(keys[char] for char in s[left: right])]
        left += 1
        right += 1
        while right <= len(s):
            # breakpoint()
            all_hash_s.append(all_hash_s[left-1] - keys[s[left-1]] + keys[s[right-1]])
            left += 1
            right += 1

        res = []
        for idx, hash_s in enumerate(all_hash_s):
            if hash_s == hash_p:
                res.append(idx)
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    s = ''.join([chr(randint(97, 97+25)) for _ in range(30000)])
    p = ''.join([chr(randint(97, 97+25)) for _ in range(2)])
    print(s)
    print(p)
    print(sol.findAnagrams(s, p))