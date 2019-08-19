class Solution:
    def count(self, s):
        if len(s) == 0:
            self.res += 1
            return
        for length in range(1, 3):
            if length <= len(s):
                if s[:length] in self.dic:
                    self.count(s[length:])

    def numDecodings(self, s: str) -> int:
        self.dic = [str(_) for _ in range(1, 27)]
        self.res = 0
        self.count(s)
        return self.res

if __name__ == '__main__':
    sol = Solution()
    s = '37'
    print(sol.numDecodings(s))
