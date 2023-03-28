from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            idx = 0
            while idx < min(len(res), len(s)):
                if res[idx] != s[idx]:
                    res = res[:idx]
                    break
                idx += 1
            else:
                res = res[:idx]
            print(s, res)

        return res

if __name__ == '__main__':
    sol = Solution()
    strs = ["flower","flow","flight"]
    print(sol.longestCommonPrefix(strs))