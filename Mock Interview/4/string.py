'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

class Solution:
    def gcdOfStrings(self, str1, str2):
        res1 = self.cdOfString(str1)
        res2 = self.cdOfString(str2)
        # print(res1, res2)
        for r1 in res1:
            for r2 in res2:
                if self.strEqule(r1, r2):
                    return r1
        return ''

    def cdOfString(self, s):
        res = []
        for idx in range(1, len(s)):
            sub_res = s[:idx]
            length = len(sub_res)

            idx2 = idx
            flag = True
            while idx2 < len(s):
                if not self.strEqule(sub_res, s[idx2: idx2 + length]):
                    flag = False
                    break
                idx2 += length
                if idx2 > len(s):
                    flag = False
                    break

            if flag:
                res.append(sub_res)
        res.append(s)
        return res[::-1]

    def strEqule(self, str1, str2):
        if len(str1) != len(str2):
            return False
        for c1, c2 in zip(str1, str2):
            if c1 != c2:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    str1 = "ABABABAB" * 125
    str2 = "ABC" * 250
    print(sol.gcdOfStrings(str1, str2))