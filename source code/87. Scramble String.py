class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-1])):
                return True
        return False



if __name__ == '__main__':
    sol = Solution()
    str1 = 'abab'
    str2 = 'bbaa'
    print(sol.isScramble(str1, str2))
