class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        startof = {')': '(', ']': '[', '}': '{'}
        for char in s:
            # breakpoint()
            if char not in startof.keys():
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == startof[char]:
                    stack = stack[:-1]
                else:
                    return False
            # print(stack)
        if len(stack) == 0:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s = "([)]"
    print(sol.isValid(s))
