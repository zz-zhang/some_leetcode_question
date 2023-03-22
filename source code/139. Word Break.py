import enum
from typing import List
import random

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False for _ in s]
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i - len(word)] and s[i - len(word): i] == word:
                    print(i, word, dp[i - len(word)])
                    dp[i] = True
                    break
        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    # s = "baabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # wordDict =["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
    s = ''.join([chr(random.randint(97, 97+26)) for _ in range(300)])
    wordDict = [''.join([chr(random.randint(97, 97+26)) for _ in range(20)]) for _ in range(1000)]
    print(sol.wordBreak(s, wordDict))