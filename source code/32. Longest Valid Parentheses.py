import numpy
class Solution:
    def refresh(self, i, cer):
        i -= 1
        while i >= 0:
            if cer[i] == 1:
                cer[i] = 2
                return
            i -= 1
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        flag = 0
        cer = []
        while i < len(s):
            if s[i] == '(':
                flag += 1
                cer.append(1)
            else:
                if flag == 0:
                    cer.append(0)
                else:
                    self.refresh(i, cer)
                    flag -= 1
                    cer.append(2)
            i += 1
        # print(cer)
        max = 0
        num = 0
        for j in cer:
            if j == 2:
                num += 1
                if max < num:
                   max = num
            else:
                num = 0
        return max

if __name__ == '__main__':
    sol = Solution()
    s = '((()()())'
    print(sol.longestValidParentheses(s))