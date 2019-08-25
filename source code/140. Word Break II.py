class Solution:
    result = []

    def is_illegal(self, s, word_dict):
        dp = [False for c in s] + [False]
        dp[0] = True
        for i in range(0, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in word_dict:
                    dp[i] = True
        return not dp[len(s)]

    def dfs(self, s, word_dict, sub_res):
        if self.is_illegal(s, word_dict):
            return
        if len(s) == 0:
            self.result.append(sub_res[1:])
        for word in word_dict:
            if s.startswith(word):
                self.dfs(s[len(word):], word_dict, sub_res + ' ' + word)

    def wordBreak(self, s, wordDict):
        self.result = []
        self.dfs(s, wordDict, '')
        return self.result

if __name__ == '__main__':
    sol = Solution()
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(sol.wordBreak(s, wordDict))
