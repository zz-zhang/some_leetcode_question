'''
https://leetcode.com/problems/string-to-integer-atoi/
'''


class Solution:
    def __init__(self):
        self.MAX_INT = 2147483647
        self.MIN_INT = -2147483648

    def myAtoi(self, s: str) -> int:
        # remove spaces
        # s = s.replace(' ', '')
        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        if self._is_legal(s):
            if s[0] == '-':
                sign = -1
            else:
                sign = 1
            if s[0] in ['+', '-']:
                s = s[1:]
            i = sign * self._convert(s)
            if i < self.MIN_INT:
                return self.MIN_INT
            elif i > self.MAX_INT:
                return self.MAX_INT
            else:
                return i
        else:
            return 0

    def _convert(self, s):
        legal = [str(i) for i in range(10)]
        res = 0
        for c in s:
            if c not in legal:
                break
            res *= 10
            res += int(c)
        return res

    def _is_legal(self, s):
        begin_with = [str(i) for i in range(10)] + ['-', '+']

        if len(s) == 0:
            return False
        if s[0] not in begin_with:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    string = [
        '42', '   -42', '4193 with words', 'words and 987', '-91283472332'
    ]
    for s in string:
        print(sol.myAtoi(s))