from typing import *

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                stack = self.decode(stack)
            else:
                stack.append(char)
        res = ''.join(stack)
        return res

    def decode(self, stack):
        res = ''
        num = ''
        string = ''
        num_flag = False
        while len(stack) > 0 and (not num_flag or (num_flag and stack[-1] in '0123456789')):
            if stack[-1] in '0123456789':
                num_flag = True
            if not num_flag:
                if stack[-1] != '[':
                    string = string + stack[-1]
            else:
                num = num + stack[-1]
            stack = stack[:-1]
        string = string[::-1]
        if len(num) > 0:
            num = int(num[::-1])
        else:
            num = 1
        print(string, num)

        res = num * string
        # print(res)
        for char in res:
            stack.append(char)
        return stack


if __name__ == '__main__':
    sol = Solution()
    s = "5abc[]2[]"
    print(sol.decodeString(s))