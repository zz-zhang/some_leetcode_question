'''
https://leetcode.com/problems/regular-expression-matching/
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = self._split(p)
        for item in p:
            if len(item) == 1:
                if item[0] != '.' and item[0] not in s:
                    return False
        return self._match(s, p)

    def _len_min(self, p):
        l = 0
        for item in p:
            if '*' not in item:
                l += 1
        return l

    def _match(self, s, p):
        if len(s) == 0:
            if self._len_min(p) == 0:
                return True
            else:
                return False
        if len(p) == 0:
            return False
        # with '*'
        if len(p[0]) == 2:
            # s[0] appears 0 time
            if self._match(s, p[1:]):
                return True
            if s[0] == p[0][0] or p[0][0] == '.':
                # s[0] appears once
                if self._match(s[1:], p[1:]):
                    return True
                # s[0] appears at least 2 times
                if self._match(s[1:], p):
                    return True

        # without '*'
        else:
            if s[0] == p[0][0] or p[0][0] == '.':
                if self._match(s[1:], p[1:]):
                    return True

        return False

    def _split(self, p):
        res = []
        for c in p:
            if c != '*':
                res.append(c)
            else:
                res[-1] = res[-1] + '*'
        return res


if __name__ == '__main__':
    ss = ['a', 'aa', 'aa', 'ab', 'aab', 'mississippi', 'a', 'aaaaaaaaaaaaab']
    pp = ['ab*', 'a', 'a*', '.*', 'c*a*b', 'mis*is*p*', '.*..a*', 'a*a*a*a*a*a*a*a*a*a*c']
    sol = Solution()
    for (s, p) in zip(ss, pp):
        print(sol.isMatch(s, p))