class Solution:
    def isSubsequence(self, s: str, t: str):
        if len(s) == 0:
            return True
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i < len(s):
            return False
        if s[-1] != t[j - 1]:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "a"
    t = "a"
    print(sol.isSubsequence(s, t))
        